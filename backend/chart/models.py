from django.db import models

# Create your models here.


class PostSnapshot():
    """ Plain model just for grabber. It can't be use in DB
    """
    def __init__(this, time, likes, reposts, comments):
        this.time = time
        this.likes = likes
        this.reposts = reposts
        this.comments = comments
