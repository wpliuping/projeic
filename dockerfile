FROM python:3.6
COPY . /sqlserver_test
WORKDIR /sqlserver_test
RUN pip install -r requirements.txt
CMD ["python", "/run.py"]