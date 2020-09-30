cd to dockerfile

docker build --flaskapp .
docker run -d --name flaskapp -p 80:80 tiangolo/uwsgi-nginx-flask
