from django.db import models

# Create your models here.

class calls(models.Model):
    call_id = models.AutoField(primary_key=True)
    call_tag = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.call_tag


class callStatus(models.Model):
    call_type_choices = (
        ('1', u'Welcome Call'),
        ('2', u'Winback Call'),
        ('3', u'Experince Call'),
    )

    call_status_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32, choices=call_type_choices, null=True, blank=True)
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    additional_tag_required = models.BooleanField(default=True)



    def __str__(self):
        return self.title