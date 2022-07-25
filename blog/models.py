from asyncio.windows_events import NULL
from datetime import date
from platform import mac_ver
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
# from embed_video.fields  import  EmbedVideoField
from embed_video.fields import EmbedVideoField


class PostManager(models.Manager):
	def like_toggle(self, user, post_obj):
		if user in post_obj.liked.all():
			is_liked = False
			post_obj.liked.remove(user)
		else:
			is_liked = True
			post_obj.liked.add(user)
		return is_liked

POST_CHOICES = (
	('Show','Show'),
	('Event','Event'),
	('Talent','Talent'),
	('Rent','Rent'),
	('Contact','Contact'),
	('Post','Post')

)

TALENT_CHOICES = (
('Actor','Actor'),
('Actress','Actress'),
('Director','Director'),
('Associate Director','Associate Director'),
('Assistant Director','Assistant Director'),
('Child Artist','Child Artist'),
('Dubbing Artist','Dubbing Artist'),
('Script Writer','Script Writer'),
('Storyboard Artist','Storyboard Artist'),
('Executive Producer','Executive Producer'),
('Location','Location manager'),
('Production manager','Production Manager'),
('Art Director','Art Director'),
('Lightman','Lightman'),
('Makeup','Makeup'),
('Stunt','Stunt'),
('Editor','Editor'),
('Dubbing Engineer','Dubbing Engineer'),
('Sound Engineer','Sound Engineer'),
('Music Director','Music Director'),
('Sound Mixing','Sound Mixing'),
('Colorist','Colorist'),
('Pubicity Design','Pubicity Design'),
('Others','Others')
)


CONTACT_CHOICES=(
	('Contact Name','Contact Name'),
	('Company','Company')
)

SHOW_CHOICES=(
	('Short Film','Short Film'),
	('Feature Film','Feature Film'),
	('Documentory','Documentory'),
	('Series','Series')


)

LANGUAGE_CHOICES=(
	('TAMIL','TAMIL'),
	('TELEGU','TELEGU'),
	('MALAYALAM','MALAYALAM'),
	('ENGLISH','ENGLISH')



)
GENRE_CHOICES=(
	('DRAMA','DRAMA'),
	('THRLLER','THRILLER'),
	('ROMANCE','ROMANCE'),
	('SCI-FI','SCI-FI')
)

RENT_CHOICES=(
	('Location','Location'),
	('Equipment','Equipment')



)
CURRENCY_CHOICES=(

('USD','USD'),
('INR','INR'),
('EUR','EUR'),
('OTHERS','OTHERS')



)

class Post(models.Model):
    

    ##common
    
	form_choice = models.CharField(max_length=2, blank=2)
	location=models.CharField(max_length=50,blank=True)
	description=models.TextField(blank=True)
	tags=models.CharField(max_length=50,blank=True)
	img = models.ImageField(upload_to='post/', blank=True)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=NULL)

    

	##Event
	From=models.DateTimeField(blank=True,null=True)
	to=models.DateTimeField(blank=True,null=True)
	##Talent
	talent=models.CharField(max_length=50,choices=TALENT_CHOICES)
	language=models.CharField(max_length=50,blank=True)
	##Contact
	contact_type=models.CharField(max_length=100, choices=CONTACT_CHOICES)
	phone_number=models.CharField(max_length=20,blank=True)
	email_id=models.CharField(max_length=100,blank=True)
	##show
	show=models.CharField(max_length=100, choices=SHOW_CHOICES)
    
	video_link = EmbedVideoField(blank=True)
	show_language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES)
	genre=models.CharField(max_length=100,choices=GENRE_CHOICES,default=NULL)
	##rent
	rent_option=models.CharField(max_length=100,choices=RENT_CHOICES,)
	name=models.CharField(max_length=30,blank=True)
	currency=models.CharField(max_length=20,choices=CURRENCY_CHOICES)
	price_per_day=models.CharField(max_length=20,blank=True,default=NULL)

	
	title = models.CharField(max_length=100,blank=True)

	
	liked = models.ManyToManyField(
		settings.AUTH_USER_MODEL, blank=True, related_name='liked')
	date_posted = models.DateTimeField(default=timezone.now)
	

	objects = PostManager()

	class Meta:
		ordering = ('-date_posted', )

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
	post = models.ForeignKey(
		Post, related_name='comments', on_delete=models.CASCADE)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text = models.TextField()
	
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=True)

	def approve(self):
		self.approved_comment = True
		self.save()

	def get_absolute_url(self):
		return reverse("post_list")

	# def __str__(self):
	#     return self.author
