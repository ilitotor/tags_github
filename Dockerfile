FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN mkdir /brainnco
WORKDIR /brainnco/

# Installing OS Dependencies
COPY requirements.txt /brainnco/
RUN pip install -r /brainnco/requirements.txt
COPY . /brainnco

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

