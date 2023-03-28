from django.apps import AppConfig


class UsersBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_blog'

    def ready(self):
        import users_blog.signals