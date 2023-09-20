from flask import Flask, request
from faker import Faker
import csv
import requests
import json


app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/requirements/")
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
    content_str = "<br>".join(content)
    return content_str


@app.route("/users/generate/")
def fake_users():
    query_param = request.args.get("query", default=100, type=int)
    faker = Faker("uk_UA")
    users = []
    for _ in range(query_param):
        generate = f"{faker.name()} - {faker.email()}"
        users.append(generate)
    faked_users = "<br>".join(users)
    return faked_users


@app.route('/mean/')
def human_mean():
    total_height = 0
    total_weight = 0
    num_rows = 0
    with open("hw.csv", newline="", encoding="utf-8") as human_data:
        csv_reader = csv.reader(human_data, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            if len(row) > 0:
                total_height += float(row[1])
                total_weight += float(row[2])
                num_rows += 1
        total_height_sm = total_height * 2.54
        total_weight_kg = total_weight * 0.45359237
    average_height = round((total_height_sm / num_rows), 0) if num_rows > 0 else 0
    average_weight = round((total_weight_kg / num_rows), 2) if num_rows > 0 else 0
    answer = f"Середній зріст: {average_height} см.<br>Середня вага: {average_weight} кг."
    return answer


@app.route('/space/')
def astros():
    data = requests.get("http://api.open-notify.org/astros.json").json()
    astro_number = "There is no astros in orbit!"
    for key, value in data.items():
        if key == "number":
            astro_number = f"There is {value} astros in orbit"
            break
    return astro_number


if __name__ == "__main__":
    app.run()
