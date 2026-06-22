from app import create_app, db
from sqlalchemy import inspect

app = create_app()
ctx = app.app_context()
ctx.push()
print('engine url=', db.engine.url)
print('tables=', inspect(db.engine).get_table_names())
ctx.pop()
