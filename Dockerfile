FROM ubuntu:14.04
RUN apt-get update \
    && apt-get install -y python-pip \
    && apt-get install -y git
WORKDIR /myapp
ADD app app
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD python app/main.py
EXPOSE 5000
