import os
from flask import Flask, jsonify, request

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.route('/', methods=["GET"])
def index():
    image_url = 'http://giphy.com/gifs/NpEE2cRs2Amkg'
    text = 'Live long and prosper.'
    episode_credit = 'Start Trek, season 2, episode 1 ("Amok Time," 1968)'

    response = {
        "response_type": "in_channel",
        "text": ":spock-hand: Spock-check yourself!\n{}".format(image_url),
        "attachments": [{
            "text": '"{}"'.format(text),
            "color": "3B8FCB",
            "fields": [{
                "title": "Episode Credit: ",
                "value": episode_credit,
                "short": True
            }]
        }]
    }

    return jsonify(response)

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=PORT)
