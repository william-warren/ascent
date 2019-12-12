from django.contrib import admin
from initiative.models import Initiative, User, StatusReport

# Register your models here.
admin.site.register(Initiative)
admin.site.regiester(StatusReport)
