FROM tiangolo/uwsgi-nginx-flask:python3.8
RUN pip install --upgrade 'sentry-sdk[flask]==0.16.2'
COPY ./app /app
