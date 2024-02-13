FROM  mcr.microsoft.com/windows-cssc/python:3.9-nanoserver-ltsc2019

# Set the working directory
WORKDIR /app

COPY . .
RUN python -m venv venv
RUN venv\Scripts\activate
RUN python -m pip install -r requirements.txt


EXPOSE 8080 80 443 22
ENTRYPOINT ["python", "app.py"]