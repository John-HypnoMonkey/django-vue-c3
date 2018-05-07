from .models import PostSnapshot
import vk
from django.conf import settings


def parseVK(post_id):
    session = vk.Session(access_token=settings.VK_TOKEN)

    vk_api = vk.API(session)
    if post_id == 0:
        post = vk_api.wall.get(domain=settings.VK_GROUP, count=1, v=5.0)
    else:
        post = vk_api.wall.get(domain=settings.VK_GROUP, count=1, post_id=post_id, v=5.0)
    id_ = post['items'][0]['id']
    likes = post['items'][0]['likes']['count']
    comments = post['items'][0]['comments']['count']
    reposts = post['items'][0]['reposts']['count']
    return PostSnapshot(int(id_), int(likes), int(comments), int(reposts))
