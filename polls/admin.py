from django.contrib import admin

# Register your models here.
from django.contrib import admin
from polls.models import Poll,Choice;

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]

admin.site.register(Poll,PollAdmin)