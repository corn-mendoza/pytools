FROM python:3.9

#copy all the files
COPY . /app

WORKDIR /app

#Install the dependencies
RUN apt-get -y update
RUN pip3 install -r requirements.txt

EXPOSE 5001

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]