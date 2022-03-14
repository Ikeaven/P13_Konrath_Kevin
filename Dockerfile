FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000

# CMD gunicorn --bind=0.0.0.0 oc_lettings_site.wsgi
CMD gunicorn oc_lettings_site.wsgi