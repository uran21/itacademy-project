from django.db import models
class Theme(models.Model):

	title = models.CharField(max_length=128)
	color = models.CharField(max_length=8)
	image = models.ImageField(upload_to='uploads/')
	
	def __str__(self):
		return self.title
	
class Post(models.Model):
	title = models.CharField(max_length=128)
	content = models.TextField()
	add_time = models.DateTimeField(auto_now_add=True)
	theme=models.ForeignKey(
		Theme, 
		on_delete=models.CASCADE,
		null=True
	)
	
	def __str__(self):
		return self.title