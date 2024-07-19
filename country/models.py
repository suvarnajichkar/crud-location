
# Create your models here.
from django.db import models
import uuid

# Create your models here.
class Base(models.Model):
	is_active = models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now=True)
	created_date = models.DateTimeField(auto_now_add=True)
	uuid = models.UUIDField( default=uuid.uuid4, editable=False)
	
	

	class Meta:
		abstract=True

class Country(Base):
	name = models.CharField(max_length=10)
	slug = models.SlugField(unique=True)
	code = models.CharField(max_length=10,unique=True)
	flag = models.ImageField(upload_to = 'flag')
	is_state_available = models.BooleanField(default=True)
	
	
	def __str__(self):
		return self.name


class State(Base):
	Country = models.ForeignKey(to=Country,on_delete=models.CASCADE)
	statename=models.CharField(max_length=100)
	stateslug=models.SlugField(unique=True)
	language=models.CharField(max_length=100)
	population = models.IntegerField()

	def __str__(self):
		return self.statename

class City(Base):
	country = models.ForeignKey(to= Country, on_delete= models.CASCADE)
	state = models.ForeignKey(to=State, on_delete = models.SET_NULL,null=True)
	cityname=models.CharField(max_length=100)
	slug=models.SlugField(unique=True)

	def __str__(self):
		return self.cityname
	

	




