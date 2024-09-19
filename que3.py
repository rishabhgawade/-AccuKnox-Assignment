from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    if transaction.get_autocommit():
        print("Running outside of a transaction")
    else:
        print("Running inside a transaction")

def my_view(request):
    with transaction.atomic():
        instance = MyModel.objects.create(name="Test")
        print("Model saved within transaction")
    return HttpResponse("Done")
