from django.db import models

# Create your models here.
class Article(models.Model) :
	title = models.CharField(max_length = 100)#博客题目
	category =models.CharField(max_length = 50,blank = True) #博客标签
	date_time = models.DateTimeField(auto_now_add = True) # 博客日期
	content = models.TextField(blank = True, null = True) # 正文
	# def __init__(self, arg):
	# 	super(Article, self).__init__()
	# 	self.arg = arg

	def __str__(self) :
		return self.title

	class Meta:
		ordering = ['-date_time']
