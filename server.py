import os
import requests
import random
from flask import Flask, jsonify, request, render_template

import quotes

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.route('/', methods=["GET"])
def index():
    """Return the main page."""

    scope = "commands"
    client_id = os.environ.get('SLACK_CLIENT_ID')
    redirect_uri = "https://spock-check.herokuapp.com/auth"
    state = "RANDOMSTATE"

    auth_url = ("https://slack.com/oauth/authorize?" +
                "&scope=" + scope +
                "&client_id=" + client_id +
                "&redirect_uri=" + redirect_uri +
                "&state=" + state)

    return render_template('addbutton.html', auth_url=auth_url)


@app.route('/command', methods=["GET"])
def command():
    """Decide how to route the incoming request."""
    payload = request.args
    command_text = payload.get('text', '').strip()
    command_token = payload.get('token', '').strip()

    # FIXME: once this works, update existing slash-command custom integrations
    verification_token = os.environ.get('SLACK_VERIFICATION_TOKEN')
    if command_token != verification_token:
        return invalid_slack_token()

    if command_text == 'gif':
        return get_spock_gif()
    elif command_text == 'quote':
        return get_spock_quote()
    else:
        return get_spock_gif()


@app.route('/quote', methods=["GET"])
def get_spock_quote():
    quote = quotes.get_random_quote(quotes.SPOCK_QUOTES)
    # episode_credit = 'Start Trek, season 2, episode 1 ("Amok Time," 1968)'

    response = {
        "response_type": "in_channel",
        "text": ':spock-hand: Spock-check yourself!\n_"{}"_'.format(quote),
        # "attachments": [{
        #     "color": "3B8FCB",
        #     "fields": [{
        #         "title": "Episode Credit: ",
        #         "value": episode_credit,
        #         "short": True
        #     }]
        # }]
    }

    return jsonify(response)


@app.route('/gif', methods=["GET"])
def get_spock_gif():
    image_url = get_gif('Spock')

    response = {
        "response_type": "in_channel",
        "text": ":spock-hand: Spock-check yourself!\n{}".format(image_url),
    }

    return jsonify(response)


def get_gif(search_term):
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


@app.route('/auth', methods=["GET"])
def confirm_auth():
    """Provide feedback to user about whether or not auth has been successful."""

    error = request.args.get('error')
    auth_code = request.args.get('code')

    # case where user has auth'd
    if not error:
        access_token = get_slack_access_token(auth_code)
        message = "Wahoo! You've authorized Spock-Check!"

    # case wher user has denied auth
    else:
        message = "Spock-Check has NOT been authorized."

    return render_template('auth.html', message=message)


def invalid_slack_token():
    """Return a response if the request token provided is invalid."""

    response = {
        "response_type": "in_channel",
        "text": "Sorry, I don't recognize your team!",
    }

    return jsonify(response)


def get_slack_access_token(auth_code):
    """Makes a request to Slack, using the oauth.access API,
    to get an access token."""

    params = {
        'client_id': os.environ.get('SLACK_CLIENT_ID'),
        'client_secret': os.environ.get('SLACK_CLIENT_SECRET'),
        'code': auth_code,
        'redirect_uri': 'https://spock-check.herokuapp.com/auth'
    }

    response = requests.get('https://slack.com/api/oauth.access', params=params).json()

    return response.get('access_token')

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
