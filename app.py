from flask import Flask, render_template

app = Flask(__name__)
projects = [{
    'id':
    1,
    'project':
    'Web Scrapping',
    'skills':
    'urllib python, Python Requests, Selenium, Beautiful Soup'
}, {
    'id':
    2,
    'project':
    'AI model for flare mointoring',
    'skills':
    'Python pandas, sikitlib, matblotlib,microsoft azure, pychatgpt'
}, {
    'id':
    3,
    'project':
    'Web Scrapping',
    'skills':
    'urllib python, Python Requests, Selenium, Beautiful Soup'
}]


@app.route("/")
def hello_world():
  return render_template('home.html',
                         myskills=projects,
                         myname='Hadeel Alghassab')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=True)  #Run Flask server
