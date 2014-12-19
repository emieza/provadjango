from django.contrib import admin

from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    # detail view
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # detail view inlined
    inlines = [ChoiceInline]
    # list view
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text','question','votes')
    
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
