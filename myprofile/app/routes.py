from flask import render_template
from app import app

@app.route('/')
def resume():
    return render_template('resume.html')
