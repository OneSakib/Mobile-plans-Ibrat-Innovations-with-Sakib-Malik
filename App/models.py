from django.db import models

# Create your models here.
PLAN_TYPE = (
    ('Popular', 'Popular'),
    ('Unlimited', 'Unlimited'),
    ('Data', 'Data'),
    ('Cricket', 'Cricket'),
    ('Combo', 'Combo'),
    ('Talktime', 'Talktime'),

)
CIRCLE = (
    ('ALL Circle', 'ALl Circle'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar/Jharkhand', 'Bihar/Jharkhand'),
    ('Chennai', 'Chennai'),
    ('Delhi NCR', 'Delhi NCR'),
    ('Goa', 'Goa'),
    ('Gujrat', 'Gujrat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu Kashmir', 'Jammu Kashmir'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Kolkata', 'Kolkata'),
    ('Madhya Pradesh/Chhattisgarh', 'Madhya Pradesh/Chhattisgarh'),
    ('Maharashtra', 'Maharashtra'),
    ('Mumbai', 'Mumbai'),
    ('North East', 'North East'),
    ('Orissa', 'Orissa'),
    ('Punjab', 'Punjab'),
    ('Rajashtan', 'Rajashtan'),
    ('Tamilnadu', 'Tamilnadu'),
    ('Telengana', 'Telengana'),
    ('UP East', 'UP East'),
    ('UP West', 'UP West'),
    ('Uttrakhand', 'Uttrakhand'),
    ('West Bengal', 'West Bengal'),

)


class PrepaidPlans(models.Model):
    plans_type = models.CharField(choices=PLAN_TYPE, max_length=100)
    circle = models.CharField(choices=CIRCLE, max_length=100)
    data = models.CharField(default="NA", max_length=100)
    validity = models.CharField(default="NA", max_length=20)
    desc = models.CharField(default="NA", max_length=300)
    price = models.CharField(default='NA', max_length=20)

    class Meta:
        abstract = True


class Airtel(PrepaidPlans):
    def __str__(self):
        return "Airtel"

    class Meta:
        verbose_name_plural = 'Airtel'


class Vodafone(PrepaidPlans):

    def __str__(self):
        return "Vodafone"

    class Meta:
        verbose_name_plural = 'Vodafone'


class BSNL(PrepaidPlans):
    def __str__(self):
        return "BSNL"

    class Meta:
        verbose_name_plural = 'BSNL'


class JIO(PrepaidPlans):
    def __str__(self):
        return "JIO"

    class Meta:
        verbose_name_plural = 'JIO'


class MTNL(PrepaidPlans):
    def __str__(self):
        return "MTNL"

    class Meta:
        verbose_name_plural = 'MTNL'
