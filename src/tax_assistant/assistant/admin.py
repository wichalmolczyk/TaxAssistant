from django.contrib import admin

# Register your models here.

from .models import Interaction, Session


admin.site.register(Interaction)
admin.site.register(Session)