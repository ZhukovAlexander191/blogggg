from django.contrib import admin

from .models import Article

admin.site.register(Article)

from .models import Post

admin.site.register(Post)

