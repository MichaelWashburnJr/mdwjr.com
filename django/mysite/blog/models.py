from django.db import models

class Category(models.Model):
	"""
	A category of a post.  This could be a project, tutorial,
	review, etc.
	"""
	title = models.CharField(max_length=100, db_index=True)
	slug = models.CharField(max_length=100, db_index=True)

	def __str__(self):
		return self.title

class Post(models.Model):
	"""
	A blog post which should support rich text
	"""
	is_active = models.BooleanField(default=True)
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	style = models.TextField()
	posted= models.DateField(db_index=True, auto_now_add=True)
	last_modified = models.DateField(db_index=True, auto_now=True)
	category = models.ForeignKey(Category)

	def __str__(self):
		return self.title

