from django.contrib import admin

# Register your models here.
from .models import Hours, Review, EmailList, Promotion, Tag, Article, Photos
admin.site.register(Hours)
admin.site.register(Review)
admin.site.register(EmailList)
admin.site.register(Promotion)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Photos)