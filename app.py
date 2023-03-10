from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'dataanalyist',
    'location':'Jenin',
    'salary': '1000 ILS'
    
  },  
  {
    'id':2,
    'title': 'data Entry',
    'location':'Nablus',
    'salary': '20000 ILS'
    
  },
    {
    'id':3,
    'title': 'Computer Scientiest',
    'location':'Ramallah',
    'salary': '2000 ILS'
    
  },
  {
    'id':4,
    'title': 'Pharmaciest',
    'location':'Albirah',
    'salary': '4000 ILS'
    
  }
  
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs = JOBS ,company_name = 'Ashraf Abu Alrub')
@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
#to make data dynamic without use db use
#Dynamic Data using Templates
