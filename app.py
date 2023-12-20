from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Remote'
}, {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'California, USA',
    'salary': '$120,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  print("I'm inside the if now")
  app.run(host='0.0.0.0', debug=True)
