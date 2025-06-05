from django.db import models

# Create your models here.
class coffee_db(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    # image = models.ImageField(upload_to='coffee_images/')
    image = models.CharField(max_length=2083) # we are tryig to pass the url of the images and the size of the image url = 2083

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Coffee Items"
        ordering = ['name']  # Order by name by default