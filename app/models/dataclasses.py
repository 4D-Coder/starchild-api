from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar('T')

@dataclass(frozen=True)
class User(Generic[T]):
  s: str
  p: str
  o: T
