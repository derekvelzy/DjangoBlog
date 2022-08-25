from django.db import models
from django.conf import settings
from django.utils import timezone

# models.Model means its a django model, and it should be saved in the database
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title


# models.CharField - this is how you define text with limit amount of charaters
# models.TextField - for long text without a limit
# models.DateTimeField - a date and time
# models.ForeignKey - link to another model

# def publish(self):
#   