FROM python:3.11-alpine
WORKDIR /app
#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt
RUN mkdir simpleDateTime && cd simpleDateTime
COPY . .
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]