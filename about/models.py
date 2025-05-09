from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Stores a single about entry related to a :model:`auth.User`.
    Each about entry has a title, profile image, updated date,
    and content.
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request entry related to a :model:`auth.User`.
    Each request has a name, email, message, and read status.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
