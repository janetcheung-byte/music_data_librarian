from django.contrib import admin

# Register your models here.
from .models import MusicMetadata

admin.site.register(MusicMetadata)