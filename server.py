import os
import requests
import random
from flask import Flask, jsonify, request

from pprint import pprint

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.route('/', methods=["GET"])
def index():
    image_url = get_gif('Spock')
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

def get_gif(search_term='Spock'):
    """Hit up the Giphy Search API to get a random gif."""

    # FIXME: currently hardcoded and not doing any parsing, substitution
    query_term = search_term

    params = {
        # FIXME: Currently using beta key, should request actual for production.
        'api_key': os.environ.get('GIPHY_API_KEY'),
        'q': query_term,
        'limit': 1,
        'offset': 0, #results offset, defaults to 0
        'rating': 'g', #limit results to those rated (y, g, pg, pg-13 or r)
        'fmt': 'json', #other option is HTML, for debugging in browser
    }

    initial_response = requests.get('http://api.giphy.com/v1/gifs/search', params=params).json()

    results_count = initial_response['pagination']['total_count']
    offset = random.randrange(1, results_count-1)
    params['offset'] = offset

    final_response = requests.get('http://api.giphy.com/v1/gifs/search', params=params).json()
    gif_url = final_response['data'][0]['images']['original']['url']

    return gif_url


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
