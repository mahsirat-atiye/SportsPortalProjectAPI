from django.contrib import admin

# Register your models here.
from sport.models import *

admin.site.register(BasketballTeam)
admin.site.register(BasketballEvent)
admin.site.register(BasketballGame)
admin.site.register(BasketballNonPlayer)
admin.site.register(BasketballPlayer)
admin.site.register(BasketballLeague)

admin.site.register(FootballPlayer)
admin.site.register(FootballEvent)
admin.site.register(FootballGame)
admin.site.register(FootballNonPlayer)
admin.site.register(FootballTeam)
admin.site.register(FootballLeague)

admin.site.register(News)
admin.site.register(Resource)
admin.site.register(Tag)
