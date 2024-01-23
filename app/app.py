from flask import Flask, request, jsonify
from app import graph, routes

app = Flask(__name__)
