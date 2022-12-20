FROM python:3.8-slim-buster

ADD fibCalc.py .

CMD [ "python", "./fibCalc.py" ]