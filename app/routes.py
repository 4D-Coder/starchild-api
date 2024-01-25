from flask import Flask
from app import app

@app.route('/api/v1/')
def welcome():
  return "StarChild API v1"

@app.route('/api/v1/users')
def user_create():
  data = graph.serialize(format='turtle').decode('utf-8')
  return data
