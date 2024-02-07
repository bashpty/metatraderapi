FROM mcr.microsoft.com/azure-functions/python:4-nightly-python3.9
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