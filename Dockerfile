FROM python:latest
RUN pip3 install spotipy &&\
    pip3 install python-dotenv &&\
    pip3 install uvloop &&\
    pip3 install grpcio-tools
WORKDIR /app
COPY . ./
