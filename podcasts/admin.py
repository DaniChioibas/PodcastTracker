from django.contrib import admin

# Register your models here.
from .models import Podcast
from .models import Review
from .models import Tag

admin.site.register(Podcast)
admin.site.register(Review)
admin.site.register(Tag)