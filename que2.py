import threading
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_signal_handler(sender, **kwargs):
    print(f"Signal thread ID: {threading.get_ident()}")

def my_view(request):
    print(f"View thread ID: {threading.get_ident()}")
    return HttpResponse("Done")

# Trigger this view to see the thread IDs in both the signal and the view
