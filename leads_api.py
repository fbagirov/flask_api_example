from flask import Flask, jsonify, request 

app = Flask(__name__) # instantiating Flask application object
app.config["DEBUG"] = True # starts the debugger

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
    return "<p>A prorotype for a customer data lead API</p>"

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


app.run() # a method that runs the server