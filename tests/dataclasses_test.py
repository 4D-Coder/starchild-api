from app.popos.dataclasses import User

def test_user_instance():
  subject = "User"
  predicate = "name"
  object = "Josh"

  user = User(s=subject, p=predicate, o=object)

  assert isinstance(user, User)
  assert type(user.s) is str
  assert type(user.p) is str
  assert type(user.o) is str


