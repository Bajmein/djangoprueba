from django.contrib import admin
from .models import Comentarios


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = 'fecha',

admin.site.register(Comentarios, TaskAdmin)
