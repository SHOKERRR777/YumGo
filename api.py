from flask import Flask, render_template, request

app = Flask(__name__)

@app.router('/')
def menu_food():
    None