from django.db import models

class UserProfile(models.Model):
    profile_picture = models.FileField(upload_to='profile_pictures/')

    def __str__(self):
        return f"Profile Picture ({self.id})"
