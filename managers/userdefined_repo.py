import requests
import json
from sanic.response import text
from aiohttp_client_cache import CachedSession, SQLiteBackend


GITHUB_PAT = "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"
headers = {
        "Authorization": f"Bearer {GITHUB_PAT}"  # Include the token in the headers
    }


'''
def get_userdefined_repository(user_name, repository_name):
    url = f"https://api.github.com/repos/{user_name}/{repository_name}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        contributor_url = data['contributors_url']
        contributor_response = requests.get(contributor_url, headers=headers)
        contributor_data = contributor_response.json()
        contributor_count = 0
        for temp in contributor_data:
            contributor_count += (temp['contributions'])

        final_result = {
            'Repository Name': data['name'],
            'Description': data['description'],
            'Language': data['language'],
            'Fork Count': data['forks_count'],
            'Star Count': data['stargazers_count'],
            'Subscriber Count': data['subscribers_count'],
            'Recent Activity': contributor_count
        }
        return final_result

    else:
        return {'error': 'User not found'}
    
 '''







async def get_userdefined_repository(user_name, repository_name):
    async with CachedSession(cache=SQLiteBackend('demo_cache')) as session:
        url = f"https://api.github.com/repos/{user_name}/{repository_name}"
        async with session.get(url) as response:
            print(f'Is response coming from cache<userdefined_repo.py): {response.from_cache}')
        if response.status == 200:
            data = await response.json()
            contributor_url = data['contributors_url']
            async with session.get(contributor_url) as contributor_response:
                contributor_data = await contributor_response.json()
                contributor_count = 0
                for temp in contributor_data:
                    contributor_count += (temp['contributions'])

                final_result = {
                    'Repository Name': data['name'],
                    'Description': data['description'],
                    'Language': data['language'],
                    'Fork Count': data['forks_count'],
                    'Star Count': data['stargazers_count'],
                    'Subscriber Count': data['subscribers_count'],
                    'Recent Activity': contributor_count
                }
            return final_result

        else:
            return {'error': 'Invalid username or repository name entered'}



