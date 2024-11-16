FROM python:3.12-slim


COPY ./script.py script.py 

CMD ["python3", "script.py"]