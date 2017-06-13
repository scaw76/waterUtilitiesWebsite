from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class Notice(models.Model):
	title_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	description_text = models.TextField()

	def __str__(self):
		return self.title_text

@python_2_unicode_compatible  # only if you need to support Python 2
class NoticeFile(models.Model):
	notice_key = models.ForeignKey(Notice, on_delete=models.CASCADE)
	title_text = models.CharField(max_length= 200)
	file_upload = models.FileField(null=True, blank=True)

	def __str__(self):
		return self.title_text