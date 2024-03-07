 FROM python:3.10.12

 ADD main.py /app/main.py
 ADD requirements.txt /app/requirements.txt

 WORKDIR /app

 RUN pip install -r requirements.txt

ENV BO_SVC=test-intercept-bo-svc
ENV BO_PORT=80

CMD ["python", "main.py"]
