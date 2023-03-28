# Write a cloud function that acts as an API and returns a context (an example json containing dummy data) to a user. 
# This is being built for a user that is interested in creating their own API to use with Snowplow's API Request Enrichment functionality.
# The purpose is to show them the pattern for how this can be done, and they can then go away and make their own.
# Need to write something in the process documentation that tells user how to deploy a Cloud Function/Lambda to be their own api
# Potential one-click deployment using the cloud run button? That might be overkill for this simple example.
import os
from faker import Faker
from flask import Flask, jsonify, request
from http import HTTPStatus
from werkzeug.exceptions import HTTPException, abort


def get_secret(secret_name: str) -> str:
    """Get secret from Google Secrets Manager, set when configuring the cloud function."""
    secret_string = os.environ.get(secret_name)
    # secret_string = '123' #Just for local testing
    return secret_string


app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return jsonify({"message": "Welcome!"}), HTTPStatus.OK

@app.route('/user', methods=['GET'])
def user():
    """
    For a given id given in the query string, return the name and occupation of the user.
    Returns a context that can be attached to a snowplow event.
    """
    # auth = request.authorization

    # stored_password = get_secret("api_password")

    # if auth and auth.username == 'test' and auth.password == stored_password:
    fake = Faker()
    Faker.seed(request.args.get('id'))

    context = {
        "name": fake.name(),
        "occupation": fake.job()
    }

    return jsonify(context), HTTPStatus.OK
    # else:
    #     return abort(HTTPStatus.UNAUTHORIZED, {"error": "Please provide correct auth"})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5050))
    app.run(debug=True, host='0.0.0.0', port=port)