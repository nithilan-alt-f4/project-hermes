import resend
import csv
import random
from pymongo import MongoClient
from flask import render_template, Flask, request
import os

api_key1 = os.environ.get("KEY_1")
api_key2 = os.environ.get("KEY_2")
api_key3 = os.environ.get("KEY_3")
MONGODB_CONNECTION_STRING = os.environ.get("MONGO_URL")

client = MongoClient("MONGODB_CONNECTION_STRING")
db = client["athena"]
email_stats = db["email_stats"]

domains = {
    "sgsdfgdsf.jo3.org"    : api_key1,
    "f2.sgsdfgdsf.jo3.org" : api_key2,
    "f3.sgsdfgdsf.jo3.org" : api_key3,
}


def generate_full_name(filepath):
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
    first = random.choice(reader)["Name"].capitalize()
    last = random.choice(reader)["Name"].capitalize()
    return f"{first} {last}"

def generate_full_name_nospace(filepath):
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
    first = random.choice(reader)["Name"]
    last = random.choice(reader)["Name"]
    return f"{first}{last}"

def genereate_random_domain():
    domain = random.choice(list(domains.keys()))
    api_key = domains[domain]
    return domain, api_key

def record_email_sent(domain):
    email_stats.update_one({"_id": domain}, {"$inc": {"count": 1}}, upsert=True)

def check_api_usage(domain):
    doc = email_stats.find_one({"_id": domain})
    doc_usage = doc["count"] if doc else 0
    if doc_usage >= 100:
        domains.pop(domain, None)
        return False
    return True


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    logs = None
    if request.method == "POST":
        num_emails = int(request.form["count"])
        recipient = request.form["recipient"]
        logs = []
        a2 = 0
        a1 = 0

        for i in range(0, num_emails):
            if not domains:
                logs.append("All domains exhausted for today.")
                break

            a1 += 1
            a2 += 2
            full_name = generate_full_name(names.csv)
            full_name_nospace = generate_full_name_nospace(names.csv)

            rand_domain, api_key = genereate_random_domain()
            if not check_api_usage(rand_domain):
                continue

            params = {
                "from": f"{full_name}<{full_name_nospace}@{rand_domain}>",
                "to": [recipient],
                "subject": f"1d 🎉 - {a1}",
                "html": f"<h1>{a2}</h1><p>{a2}</p>",
            }
            resend.api_key = api_key
            resend.Emails.send(params)
            record_email_sent(rand_domain)
            logs.append(f"Sent #{a1} via {rand_domain}")
    return render_template("index.html", logs=logs)


if __name__ == "__main__":
    app.run(debug=True)

