from django.contrib import admin

from .models import User, Document, Viewer
# Register your models here.
admin.site.register(User)
admin.site.register(Document)
admin.site.register(Viewer)
