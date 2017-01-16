from django.db import models

class UploadedFiles(models.Model):
    data_file = models.FileField(upload_to='excel_data_file')
    def __str__(self):
            return self.data_file

class Guests(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date registered')
    email = models.CharField(max_length=200)

    def __str__(self):
            return self.name

class ImportedData(models.Model):
    CODIGO = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=200, blank=True,null=True)
    SUBRUBRO = models.CharField(max_length=200, blank=True,null=True)
    RUBRO = models.CharField(max_length=200, blank=True,null=True)
    MARCA_P = models.CharField(max_length=200, blank=True,null=True)
    EDAD = models.CharField(max_length=200, blank=True,null=True)
    CONSIDER = models.CharField(max_length=200, blank=True,null=True)
    GRUPO = models.CharField(max_length=200, blank=True,null=True)
    PESO = models.FloatField(blank=True,null=True)
    MATERIAL = models.CharField(max_length=200, blank=True,null=True)
    TIPO_P = models.CharField(max_length=200, blank=True,null=True)
    USO = models.CharField(max_length=200, blank=True,null=True)
    TAMANO = models.CharField(max_length=200, blank=True,null=True)
    URLFOTO1 = models.CharField(max_length=200, blank=True,null=True)
    URLFOTO2 = models.CharField(max_length=200, blank=True,null=True)
    URLFOTO3 = models.CharField(max_length=200, blank=True,null=True)
    PRECIO = models.FloatField(blank=True,null=True)
    STOCK = models.IntegerField(blank=True,null=True)
    LISTAPRE = models.CharField(max_length=200, blank=True,null=True)
    TITUMELI = models.CharField(max_length=200, blank=True,null=True)
    GRUPO_RECA = models.CharField(max_length=200, blank=True,null=True)
    DESC_LAR = models.CharField(max_length=200, blank=True,null=True)
