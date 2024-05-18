from django.db import models

import os

def tutorial_image_upload_path(instance, filename):
    # Generate a unique path for each uploaded image
    return os.path.join('tutorial_images', instance.category, filename)

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to=tutorial_image_upload_path)

    def __str__(self):
        return self.title



