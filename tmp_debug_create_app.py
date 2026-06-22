import app
from app import create_app
A = create_app()
print('A is app module:', A is app)
print('A repr:', repr(A))
print('type A:', type(A))
print('App has run attr:', hasattr(A, 'run'))
print('App dir sample:', [n for n in dir(A) if not n.startswith('__')][:10])
