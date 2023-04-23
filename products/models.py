from django.db import models
from django.contrib.auth.models import User

# Choice Fields
CATEGORY_TYPES = (
    ("food", "Food"),
    ("drink", "Drink"),
    ("toys", "Toys"),
    ("technology", "Technology"),
    ("sports", "Sports"),
    ("clothing", "Clothing"),
    ("footwear", "Footwear"),
    ("household", "Household"),
    ("homeware", "Homeware"),
    ("other", "Other")
)


class Product(models.Model):
    """
    Product model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.TextField(blank=True)
    price = models.IntegerField()
    location = models.TextField(blank=True)
    category_type = models.CharField(max_length=50, choices=CATEGORY_TYPES)
    image = models.ImageField(
        upload_to='images/', default='../default_post_lzlyyd', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'
