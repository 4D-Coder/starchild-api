from rdflib import Graph
from rdflib.namespace import DC, RDF
from rdflib.store import Store
from rdflib_sqlalchemy import registerplugins

registerplugins()

def create_rdf_graph(data: dict):
  g = Graph()

  # game = BNode()

  # g.add((game, DC.title, Literal("Lies of P")))
  # g.add((game, DC.developer, Literal("NEOWIZ")))
  # g.add((game, DC.publisher, Literal("NEOWIZ")))
  # g.add((game, DC.release_date, Literal("September 18, 2023")))
  # g.add((game, DC.genres, Literal("souls-like")))

  return g

