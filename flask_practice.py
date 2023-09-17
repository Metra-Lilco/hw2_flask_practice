from flask import Flask
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


if __name__ == "__main__":
    app.run()
