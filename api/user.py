import random
import string

from sport.models import ForgottenUser, User, ActivateUser


def generate_hash():

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))


def request_forgotten(user):
    try:
        rand = generate_hash()
        requested_user = User.objects.filter(username=user)[0]
        print(rand)
        ForgottenUser.objects.update_or_create(user=requested_user, key=rand)
    except Exception as e:
        print(e)
        return ''

    return rand


def request_activation(user):
    try:
        rand = generate_hash()
        requested_user = User.objects.filter(username=user)[0]
        print(rand)
        ActivateUser.objects.update_or_create(user=requested_user, key=rand)
    except Exception as e:
        print(e)
        return ''

    return rand


def activation_check(hashcode):
    try:
        user = ActivateUser.objects.filter(key=hashcode)[0].user
        User.objects.filter(username=user).update(is_active=True)
        ActivateUser.objects.filter(key=hashcode)[0].delete()
    except IndexError:
        pass


def forgotten_check(hashcode):
    try:
        user = ForgottenUser.objects.filter(key=hashcode)[0].user
        return user
    except IndexError:
        return None
