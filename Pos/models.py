from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Material(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Color(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name   
    
class StockProperty(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    num_of_rolls = models.IntegerField()
    size = models.DecimalField(max_digits=1000, decimal_places=2)  # Use DecimalField for precise decimal calculations
    extrasize = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)  # Use DecimalField for precise decimal calculations
    total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)  # Use DecimalField for total
    date_added = models.DateTimeField(auto_now_add=True)
    date_stocked = models.DateField()
    buying_price = models.IntegerField()
    
     
    
    def __str__(self):
        return f'{self.material.name} {self.color.name}'
    
    
    
class ProductSize(models.Model):
    size = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.size
    
  
class Product(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class ProductPro(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prod')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.product.name
    
class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField()
    gender = models.CharField(max_length=200)
    date_employed = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
    
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductPro, on_delete=models.CASCADE)
    mode_of_payment = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField()
    to_be_delivered_to = models.CharField(max_length=200, null=True, blank=True)
    no_to_be_delivered = models.IntegerField(null=True, blank=True)
    fully_payed = models.BooleanField(default=True)
    deposited = models.IntegerField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    delivered = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f'{self.customer.name} bought {self.product.product.name}'
   
    
    
class Expenses(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    expence_name = models.CharField(max_length=200)
    amount = models.IntegerField()
    date_issued = models.DateTimeField()
    reset = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.employee.first_name} {self.expence_name}'
    
    
    
    
class WorkInProgress(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    stock = models.ForeignKey(StockProperty,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_size = models.IntegerField(null=True, blank=True)
    size = models.DecimalField(max_digits=5, decimal_places=2) 
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    message = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    productQuantity = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.employee.first_name} is making {self.product_name}'
    
    
    # def save(self, *args, **kwargs):
    #     try:
    #         # Only update StockProperty if the size is provided
    #         if self.size is not None:
    #             remaining_meters = self.stock.size - self.size

    #             # Update the StockProperty
    #             self.stock.num_of_rolls -= 1  # Reduce the number of rolls by 1
    #             self.stock.total -= self.size  # Deduct the used size

    #             # Handle remaining meters
    #             if remaining_meters > 0:
    #                 # If there are remaining meters, update the StockProperty
    #                 self.stock.total -= remaining_meters
    #                 self.stock.size = self.stock.total / self.stock.num_of_rolls
    #             else:
    #                 # If the last roll is used up, set size to 0
    #                 self.stock.size = 0

    #             # Save the updated StockProperty
    #             self.stock.save()

    #         # Now you can update other fields like 'message'
    #         super().save(*args, **kwargs)
    #     except Exception as e:
    #         # Log the error
    #         print(f"Error in WorkInProgress save method: {str(e)}")