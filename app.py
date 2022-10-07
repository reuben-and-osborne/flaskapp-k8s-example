from flask import Flask 

app = Flask(__name__)

DATA = [
    {
    "first_name": "Reuben",
    "last_name": "Osborne",
    "age": 26
    },
    {
    "first_name": "Ed",
    "last_name": "Cox",
    "age": 26
    }
]

@app.route('/data')
def get_data():
    return DATA

@app.route('/data/<name>')
def get_by_name(name):
    results = []
    for person in DATA:
        if person['first_name'] == name:
            results.append(person)
        elif person['last_name'] == name:
            results.append(person)
    return results

if __name__ == "__main__":
    app.run(debug=True)
