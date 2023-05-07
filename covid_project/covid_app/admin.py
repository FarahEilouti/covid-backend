from django.contrib import admin
from .models import Record
from .models import AllCountries

class RecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Record, RecordAdmin)
admin.site.register(AllCountries)