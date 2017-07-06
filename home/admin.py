from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Discussion)
admin.site.register(DiscussionComment)
admin.site.register(Question)
admin.site.register(QuestionComment)