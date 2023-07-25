from sanic import  Sanic
from sanic.response import text,json

app = Sanic('sdvdjsv')
db = {}

@app.route('/')
async def hello(request):
    return text('hello!')

@app.get("/test")
async def hello_def(request):
    return json({
        "message": "hello, test"
    })

@app.get("/name")
async def add_name(request):
    name = request.json
    db[name['id']] = name['name']
    return text('success')

@app.get("/name/<id>")
async def get_name(request, id):
    name = db[int(id)]
    return json({'name': name})


if __name__ == '__main__':
    app.run()


@app.get('/compare')
async def compare(request):
    args = request.args
    print(args)
    if args.get('user1') and args.get('user2'):
        user1_info = await fetch_user(args.get('user1'))
        user2_info = await fetch_user(args.get('user2'))
        return await render('compare_user.html', context={
            'user1':user1_info,
            'user2':user2_info
        })
     else:
		response.BadRequest()

    { %
    for k, v in user1.items %}
    {{k}}: {{v}}


    { % endfor %}

    { %
        for k, v in user2.items %}
        {{k}}: {{v}}
        { % endfor %}


<h1>Hello, world!!!!</h1>
    <ul>
        <li>Username: {{ user1.username }}</li>
        <li>Name: {{ user1.name }}</li>
        <li>Email: {{ user1.email }}</li>
        <li>Bio: {{ user1.bio }}</li>
        <li>Followers: {{ user1.followers }}</li>
        <li>Following: {{ user1.following }}</li>
        <li>Public Repos: {{ user1.public_repos }}</li>
        <li>Followers URL: {{ user1.followers_url }}</li>
        <li>Following URL: {{ user1.following_url }}</li>
        <li>Created At: {{ user1['created at'] }}</li>  <!-- Use square brackets to access field with spaces -->
        <li>Updated At: {{ user1['updated at'] }}</li>  <!-- Use square brackets to access field with spaces -->
        <li>Starred Repository: {{ user1['starred repository'] }}</li>  <!-- Use square brackets to access field with spaces -->
    </ul>


<h1>User Comparison</h1>
    <table>
        <thead>
            <tr>
                <th>Username</th>
                <th>Name</th>
                <th>Email</th>
                <th>Bio</th>
                <th>Followers</th>
                <th>Following</th>
                <th>Public Repos</th>
                <th>Followers URL</th>
                <th>Following URL</th>
                <th>Created At</th>
                <th>Updated At</th>
                <th>Starred Repository</th>
            </tr>
        </thead>
        <tbody>
            {% for key, value in users.items() %}
            <tr>
                <td>{{ value['username'] }}</td>
                <td>{{ value['name'] }}</td>
                <td>{{ .email }}</td>
                <td>{{ user.bio }}</td>
                <td>{{ user.followers }}</td>
                <td>{{ user.following }}</td>
                <td>{{ user.public_repos }}</td>
                <td>{{ user.followers_url }}</td>
                <td>{{ user.following_url }}</td>
                <td>{{ user['created at'] }}</td>
                <td>{{ user['updated at'] }}</td>
                <td>{{ user['starred repository'] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>


{
    "username1": {
        "username": "Nayanita657",
        "name": null,
        "email": null,
        "bio": "IIT JODHPUR",
        "followers": 3,
        "following": 1,
        "public_repos": 20,
        "followers_url": "https://api.github.com/users/Nayanita657/followers",
        "following_url": "https://api.github.com/users/Nayanita657/following{/other_user}",
        "created at": "2021-10-25T18:17:21Z",
        "updated at": "2023-05-03T06:23:03Z",
        "starred repository": "-Contextual-Journal-Recommendation-and-Query-Search-Engine-Using-Word-Embedding"
    },
    "username2": {
        "username": "google",
        "name": "Google",
        "email": "opensource@google.com",
        "bio": "Google ❤️ Open Source",
        "followers": 26322,
        "following": 0,
        "public_repos": 2535,
        "followers_url": "https://api.github.com/users/google/followers",
        "following_url": "https://api.github.com/users/google/following{/other_user}",
        "created at": "2012-01-18T01:30:18Z",
        "updated at": "2021-12-30T01:40:20Z",
        "starred repository": "accompanist"
    }
}