from django.db import models
from django.utils.text import slugify


class Phones(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=70, null=False)
    price = models.IntegerField(null=False)
    image = models.TextField(max_length=70, null=False)
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phones, self).save(*args, **kwargs)