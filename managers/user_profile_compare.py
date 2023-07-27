import requests
import json
from sanic import Sanic, response
from managers.user_info import get_user_profile
from managers.user_repos import get_user_starred_repository


async def get_user_profile_compare(username1, username2):
    profile1 = await get_user_profile(username1)
    starred_repo_user1 = get_user_starred_repository(username1)
    profile1['starred repository'] = starred_repo_user1
    profile2 = await get_user_profile(username2)
    starred_repo_user2 = get_user_starred_repository(username2)
    profile2['starred repository'] = starred_repo_user2
    final_data = {
        'username1': profile1,
        'username2': profile2
    }

    return final_data
