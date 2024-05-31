from django.db import models
from common.models import BaseModel
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category (BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null= True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
    
    
    
class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.UUIDField()
    image = models.ImageField(upload_to="products/", null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Products"
        
        
class Review (BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.UUIDField()
    rating = models.PositiveIntegerField()
    comment = models.CharField(max_length=300)
    
    def __str__(self):
        return f'Review {self.id} for {self.product.name} by user {self.user}'
    class Meta:
        verbose_name_plural = "Reviews"
            
        
