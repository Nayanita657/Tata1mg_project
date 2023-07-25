import requests
import json
from aiohttp_client_cache import CachedSession, SQLiteBackend
import aiohttp


GITHUB_PAT = "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"
headers = {
        "Authorization": f"Bearer {GITHUB_PAT}"  # Include the token in the headers
    }
'''
def get_user_repository(name):
    url = f"https://api.github.com/users/{name}/repos"
    response = requests.get(url, headers=headers)
    data = response.json()
    repository_names = []
    for temp in data:
        repository_names.append(temp['name'])
    final_result = json.dumps(repository_names)
    return final_result
'''

async def get_user_repos_global(name):
    async with CachedSession(cache=SQLiteBackend('demo_cache')) as session:
        url = f"https://api.github.com/users/{name}/repos"
        async with session.get(url, headers=headers) as response:
            print(f'Is response coming from cache<user_repos.py>: {response.from_cache}')
            return response


async def get_user_repository(name):
    async with aiohttp.ClientSession() as session:
        response = await get_user_repos_global(name)
        if response.status == 200:
            data = await response.json()
            repository_names = []
            for temp in data:
                repository_names.append(temp['name'])
            final_result = json.dumps(repository_names)
            return final_result
        else:
            return {'error': 'User repo not found'}

async def get_user_starred_repository(name):
    async with aiohttp.ClientSession() as session:
        response = await get_user_repos_global(name)
        if response.status == 200:
            data = await response.json()
            starred_repository_name = ""
            max_star = 0
            for temp in data:
                current_star_count = temp['stargazers_count']
                if (max_star < current_star_count):
                    starred_repository_name = temp['name']
                    max_star = current_star_count
            return starred_repository_name
        else:
            return {'error': 'Users repo not found'}



'''
async def get_user_repository(name):
    async with CachedSession(cache=SQLiteBackend('demo_cache')) as session:
        url = f"https://api.github.com/users/{name}/repos"
        async with session.get(url, headers=headers) as response:
            print(f'Is response coming from cache<user_repos.py>: {response.from_cache}')
            if response.status == 200:
                data = await response.json()
                repository_names = []
                for temp in data:
                    repository_names.append(temp['name'])
                final_result = json.dumps(repository_names)
                return final_result
            else:
                return {'error': 'User not found'}
                
'''

'''
def get_user_starred_repository(name):
    url = f"https://api.github.com/users/{name}/repos"
    response = requests.get(url, headers=headers)
    data = response.json()
    starred_repository_name = ""
    max_star = 0
    for temp in data:
        current_star_count = temp['stargazers_count']
        if(max_star < current_star_count):
            starred_repository_name = temp['name']
            max_star = current_star_count

    return starred_repository_name
'''



