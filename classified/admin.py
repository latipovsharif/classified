from django.contrib import admin

from classified.models import (
    City,
    Classified,
    ViewCounter
)

# Register your models here.

admin.site.register(City)
admin.site.register(Classified)
admin.site.register(ViewCounter)