FROM  mcr.microsoft.com/windows/nanoserver:ltsc2019

ENV PYTHONIOENCODING UTF-8

ENV PYTHON_VERSION 3.9.11

RUN $url = ('https://www.python.org/ftp/python/{0}/python-{1}-amd64.exe' -f ($env:PYTHON_VERSION -replace '[a-z]+[0-9]*$', ''), $env:PYTHON_VERSION); \
	Write-Host ('Downloading {0} ...' -f $url); \
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $url -OutFile 'python.exe'; \
	\
	Write-Host 'Installing ...'; \
# https://docs.python.org/3/using/windows.html#installing-without-ui
	$exitCode = (Start-Process python.exe -Wait -NoNewWindow -PassThru \
		-ArgumentList @( \
			'/quiet', \
			'InstallAllUsers=1', \
			'TargetDir=C:\Python', \
			'PrependPath=1', \
			'Shortcuts=0', \
			'Include_doc=0', \
			'Include_pip=0', \
			'Include_test=0' \
		) \
	).ExitCode; \
	if ($exitCode -ne 0) { \
		Write-Host ('Running python installer failed with exit code: {0}' -f $exitCode); \
		Get-ChildItem $env:TEMP | Sort-Object -Descending -Property LastWriteTime | Select-Object -First 1 | Get-Content; \
		exit $exitCode; \
	} \
	\
# the installer updated PATH, so we should refresh our local value
	$env:PATH = [Environment]::GetEnvironmentVariable('PATH', [EnvironmentVariableTarget]::Machine); \
	\
	Write-Host 'Verifying install ...'; \
	Write-Host '  python --version'; python --version; \
	\
	Write-Host 'Removing ...'; \
	Remove-Item python.exe -Force; \
	Remove-Item $env:TEMP/Python*.log -Force; \
	\
	Write-Host 'Complete.'



WORKDIR /python-docker

COPY . .
RUN rm -Rf venv

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8080 80 443 22
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/venv/bin:$PATH"
CMD [ "python", "app.py"]