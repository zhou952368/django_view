from django.db import models


# Create your models here.


class Movie(models.Model):
    fid = models.CharField(max_length=255)
    actor = models.CharField(max_length=255, blank=True, null=True)
    cata_log_name = models.CharField(max_length=255)
    cata_log_id = models.CharField(max_length=255, blank=True, null=True)
    evaluation = models.FloatField()
    image = models.CharField(max_length=255, blank=True, null=True)
    is_use = models.IntegerField()
    loc_name = models.CharField(max_length=255, blank=True, null=True)
    loc_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    on_decade = models.CharField(max_length=255, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sub_class_name = models.CharField(max_length=255, blank=True, null=True)
    sub_class_id = models.CharField(max_length=255, blank=True, null=True)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    is_vip = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'movie'


class Girl(models.Model):
    created_date = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    published = models.CharField(max_length=255)
    source = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=30)
    url = models.CharField(max_length=255)
    used = models.BooleanField(default=True)

    class Meta:
        db_table = 'girls'
