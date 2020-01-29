FROM python:3.7

ADD . /code
WORKDIR /code
RUN sudo pip3 install -r requirements.txt
CMD ["python", "main.py"]
