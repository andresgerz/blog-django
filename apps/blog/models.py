from django.db import models
from ckeditor.fields import RichTextField

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
    verbose_name = "Author"
    verbose_name_plural = "Authors"

  def __str__(self):
    return "{0},{1}".format(self.surnames, self.names)

class Post(models.Model):
  id = models.AutoField(primary_key = True)
  title = models.CharField("Title", max_length = 100, blank = False, null = False)
  slug = models.CharField("Slut", max_length = 100, blank = False, null = False)
  description = models.CharField("Description", max_length = 100, blank = False, null = False)
  container = RichTextField()
  image = models.URLField(max_length = 250, blank = False, null = False)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE) 
  state = models.BooleanField("Published/ Don't published", default = True)
  date_creation = models.DateField("Date of Creation", auto_now = False, auto_now_add = True)

  class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def __str__(self):
    return self.title  