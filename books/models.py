from django.db import models
# Create your models here.
class Author(models.Model):
	AuthorID = models.CharField(max_length=20, primary_key=True)
	Name = models.CharField(max_length=20, unique=True)
	Age = models.IntegerField()
	Country = models.CharField(max_length=50)
	def __unicode__(self):
		return self.Name
	class Meta:
		ordering = ['Name']

class Book(models.Model):
    ISBN = models.CharField(max_length=20, primary_key=True)
    Title = models.CharField(max_length=20)
    AuthorID = models.ManyToManyField(Author, related_name="books")
    Publisher = models.CharField(max_length=20)
    PublishDate = models.DateField()
    Price = models.FloatField()
    def __unicode__(self):
        return self.Title
    class Meta:
        ordering = ['ISBN']

