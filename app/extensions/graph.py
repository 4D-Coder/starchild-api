from rdflib import URIRef, Graph
from rdflib.namespace import DC, RDF
from rdflib.store import Store

def build_triple(obj, attributes):
  import ipdb; ipdb.set_trace()
  user = URIRef(f"http://starchild.io/api/v1/register#{attributes['username']}")

  # g.add((game, DC.title, Literal("Lies of P")))
  # g.add((game, DC.developer, Literal("NEOWIZ")))
  # g.add((game, DC.publisher, Literal("NEOWIZ")))
  # g.add((game, DC.release_date, Literal("September 18, 2023")))
  # g.add((game, DC.genres, Literal("souls-like")))

