from flask import Flask, jsonify, request 

app = Flask(__name__) # instantiating Flask application object
#app.config["DEBUG"] = True # starts the debugger
app.config["DEBUG"] = False # comment the line above and switch to False when deploying to production

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


@app.route('/', methods=['GET'])
def home():
    return "A prorotype for a customer data lead API"

@app.route('/api/v1/leads/all', methods=['GET'])
def api_all():
	return jsonify(leads)

@app.route('/api/v1/leads/<int:id>', methods=['GET'])
def api_id(id):
	lead = [lead for lead in leads if lead['id'] == id]
	if len(lead) == 0:
		abort(404)
	return jsonify({'lead': lead[0]})
 
	# Use the jsonify function from Flask to convert our list of
	# Python dictionaries to the JSON format.
#	return jsonify(results)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True) # a method that runs the server