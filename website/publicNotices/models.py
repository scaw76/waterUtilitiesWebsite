from django.db import models

class Notice(models.Model):
	title_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	description_text = models.TextField()

class NoticeFile(models.Model):
	notice_key = models.ForeignKey(Notice, on_delete=models.CASCADE)
	title_text = models.CharField(max_length= 200)
	file_upload = models.FileField(upload_to='uploads/')