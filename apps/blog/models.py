from django.db import models

class Category(models.Model):
  id = models.AutoField(primary_key = True)
  name = models.CharField("Name of category", max_length = 100, null = False, blank = False)
  state = models.BooleanField("Category Activate/ Category Deactivate", default = True)
  date_creation = models.DateField("Date of creation", auto_now = False, auto_now_add = True)

  class Meta:
    verbose_name = "Category"
    verbose_name_plural = "Categories"

  def __str__(self):
    return self.name 

class Author(models.Model):
  id = models.AutoField(primary_key = True)
  names = models.CharField("Author's names", max_length = 250, null = False, blank = False)
  surnames = models.CharField("Author's surnames", max_length = 250, null = False, blank = False)
  facebook = models.URLField("Facebook", null = True, blank = True)
  twitter = models.URLField("Twitter", null = True, blank = True)
  instagram = models.URLField("Instagram", null = True, blank = True)
  web = models.URLField("Web", null = True, blank = True)
  mail = models.EmailField("E-Mail", null = False, blank = False)
  state = models.BooleanField("Author Activate/ Author Deactivate", default = True)
  date_creation = models.DateField("Date of creation", auto_now = False, auto_now_add = True)

  class Meta:
    verbose_name = "Category"
    verbose_name_plural = "Categories"

  def __str__(self):
    return "{0},{1}".format(self.surnames, self.names)