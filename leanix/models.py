from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    STATUS_CHOICE = (
        ('Pub',  'Publish'),
        ('Drf', 'Draft'),
    )

    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=3)

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])


