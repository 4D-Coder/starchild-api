# Essentially a callback module to define functions that run before each test
import pytest

from rdflib import Graph
from app import create_app

# Test instance of the app and RDF Graph
@pytest.fixture()
def app():
  g = Graph()
  app = create_app(g)

  yield app

# Testing client for request/responses
@pytest.fixture()
def client(app):
  return app.test_client()


