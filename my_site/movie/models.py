from django.db import models



class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title