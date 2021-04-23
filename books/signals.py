from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Book,ISBN

@receiver(post_save,sender=Book)
def after_book_creation(sender,instance,created,*args,**kwargs):
    if created:
        isbn_instance=ISBN.objects.create(author_title=instance.author,book_title=instance.title)
        instance.isbn=isbn_instance
        instance.save()
    else:
        print("ay 7aga")