from django.contrib import admin
from .models import User, Buraco, Agent

# Register your models here.
admin.site.register(User)
admin.site.register(Buraco)
admin.site.register(Agent)