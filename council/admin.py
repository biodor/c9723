from django.contrib import admin 
from .models import Profile, Position, Council, CouncilName, OfficersTerm

admin.site.register(Profile)
admin.site.register(Council)
admin.site.register(CouncilName)
admin.site.register(Position)
admin.site.register(OfficersTerm)
