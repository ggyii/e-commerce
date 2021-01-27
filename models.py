from django.db import models
# Create your models here.
class Product(models.Model):
  product_id = models.AutoField
  product_name = models.CharField(max_length=50)
  product_price = models.IntegerField(default="")
  product_retail = models.IntegerField()
  product_cat = models.CharField(max_length=120,default="")
  product_sdisc = models.CharField(max_length=200)
  product_img1 = models.ImageField(default="")
  product_img2 = models.ImageField(default="/")
  product_img3 = models.ImageField(default="/")
  desc = models.CharField(max_length=800)
  pub_date = models.DateField()
  def __str__(self):
    return self.product_name