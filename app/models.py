from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length = 50, default="firma")
    contactname = models.CharField(max_length = 50, default="firma")
    address = models.CharField(max_length = 100, default="firma")
    phone = models.CharField(max_length = 20, default="firma")
    email = models.CharField(max_length = 50, default="firma")
    country = models.CharField(max_length = 50, default="firma")
    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.companyname} from {self.country}"


class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "laku")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default = 3)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
     # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa hienommin,
     # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.productname} produced by {self.supplier.companyname}"
    
class Customers(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 40)
    country = models.CharField(max_length = 20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    orderdate = models.DateTimeField(auto_now_add=True)
    shipper = models.CharField(max_length = 20)
    shipping_address = models.CharField(max_length = 40)
    shipping_country = models.CharField(max_length = 20)
    
    @property
    def customer_full_name(self):
        return f"{self.customer.first_name} {self.customer.last_name}"

    def __str__(self):
        return f"Order {self.id} for {self.customer_full_name} on {self.order_date}"