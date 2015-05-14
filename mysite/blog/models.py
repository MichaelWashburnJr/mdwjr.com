from django.db import models

class Tag(models.Model):
	"""
	A category of a post.  This could be a project, tutorial,
	review, or a keyword like django, c++, etc.
	"""
	name = models.CharField(max_length=20, db_index=True)
	slug = models.CharField(max_length=20, db_index=True)

	def __str__(self):
		return self.name

	def get_all():
		return Tag.objects.all().order_by('name')

	def get_tags_in_posts(post_queryset):
		"""
		Return all tags found in a query set of posts
		"""
		return Tag.objects.filter(posts__in=post_queryset)


class Post(models.Model):
	"""
	A blog post which should support rich text
	"""
	is_active = models.BooleanField(default=True)
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	style = models.TextField(blank=True)
	posted= models.DateField(db_index=True)
	last_modified = models.DateField(db_index=True, auto_now=True)
	tags = models.ManyToManyField(Tag, related_name='posts')

	def __str__(self):
		return self.title

	def is_project(self):
		return (len(self.tags.filter(slug='project')) != 0)

	def get_all():
		"""
		Return all active posts.
		"""
		return Post.objects.filter(is_active=True).order_by('-posted')

	def get_projects():
		"""
		return all active project posts.
		"""
		return Post.objects.filter(is_active=True, tags__slug='project').order_by('-posted')

	def get_blog_posts():
		"""
		Retyrb all active blog posts.
		"""
		return Post.objects.filter(is_active=True).exclude(tags__slug='project').order_by('-posted')

	def tags_to_str(self):
		"""
		Return a space separated string of tags.
		"""
		string = ""
		for tag in self.tags.all():
			string += tag.slug + " "
		return string