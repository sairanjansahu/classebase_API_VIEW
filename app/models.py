from django.db import models

# Create your models here.
class Product_category(models.Model):
    pcid=models.IntegerField()
    pcname=models.CharField(max_length=100)

    def __str__(self):
        return self.pcname

class Product(models.Model):
    pcname=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    pid=models.IntegerField()
    pname=models.CharField(max_length=100)
    pprice=models.IntegerField()
    pdate=models.DateField()

    def __str__(self):
        return self.pname