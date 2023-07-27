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
import asyncio
from sanic import exceptions


blueprint_app = Blueprint("GIT")

@blueprint_app.get("/users/<username:str>")
async def get_user(request, username):
    profile = await get_user_profile(username)
    if profile == {'error': 'User not found'}:
        return json({"error": "user not found"}, status=400)
    return await render("dummy_user_display.html", context={'user': profile}, status=400)


@blueprint_app.get('/users/<name:str>/repos')
async def get_user_repos(request, name):
    data = await get_user_repository(name)
    if data == {'error': 'User not found'}:
        return json({"error": "user not found"}, status=400)
    data['username'] = name
    return await render("dummy_user_repos.html", context={'repository_names': data}, status=400)


@blueprint_app.get('/repos/<user_name:str>/<repository_name:str>')
async def get_userdefined_repo(request, user_name, repository_name):
    data = await get_userdefined_repository(user_name, repository_name)
    if data == {'error': 'Invalid username or repository name entered'}:
        return json({'error': 'Invalid username or repository name entered'}, status=400)
    return await render("dummy_userdefined_repo.html", context={'data': data}, status=400)


@blueprint_app.get('/users/<name:str>/repos/sort')
async def get_user_sortedrepos(request, name):
    start_time1 = time.time()
    query_params = request.args
    try:
        sorting_type = query_params['type'][0]
        valid_sorting_types = ['star', 'fork', 'recent activity']
        if sorting_type not in valid_sorting_types:
            return json({"error": "Invalid sorting type. Valid sorting types are star, fork, and recent activity."},
                        status=400)
        data = await get_user_sorted_repository(name, sorting_type)
        if data == {'error': 'User not found'}:
            return json({"error": "user not found"}, status=400)
        end_time1 = time.time()
        elapsed_time1 = start_time1 - end_time1
        return await render("dummy_sort_repo.html", context={'data': data}, status=400)
    except KeyError:
        return json({"error": "Invalid request"}, status=400)


@blueprint_app.get('/users/user_compare')
async def get_compare(request):
    try:
        query_params = request.args
        username1 = query_params['username1'][0]
        username2 = query_params['username2'][0]
        user_response1 = asyncio.get_event_loop().create_task(get_user_profile(username1))
        user_response2 = asyncio.get_event_loop().create_task(get_user_profile(username2))

        user1_Starred_repo = asyncio.get_event_loop().create_task(get_user_starred_repository(username1))
        user2_Starred_repo = asyncio.get_event_loop().create_task(get_user_starred_repository(username2))

        await asyncio.gather(*[user_response1, user_response2, user1_Starred_repo, user2_Starred_repo],
                            return_exceptions=True)

        user_response1_result = user_response1.result()
        user_response2_result = user_response2.result()
        if user_response1_result == {'error': 'User not found'} or user_response2_result == {'error': 'User not found'}:
            return json({"error": "user not found"}, status=400)

        user1_Starred_repo_result = user1_Starred_repo.result()
        user2_Starred_repo_result = user2_Starred_repo.result()
        user_response1_result['Most Starred Repo'] = user1_Starred_repo_result
        user_response2_result['Most Starred Repo'] = user2_Starred_repo_result
        return await render("dummy_user_compare.html", context={'content1': user_response1_result, 'content2': user_response2_result}, status=400)

    except:
        return json({"error": "Invalid request"}, status=400)

@blueprint_app.post('/users/repo_compare')
async def get_repo_compare(request):
    try:
        body = request.json
        username1 = body['username1']
        username2 = body['username2']
        repo1 = body['repo1']
        repo2 = body['repo2']
        repo_details1 = asyncio.get_event_loop().create_task( get_userdefined_repository(username1,repo1))
        repo_details2 = asyncio.get_event_loop().create_task(get_userdefined_repository(username2,repo2))
        group = asyncio.gather(*[repo_details1,repo_details2],return_exceptions=True)
        await group
        repo_details1_result = repo_details1.result()
        repo_details2_result = repo_details2.result()
        repo_details1_result['username1'] = username1
        repo_details2_result['username2'] = username2
        return await render("dummy_repo_compare.html", context={'content1': repo_details1_result, 'content2': repo_details2_result},
                        status=400)
    except:
        return json({"error": "Invalid request"}, status=400)




