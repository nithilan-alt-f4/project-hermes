from flask import Flask, request, jsonify, send_from_directory
import yagmail
import random
import os

app = Flask(__name__, static_folder=".")

MESSAGES = [
    """#🇯🇵Japan is turning footsteps into electricity!Using piezoelectric tiles, every step you take generates a small amount of energy Millions of steps together can power LED lights and displays in busy places like Shibuya Station. A brilliant way to create a sustainable and smart city. (syncopation)""",

    """Tonight, @thv took a turn in the audience as he watched @gracieabrams and @dojacat perform at #vogueWorld: Hollywood. No stranger to a fashion show either, the @bts.bighitofficial star dressed in a look that could have easily appeared on the runway.""",

    """No problem! Here's the information about the Mercedes CLR GTR:
The Mercedes CLR GTR is a remarkable racing car celebrated for its outstanding performance and sleek design. Powered by a potent 6.0-liter V12 engine, it delivers over 600 horsepower. 🔧
Acceleration from 0 to 100 km/h takes approximately 3.7 seconds, with a remarkable top speed surpassing 320 km/h. 🥇
Incorporating advanced aerodynamic features and cutting-edge stability technologies, the CLR GTR ensures exceptional stability and control, particularly during high-speed maneuvers. 💨
Originally priced around $1.5 million, the Mercedes CLR GTR is considered one of the most exclusive and prestigious racing cars ever produced. 💰
Its limited production run of just five units adds to its rarity, making it highly sought after by racing enthusiasts and collectors worldwide. 🌎""",

    """IF UR NOT ZOINK STAY BACK
zoink-senpai… ohayo gozaimasu!! 🌸✨
i've been hiding these feelings in my kokoro for so long… but today… I CAN'T HOLD BACK MY LOVE ANYMORE 😭💖
zoink-sama… you are my ichiban… my legend… my TOP 1 OF MY HEART!!! 🔥
the way you play Geometry Dash… it's not human… it's DIVINE…
every click… every jump… every frame-perfect input…
it's like watching a god descend into the level editor itself… 😭🙏""",

    """Are-.. Are y-.. S-.. Are you-.. A-.. Ar-.. areyoushure? Are you sure? SEA SALT! WHERE'S OMNIMAN? How is that possible? I do not wanna hurt you, sir. I NEED YOU SEA SALT!!! Pretty sure. I am omning it, I am omning it so good! WHERE IS HE??? I am so lonely. Threw a trash bag. Stand ready for my arrival, worm. WHAT'S 17 MORE YEARS? ARE YOU SURE?"""
]

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/send", methods=["POST"])
def send_email():
    data = request.json
    recipient = data.get("recipient")
    count = int(data.get("count", 1))
    subject_style = data.get("subject_style", "numbered")

    sender_email = os.environ.get("SENDER_EMAIL")
    app_password = os.environ.get("APP_PASSWORD")

    if not sender_email or not app_password:
        return jsonify({"error": "Missing SENDER_EMAIL or APP_PASSWORD env vars"}), 500

    if not recipient:
        return jsonify({"error": "No recipient provided"}), 400

    if count > 500:
        return jsonify({"error": "Max 500 emails per request"}), 400

    try:
        yag = yagmail.SMTP(sender_email, app_password)
        sent = 0

        for i in range(count):
            body = MESSAGES[i % len(MESSAGES)]

            if subject_style == "numbered":
                subject = f"Message #{i + 1}"
            elif subject_style == "random":
                subject = "Ref: " + ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))
            else:
                subject = f"Message #{i + 1}"

            yag.send(to=recipient, subject=subject, contents=body)
            sent += 1

        return jsonify({"success": True, "sent": sent})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
