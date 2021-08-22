FROM python:3.7-alpine

#recomended in containers
#avoid  python to buffer the outputs, prints it directly
ENV PYTHONUNBUFFERED 1

# Install all dependecies
COPY ./requirements.txt /requirements.txt
# Install postgresql client
RUN apk add --update --no-cache postgresql-client
# Install temporary packages
RUN apk add --update --no-cache --virtual .tmp-build-deps \
			gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
# Delete temporary packages
RUN apk del .tmp-build-deps

# Make folder to store application
RUN mkdir /app
WORKDIR /app
COPY ./ /app

# User that's going to run app -D
RUN adduser -D user
USER user