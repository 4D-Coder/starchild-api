from flask import Flask, request, jsonify
from app import graph, routes
from pymantic import sparql

server = sparql.SPARQLServer('http://127.0.0.1:9999/bigdata/sparql')

starchild = Flask(__name__)


