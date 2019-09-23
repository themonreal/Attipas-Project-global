from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit

class Size(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('size_detail',kwargs={'size_slug':self.slug})
def pre_save_size_slug(sender,instance, *args,**kwargs):
    if not instance.slug:
         slug = slugify(translit(str(instance.name), reversed=True))
         instance.slug=slug
pre_save.connect(pre_save_size_slug, sender=Size)


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)

class ProductManager(models.Manager):

    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(avaible=True)


class Product(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    avaible = models.BooleanField(default=True)
    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse('product_detail',kwargs={'product_slug':self.slug})
