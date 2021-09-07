from django.db import models


# Create your models here.
class StudentInfo(models.Model):

    roll_no = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50, null=True)
    class_standard = models.CharField(max_length=30, null=True)
    school_name = models.CharField(max_length=60, null=True )
    mobile = models.CharField(max_length=30, null=True)
    Address = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class StudentAcademics(models.Model):
    roll_no = models.ForeignKey(StudentInfo, null=True, on_delete=models.CASCADE)
    maths = models.CharField(max_length=20, null=True)
    Physics = models.CharField(max_length=20, null=True)
    Chemistry = models.CharField(max_length=20, null=True)
    Biology = models.CharField(max_length=20, null=True)
    English = models.CharField(max_length=20, null=True)


