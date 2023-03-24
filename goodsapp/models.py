from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=10)

    def __unicode__(self):
        return u'<Category:%s>'%self.cname

class Goods(models.Model):
    gname = models.CharField(max_length=100, unique=True)
    gdesc = models.CharField(max_length=100)
    oldprice = models.DecimalField(max_digits=5,decimal_places=2)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return u'<Goods:%s>' % self.gname

class GoodsDetailName(models.Model):
    gdname = models.CharField(max_length=30)


class GoodDetail(models.Model):
    gdurl = models.ImageField(upload_to='')
    goodsdname = models.ForeignKey(GoodsDetailName)
    goods = models.ForeignKey(Goods)
