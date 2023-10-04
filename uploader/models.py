from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.core.validators import FileExtensionValidator
import os

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        name = 'shift.csv'
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class Upload(models.Model):
    name = models.CharField(u"Name", max_length=128)
    upload_file = models.FileField(u"File", storage=OverwriteStorage(), validators=[FileExtensionValidator(allowed_extensions=["csv"])])