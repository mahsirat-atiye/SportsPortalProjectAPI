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
    rand = generate_hash()
    print(rand)
    print(ActivateUser.objects.all())
    print(ActivateUser.objects.filter(user=User.objects.filter(username=user)))
    ActivateUser.objects.filter(user=User.objects.filter(username=user)).update_or_create(key=rand)

    return rand


def validate_user(hashcode):
    print(ActivateUser.objects.filter(key=hashcode))
    print(ForgottenUser.objects.filter(key=hashcode))
