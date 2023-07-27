import requests
import json
from managers.userdefined_repo import get_userdefined_repository
from managers.user_repos import get_user_repos_global
import aiohttp
import time

GITHUB_PAT = "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"
headers = {
        "Authorization": f"Bearer {GITHUB_PAT}"  # Include the token in the headers
    }

'''
def get_user_sorted_repository(name, sorting_type):
    #calling api to get all the repository for a particular user
    url1 = f"https://api.github.com/users/{name}/repos"
    response = requests.get(url1, headers=headers)
    if response.status_code == 200:
        user_repos = response.json()
        final_result = []
        for temp in user_repos:
            user_repo_name = temp['name']
            user_defined_repo_info = get_userdefined_repository(name, user_repo_name)
            repo_name = user_defined_repo_info['Repository Name']
            fork_count = user_defined_repo_info['Fork Count']
            star_count = user_defined_repo_info['Star Count']
            Recent_activity = user_defined_repo_info['Recent Activity']
            temp=[]
            temp.append(repo_name)
            temp.append(fork_count)
            temp.append(star_count)
            temp.append(Recent_activity)
            final_result.append(temp)
        if sorting_type == 'star':
            final_result = sorted(final_result, key=lambda x: x[2], reverse=True)
        elif sorting_type == 'fork':
            final_result = sorted(final_result, key=lambda x: x[1], reverse=True)
        elif sorting_type == 'recent activity':
            final_result = sorted(final_result, key=lambda x: x[3], reverse=True)

        result = json.dumps(final_result)
        return result
'''

async def get_user_sorted_repository(name, sorting_type):
    #calling api to get all the repository for a particular user
    async with aiohttp.ClientSession() as session:
        start_time3 = time.time()
        response = await get_user_repos_global(name)
        end_time3 = time.time()
        elapsed_time3 = end_time3 - start_time3
        #print(f"Function execution time API: {elapsed_time3:.6f} seconds")
        if response.status == 200:
            user_repos = await response.json()
            final_result = []
            start_time2 = time.time()
            #print('josn data length',len(user_repos))
            for temp in user_repos:
                user_repo_name = temp['name']
                user_defined_repo_info = await get_userdefined_repository(name, user_repo_name)
                repo_name = user_defined_repo_info['Repository Name']
                fork_count = user_defined_repo_info['Fork Count']
                star_count = user_defined_repo_info['Star Count']
                Recent_activity = user_defined_repo_info['Recent Activity']

                temp=[]
                temp.append(repo_name)
                temp.append(fork_count)
                temp.append(star_count)
                temp.append(Recent_activity)
                final_result.append(temp)

            end_time2 = time.time()
            elapsed_time2 = end_time2 - start_time2
            print(f"Function execution time aftr for loop: {elapsed_time2:.6f} seconds")

            if sorting_type == 'star':
                final_result = sorted(final_result, key=lambda x: x[2], reverse=True)
            elif sorting_type == 'fork':
                final_result = sorted(final_result, key=lambda x: x[1], reverse=True)
            elif sorting_type == 'recent activity':
                final_result = sorted(final_result, key=lambda x: x[3], reverse=True)
            end_time2 = time.time()
            elapsed_time2 = end_time2 - start_time2
            #print(f"Function execution time after sorting: {elapsed_time2:.6f} seconds")
            return {"List": final_result, "Status Code": "200"}

        else:
            return {'error': 'User not found'}






