from django.db import models
from .category import Category
from .owner import Owner

# Create your models here.


class Asset(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=200)

    value = models.DecimalField(max_digits=19, decimal_places=2)
    acquisition_date = models.DateField()
    category = models.ManyToManyField(Category, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
