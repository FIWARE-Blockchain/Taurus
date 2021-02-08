# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip3 install --upgrade pip
RUN apk update && apk add python3-dev && apk --no-cache add gcc musl-dev
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# copy project
COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "migrate"]

CMD ["python3", "manage.py", "runserver"]
