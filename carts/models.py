# 
# Django中models.py的作用是定义数据模型。
# 
# 在Django中，models.py文件是一个Python模块，它包含了应用程序所需的所有数据库表和字段。
# 通过定义数据模型，我们可以创建、读取、更新和删除数据库记录。
# 每个模型类都对应着一个数据库表，并且每个属性都对应着该表中的一列。
# 在这些属性中，我们可以指定其类型（例如CharField或IntegerField），以及其他选项（例如最大长度或是否允许为空）。
# 此外，在models.py文件中还可以定义与其他模型之间的关系（例如ForeignKey或ManyToManyField），从而构建复杂的数据结构。
# 当我们修改了models.py文件后，需要运行migrations来同步数据库结构
from django.db import models

# Create your models here.

from store.models import Product

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity
    
    def str(self):
        return self.product