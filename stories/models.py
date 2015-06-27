from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
	user = models.ForeignKey(User, editable = False)
	time = models.DateTimeField(auto_now_add=True)

class Snippets(models.Model):
	TYPES = [("Video", "Video"),
			 ("Picture", "Picture"),
			 ("Text", "Text")]
	story = models.ForeignKey(Story)
	post_type = models.CharField(max_length=8, choices=TYPES, default='Text')
	attachment = models.TextField(null=True)
	content = models.TextField(null=True)
	time = models.DateTimeField(null=False)