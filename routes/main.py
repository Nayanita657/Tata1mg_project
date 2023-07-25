from sanic import Sanic,response, Blueprint
from sanic.response import text, json
from sanic.request import Request
import sys
sys.path.append('/Users/nayanita.saha/temp/temp_service')
from managers.user_info import get_user_profile
from managers.user_repos import get_user_repository
from managers.userdefined_repo import get_userdefined_repository
from managers.user_sortedrepo import get_user_sorted_repository
from managers.user_repos import  get_user_starred_repository
from managers.user_profile_compare import get_user_profile_compare
from sanic_ext import render
import time


blueprint_app = Blueprint("GIT")

@blueprint_app.get("/users/<username>")
async def get_user(request, username):
    profile = await get_user_profile(username) # Await the coroutine
    '''
    if profile:
        return json(profile)
    else:
        return json({"error": "User not found"}, status=404)
    '''
    return await render("user_display.html", context={'user': profile}, status=400)


@blueprint_app.get('/users/<name:str>/repos')
async def get_user_repos(request, name):
    data = await get_user_repository(name)
    if data:
        return json(data)
    else:
        return json({"error": "User not found"}, status=404)



@blueprint_app.get('/repos/<user_name:str>/<repository_name:str>')
async def get_userdefined_repo(request, user_name, repository_name):
    data = get_userdefined_repository(user_name, repository_name)
    if data:
        return json(data)
    else:
        return json({"error": "User not found"}, status=404)



@blueprint_app.get('/users/<name:str>/repos/sort')
async def get_user_sortedrepos(request, name):
    start_time1 = time.time()
    query_params = request.args
    sorting_type = query_params['type'][0]
    data = await get_user_sorted_repository(name, sorting_type)
    end_time1 = time.time()
    elapsed_time1 = start_time1 - end_time1
    if data:
        print(f"Function execution time: {elapsed_time1:.6f} seconds")
        return json(data)
    else:
        return json({"error": "User not found"}, status=404)


@blueprint_app.get('/users/compare_repo')
async def get_compare(request):
    query_params = request.args
    username1 = query_params['username1'][0]
    username2 = query_params['username2'][0]
    data = await get_user_profile_compare(username1, username2)

    '''
    if data:
        return json(data)
    else:
        return json({"error": "User not found"}, status=404)
    '''

    return await render("test.html", context={'user': data}, status=400)

'''
    table_data = [{**{"Username": key}, **value} for key, value in data.items()]

    # Render the table as HTML using Jinja2 template
    template = Template('<table>{{ table }}</table>')
    table_html = template.render(table=table_data)

    # Return the HTML table as the response with content type 'text/html'
    return response.html(table_html)
    response.
'''







