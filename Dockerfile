FROM python:3.9.10

WORKDIR /TotalSecurity
COPY . /TotalSecurity
 
RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "TotalSecurity"]
