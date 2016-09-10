FROM jesuejunior/python:3
MAINTAINER Jesue Junior <jesuesousa@gmail.com>

WORKDIR /app
COPY requirements.txt .
COPY src/ .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "2", "everest.wsgi:application"]
