from flask import Flask
from app import app

@app.route('/')
def welcome():
  return "Welcome to the Popular Game Titles API!"

@app.route('/game')
def get_game_info():
  g = graph.create_rdf_graph()
  graph = graph.create_rdf_graph()
  data = graph.serialize(format='turtle').decode('utf-8')
  return data
