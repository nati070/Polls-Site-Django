from django.contrib import admin
from .models import Question , Choice

# Register your models here.
#admin.site.register(Question)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    list_display = ('question_text' , 'pub_date' , 'was_published_recently')
    list_filter = ['pub_date']
# the date came before the text question.     
    fileds = ['pub_date' , 'question_text']
#if we want to improve our fildes to filedsets.
    fieldsets = [
        (None, {"fields": ['question_text']}),
        ('Date Information' , {"fields" : ['pub_date'] , 'classes' : ['collapse']}),]
    inlines = [ChoiceInline]
admin.site.register(Question , QuestionAdmin)

#this will give us the ablilty to add choices for each question , but it not so efficient , because we want to add choices in better way
#admin.site.register(Choice)
