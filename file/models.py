from django.db import models

# Create your models here.
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()
class Map(models.Model):
    id = models.AutoField( primary_key=True)
    map_name = models.CharField(max_length=200)
    map_data = models.FileField(upload_to='/maps', storage=gd_storage)