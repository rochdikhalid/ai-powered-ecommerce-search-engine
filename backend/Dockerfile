FROM python:3.12  

WORKDIR /app 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

# Expose the port your app runs on
EXPOSE 8000

CMD ["uvicorn", "src.main:app --host 0.0.0.0"]  