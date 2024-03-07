 FROM python:3.10.12

 ADD main.py /app/main.py
 ADD requirements.txt /app/requirements.txt

 WORKDIR /app

 RUN pip install -r requirements.txt

 CMD ["python", "main.py"]
