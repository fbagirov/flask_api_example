

# [START gae_python37_app]
from flask import Flask, jsonify, request


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

leads = [
  {
  	"id":1,
    "firstname": "Michael",
    "lastname": "Jordan",
    "address": "1901 West Madison Str",
    "city": "Chicago",
    "state": "IL",
    "zip": 60612,
    "country": "USA"
  },
  {
  	"id":2,
    "firstname": "Bart",
    "lastname": "Simpson",
    "address": "1 Evergreen Street",
    "city": "Springfield",
    "state": "OR",
    "zip": 97403,
    "country": "USA"
  },
  {
  	"id":3,
    "firstname": "Sarah",
    "lastname": "Connor",
    "address": "309 Caldera Canyon, Apt 225",
    "city": "Los Angeles",
    "state": "CA",
    "zip": 90007,
    "country": "USA"
  },
  {
  	"id":4,
    "firstname": "Fred",
    "lastname": "Krueger",
    "address": "1428 Elm Street",
    "city": "Los Angeles",
    "state": "CA",
    "zip": 90008,
    "country": "USA"
  }
]



@app.route('/')
def home():
    """Return a friendly HTTP greeting."""
    return 'A prorotype for a customer data lead API'

@app.route('/api/v1/leads/all', methods=['GET'])
def api_all():
	return jsonify(leads)

@app.route('/api/v1/leads/<int:id>', methods=['GET'])
def api_id(id):
	lead = [lead for lead in leads if lead['id'] == id]
	if len(lead) == 0:
		sys.exit(404)
	return jsonify({'lead': lead[0]})

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
