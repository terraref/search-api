FROM python:3-alpine

EXPOSE 5000

WORKDIR /usr/src/app

RUN apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
    && python3 -m pip install -r requirements.txt --no-cache-dir \
    && apk --purge del .build-deps

RUN pip install connexion \
    sqlalchemy \
    flask-restful \
    flask_wtf \
    flask_cors

COPY . .

CMD ["./server.py"]
