from sanic import Sanic,response
from routes.main import blueprint_app


app = Sanic("GIT_Project")
app.blueprint(blueprint_app)


if __name__ == '__main__':
    app.run()