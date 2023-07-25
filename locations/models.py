from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point, LineString, Polygon

class LonLat(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()

    def __str__(self):
        return self.name

class Road(models.Model):
    name = models.CharField(max_length=100)
    path = models.LineStringField()

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    area = models.PolygonField()

    def __str__(self):
        return self.name