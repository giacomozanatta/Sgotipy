FROM python:latest
RUN pip3 install spotipy &&\
    pip3 install python-dotenv
WORKDIR /app
COPY . ./
