import time
from django.core.signals import request_finished
from django.dispatch import receiver
import datetime

@receiver(request_finished)
def my_signal_handler(sender, **kwargs):
    print(f"Signal received at: {datetime.datetime.now()}")
    time.sleep(5)  # Simulate long-running task
    print(f"Signal completed at: {datetime.datetime.now()}")

# Trigger the signal (e.g., through an HTTP request)
