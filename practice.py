from sanic import Sanic
from sanic.response import text, json
from managers.user_info import get_user_profile


app = Sanic("MyHelloWorld")
db = {}

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)