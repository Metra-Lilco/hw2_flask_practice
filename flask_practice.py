from flask import Flask, request
from faker import Faker
import csv
import requests


app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/requirements")
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
    content_str = "<br>".join(content)
    return content_str


@app.route("/users/generate")
def fake_users():
    query_param = request.args.get("query", default=100, type=int)
    faker = Faker("uk_UA")
    users = []
    for _ in range(query_param):
        generate = f"{faker.name()} - {faker.email()}"
        users.append(generate)
    faked_users = "<br>".join(users)
    return faked_users


if __name__ == "__main__":
    app.run()
