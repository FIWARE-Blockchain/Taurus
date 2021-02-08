from django.apps import AppConfig

class ApisConfig(AppConfig):
    name = 'apis'

    def ready(self):
        print ("Starting 1...")        
        from .controllerConfigsListners import listnerLoop
        import threading
        x = threading.Thread(target=listnerLoop)
        x.start()

