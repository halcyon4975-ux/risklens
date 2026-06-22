def run():
    from app import create_app, db
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.create_all()
    print('created')
    ctx.pop()

if __name__ == '__main__':
    run()
