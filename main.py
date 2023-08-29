from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/project01')
def project01():
    return render_template('project01.html')

@app.route('/project_cocktail')
def project_cocktail():
    return render_template('project-cocktail.html')

@app.route('/project03')
def project03():
    return render_template('project03.html')



if __name__ == '__main__':
    app.run(debug=True)