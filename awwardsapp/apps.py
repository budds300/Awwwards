from django.apps import AppConfig

class AwwardsappConfig(AppConfig):
    name = 'awwardsapp'

    def ready(self):
        import awwardsapp.signals