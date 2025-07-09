from django.contrib import admin
from .models import AboutSection
from django_summernote.admin import SummernoteModelAdmin

@admin.register(AboutSection)
class AboutSectionAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_on')
    search_fields = ['title']
    summernote_fields = ('content',)
