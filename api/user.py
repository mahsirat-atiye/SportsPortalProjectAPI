import random
import string

from sport.models import ForgottenUser, User, ActivateUser


def generate_hash():

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))


def request_forgotten(user):
    rand = generate_hash()
    ForgottenUser.objects.filter(user=User.objects.filter(username=user)).update_or_create(key=rand)

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


def validate_user(hashcode):
    try:
        print(ActivateUser.objects.filter(key=hashcode)[0])
    except IndexError:
        try:
            print(ForgottenUser.objects.filter(key=hashcode)[0])
        except IndexError:
            return

