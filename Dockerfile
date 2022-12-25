FROM python:3.11

WORKDIR /src

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/src

ENTRYPOINT ["python3"]
