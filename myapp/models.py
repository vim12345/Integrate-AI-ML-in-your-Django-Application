from django.db import models

class Product(models.Model):
    """
    Model representing a product in the system.
    """

    # Fields for the Product model
    name = models.CharField(max_length=255, help_text="Enter the name of the product")
    description = models.TextField(help_text="Enter a detailed description of the product")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the price of the product")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when the product was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time when the product was last updated")

    # Optional fields
    image = models.ImageField(upload_to="product_images/", null=True, blank=True, help_text="Upload an image of the product")

    def __str__(self):
        """
        String representation of the model instance.
        """
        return self.name
