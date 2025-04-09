from django.db import models # type: ignore

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "posts"