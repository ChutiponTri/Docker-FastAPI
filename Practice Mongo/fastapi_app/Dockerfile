FROM python:3.12

WORKDIR /fastapi_app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8305

# ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8305"]