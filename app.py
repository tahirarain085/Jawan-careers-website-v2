from flask import Flask,render_template,jsonify
# from database import load_jobs_from_db
from db import load_jobs_from_db
app = Flask(__name__)




@app.route('/')

def home():
    jobs = load_jobs_from_db()
   
    return render_template("home.html",jobs=jobs,company_name="Jawan")


@app.route('/api/jobs')

def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify( jobs)







print(__name__)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True )