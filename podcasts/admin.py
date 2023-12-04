from django.contrib import admin

# Register your models here.
from .models import Podcast
from .models import Review
from .models import Episode
from .models import ReviewEpisode

admin.site.register(Podcast)
admin.site.register(Review)
admin.site.register(Episode)
admin.site.register(ReviewEpisode)