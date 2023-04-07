from django.db import models
from user.models import UserModel
# Create your models here.
class ProductModel(models.Model):
    class Meta:
        db_table = 'product'

    code = models.CharField(max_length=50, unique=True, default='')
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=0, default='')
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.pk:
            self.stock_quantity = 0
            super(ProductModel, self).save(*args, **kwargs)

