from django.db import models
from django.utils.crypto import get_random_string
from utils.repo_operators import SENTINEL, filter_sentinel
from user_manager.models import User


def get(pk):
    try:
        return User.objects.get(pk=pk)
    except models.ObjectDoesNotExist:
        return None


def filter_(phone=SENTINEL):
    kwargs = filter_sentinel(locals().copy())
    return User.objects.filter(**kwargs)


def get_or_create(phone, first_name, last_name=SENTINEL, password=SENTINEL, email=SENTINEL):
    kwargs = filter_sentinel(locals().copy())
    kwargs.pop("phone")

    if password == SENTINEL or not password:
        kwargs["password"] = get_random_string()

    user, created = User.objects.get_or_create(
        phone=phone, username=phone, defaults=kwargs
    )
    return user


def update(
    user_id, first_name=SENTINEL, last_name=SENTINEL, email=SENTINEL, phone=SENTINEL, password=SENTINEL
):
    kwargs = filter_sentinel(locals().copy())
    kwargs.pop("user_id")
    kwargs.pop("password")

    User.objects.filter(pk=user_id).update(**kwargs)
    user = get(pk=user_id)

    if password != SENTINEL:
        user.reset_password(password=password)
    return user
