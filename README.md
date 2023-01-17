FastAPI + SQLAlchemy 
===

A simple fastapi sqlalchemy example

Requirements
---

This example is made in python 3.9


Install
---

pip install -r requirements.txt

Docker
---

docker build . --tag fastapi-sqlalchemy

docker run -p8080:80 --name fastapi-sqlalchemy fastapi-sqlalchemy