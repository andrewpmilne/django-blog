from django.contrib import admin
from .models import AboutSection, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(AboutSection)
class AboutSectionAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'updated_on')
    search_fields = ['title']
    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)