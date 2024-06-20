from django.db import models

# Create your models here.
class Emp(models.Model):
    first_name=models.CharField(max_length=30,verbose_name="enter ur first name",help_text="anu")
    last_name=models.CharField(max_length=30,verbose_name="enter ur last name")
    email=models.EmailField(max_length=30)
    class Meta:
        db_table="tbl_emp"

class Tech(models.Model):
    first_name=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='images/')

# class (models.Model):
#     first_name=models.CharField(max_length=30,verbose_name="enter ur first name",help_text="anu")
#     last_name=models.CharField(max_length=30,verbose_name="enter ur last name")
#     age=models.IntegerField(max_length=30)
#     email=models.EmailField(max_length=30)
#     class Meta:
#         db_table="tbl_stu"

class State(models.Model):
    state_name=models.CharField(verbose_name='state',max_length=50)
    district=models.ForeignKey(verbose_name='dist',max_length=50)
    class Meta:
        db_table="tbl_state"
class District(models.Model):
    district=models.CharField(verbose_name='dist',max_length=50)
    class Meta:
        db_table="tbl_dist"

