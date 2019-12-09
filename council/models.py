from django.db import models
from django.utils import timezone
from PIL import Image

class Council(models.Model):
	council_number = models.CharField(max_length=200)

	def __str__(self):
		return self.council_number

class CouncilName(models.Model):
	council_name = models.CharField(max_length=200)
	council_number = models.ForeignKey(Council, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.council_name

class  Profile(models.Model):
	ASSOCIATE = 'A'
	INSURANCE = 'I'
	INACTIVE = 'N'
	Membership_Type = (
		(ASSOCIATE, 'Associate'),
		(INSURANCE, 'Insurance'),
		(INACTIVE, 'Inactive'),
	)
	Membership_Class = (
		('H', ('H. Honorary')),
		('L', ('L. Honorary Life')),
	)
	membership_number = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	street_address = models.CharField(max_length=100)
	City_state_zip = models.CharField(max_length=100)
	first_degree_date = models.DateTimeField(blank=True, null=True)
	second_degree_date = models.DateTimeField(blank=True, null=True)
	third_degree_date = models.DateTimeField(blank=True, null=True)
	reentry_date = models.DateTimeField(blank=True, null=True)
	birth_date = models.DateTimeField(blank=True, null=True)
	membership_type = models.CharField('Membership Type', max_length=1, choices=Membership_Type, default=ASSOCIATE)
	membership_class = models.CharField('Membership Class', max_length=1, choices=Membership_Class, blank=True,)
	assembly_number = models.CharField(max_length=100, blank=True, null=True)
	council_number = models.ForeignKey(Council, on_delete=models.CASCADE, blank=True, null=True)
	council_name = models.ForeignKey(CouncilName, on_delete=models.CASCADE, blank=True, null=True)
	email = models.EmailField()
	phone = models.CharField(max_length=50, blank=True, null=True)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.membership_number} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)


		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class Position(models.Model):
	position = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.position

class OfficersTerm(models.Model):
	colbn_year = models.CharField(max_length=100)
	council_number = models.ForeignKey(Council, on_delete=models.CASCADE, blank=True, null=True)
	position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)
	membership_number = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
	name = models.CharField(max_length=250)
	installed_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

	def __str__(self):
		return self.position

