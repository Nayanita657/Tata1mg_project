import requests
from sanic.response import text, json
import aiohttp
import os
from aiohttp_client_cache import CachedSession, SQLiteBackend


'''
def get_user_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        user = {
            'username': data['login'],
            'name': data['name'],
            'email': data['email'],
            'bio': data['bio'],
            'followers': data['followers'],
            'following': data['following'],
            'public_repos': data['public_repos'],
            'followers_url': data['followers_url'],
            'following_url': data['following_url'],
            'created at': data['created_at'],
            'updated at': data['updated_at']

        }
        return user
    else:
        return json({'error': 'User not found'}, status=404)

'''
#GITHUB_PAT = os.environ.get('GITHUB_PAT')
GITHUB_PAT = "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"
headers = {
        "Authorization": f"Bearer {GITHUB_PAT}"  # Include the token in the headers
    }
async def get_user_profile(username):
    async with CachedSession(cache=SQLiteBackend('demo_cache')) as session:
        url = f"https://api.github.com/users/{username}"
        async with session.get(url, headers=headers) as response:
            print(f'Is response coming from cache<user_info.py): {response.from_cache}')
            if response.status == 200:
                data = await response.json()
                user = {
                    'username': data['login'],
                    'name': data['name'],
                    'email': data['email'],
                    'bio': data['bio'],
                    'followers': data['followers'],
                    'following': data['following'],
                    'public_repos': data['public_repos'],
                    'followers_url': data['followers_url'],
                    'following_url': data['following_url'],
                    'created at': data['created_at'],
                    'updated at': data['updated_at']
                }
                return user
            else:
                return {'error': 'User not found'}




# async def get_user_repos(username):
#     print("HELLO")
#     async with aiohttp.ClientSession() as session:
#         url = f"https://api.github.com/users/{username}/repos"
#         print("HERE")
#         async with session.get(url) as response:
#             if response.status == 200:
#                 data = await response.json()
#                 print("HERE")
#                 # user = {}
#                 # i=1
#                 # for key in data:
#                 #     user[f'Repo{i}'] = key['name']
#                 #
#                 # print(user)
#                 return data
#             else:
#                 return {'error': 'User not found'}