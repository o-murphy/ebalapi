from django.apps import AppConfig


class EbalapiServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ebalapi_service'

    def ready(self):
        from ebalapi_service.web import admin
        from ebalapi_service.web import signals
        assert signals
        assert admin

        import ebalapi_service.search_indexes
        assert ebalapi_service.search_indexes
