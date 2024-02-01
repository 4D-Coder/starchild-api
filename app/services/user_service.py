from app.models.dataclasses import User

def build_user(s, p, o):
  user = User(s=s, o=o, p=p )
  import ipdb; ipdb.set_trace()
