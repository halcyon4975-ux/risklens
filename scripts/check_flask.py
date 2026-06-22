import sys
print('executable=', sys.executable)
try:
    import flask
    print('flask ok, version=', getattr(flask, '__version__', 'unknown'))
except Exception as e:
    print('flask import failed:', type(e).__name__, str(e))
