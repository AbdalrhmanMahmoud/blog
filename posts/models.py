from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse


# central in the data from views
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False)


# Post items
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True)
    content = models.CharField(max_length=5000)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True,  blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    p = models.CharField(max_length=10)
    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]

