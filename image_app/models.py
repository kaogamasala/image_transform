from django.db import models
from django.contrib.auth.models import User

CHOICE = (
	('', '変換方法を選んでください'),
    ('グレースケール', 'グレースケール'),
    ('モザイク', 'モザイク'),
    ('フェイスモザイク', 'フェイスモザイク'),
    ('モザイクgif', 'モザイクgif'),
)
class Document(models.Model):
	description = models.CharField('画像変換方法', max_length=255, choices=CHOICE)
	photo = models.ImageField('画像選択', upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	output = models.ImageField(default = 'output/output.jpg')
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.description