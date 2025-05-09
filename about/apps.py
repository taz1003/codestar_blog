from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration for the About app.
    This class sets the default auto field type and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
