from rdflib import Graph, plugin, Literal, BNode
from rdflib.namespace import DC, RDF
from rdflib.store import Store
from rdflib_sqlalchemy import registerplugins

registerplugins()

def configure_store():
  id = 'rdf-data-store'
  uri = 'sqlite:///rdf_store.db'
  store = plugin.get('SQLAlchemy', Store)(identifier=id)
  
def create_rdf_graph():
  g = Graph()

  game = BNode()

  g.add((game, DC.title, Literal("Lies of P")))
  g.add((game, DC.developer, Literal("NEOWIZ")))
  g.add((game, DC.publisher, Literal("NEOWIZ")))
  g.add((game, DC.release_date, Literal("September 18, 2023")))
  g.add((game, DC.genres, Literal("souls-like")))

  return g
