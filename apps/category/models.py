from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Category')
    
    parent = models.ForeignKey(
        'self', related_name='children', on_delete=models.CASCADE, blank=True, null=True
    )
    
    name = models.CharField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to='media/categories/')
        
    def __str__(self) -> str:
        return self.name
    
    def get_thumbnails(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return ''