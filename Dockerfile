FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD uwsgi --module=spacescoop.wsgi --http=0.0.0.0:80
