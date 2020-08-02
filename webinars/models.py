from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class webinarsmodel(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    webinar_heading=models.CharField(max_length=100)
    webinar_details=models.TextField()
    webinar_image=models.URLField()
    time=models.DateTimeField()
    status=models.BooleanField(default=False)