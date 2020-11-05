from flask import Flask, request, redirect, url_for, render_template
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('ingrese.html')

@app.route('/', methods=['POST'])
def my_form_post():
    upper = request.form['text']
    lower = request.form['text']
    processed_upper = upper.upper()
    processed_lower = lower.lower()
    return processed_upper
    return processed_lower
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)