FROM python:3.11.7-slim
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /temp/requirements.txt
COPY mailing_service /mailing_service
WORKDIR /mailing_service
EXPOSE 8001

RUN pip3 install --upgrade pip
RUN pip3 install -r /temp/requirements.txt
RUN adduser --disabled-password service-user
USER service-user

