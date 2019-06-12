FROM python:3-alpine

EXPOSE 5000

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
    && python3 -m pip install -r requirements.txt --no-cache-dir \
    && apk --purge del .build-deps

RUN pip install connexion \
    pip install sqlalchemy \
    pip install flask_cors

COPY . .

CMD ["./server.py"]
