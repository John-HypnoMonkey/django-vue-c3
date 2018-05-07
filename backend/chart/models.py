from django.db import models

# Create your models here.


class PostSnapshot():
    """ Plain model just for grabber. It can't be used in DB
    """
    def __init__(this, post_id, likes, reposts, comments):
        this.post_id = post_id
        this.likes = likes
        this.reposts = reposts
        this.comments = comments
