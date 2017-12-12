# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
from django.db import models

# Create your models here.
class Zipcode(models.Model):
	zipcode = models.IntegerField(max_length = 5)
	city = models.CharField(max_length = 45)
	State = models.CharField(max_length = 2)
	country = models.CharField(max_length = 50, blank = True)

	def __unicode__(self):
		return (u'id = %d, zipcode = %s') %(self.id, self.zipcode)

	class Meta:
		ordering = ['id']

class Student(models.Model):
	zipcode = models.ForeignKey(Zipcode, on_delete = models.CASCADE)
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	age = models.IntegerField(max_length = 3)
	email = models.EmailField()
	gender = models.CharField(max_length = 1)
	phone = models.CharField(max_length = 12)
	address = models.CharField(max_length = 50)

	def __unicode__(self):
		return (u'firstname = %s') % self.first_name

	class Meta:
		ordering = ['id']

class Payment_Method(models.Model):
	card_number = models.IntegerField(max_length = 12)
	payment_type = models.CharField(max_length = 10)
	expired_date = models.DateField()

	def __unicode__(self):
		return (self.payment_type)

	class Meta:
		ordering = ['id']

class Order(models.Model):
	ord_placed_date = models.DateField()
	ord_paid_date = models.DateField()
	student_id = models.ForeignKey(Student,on_delete = models.CASCADE)
	payment_id = models.ForeignKey(Payment_Method,on_delete = models.CASCADE)

	class Meta:
		ordering = ['id']

class Instructor(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	age = models.IntegerField(max_length = 3)
	email = models.EmailField()
	gender = models.CharField(max_length = 1)
	phone = models.CharField(max_length = 12)

	def __unicode__(self):
		return (u'firstname = %s') % self.first_name

	class Meta:
		ordering = ['id']

class Course(models.Model):
	instructor_id = models.ForeignKey(Instructor, on_delete = models.CASCADE)
	course_name = models.CharField(max_length = 30)
	price = models.FloatField(max_length = 5)
	start_date = models.DateField()
	end_date = models.DateField()
	time = models.TimeField()
	description = models.TextField(max_length = 100)

	def __unicode__(self):
		return (u'coursename = %s') % self.course_name

	class Meta:
		ordering = ['id']

class Order_items(models.Model):
	course_id = models.ForeignKey(Course,on_delete = models.CASCADE)
	order_id = models.ForeignKey(Order,on_delete = models.CASCADE)
	quantity = models.IntegerField(default = 1)

	class Meta:
		ordering = ['id']



