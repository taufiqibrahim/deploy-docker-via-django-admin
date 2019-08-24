from django.contrib import admin
from dockerman.models import Container


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('container_host', 'container_port', 'container_default_message')
