from django.db import models



class ImportFile(models.Model):
    file = models.FileField(upload_to='imports')
    
class ImportRecord(models.Model):
    import_file = models.ForeignKey(ImportFile, on_delete=models.CASCADE)  
    item_code = models.CharField(max_length=100)
    legacy_data = models.TextField()
    noun = models.CharField(max_length=100)
    modifier = models.CharField(max_length=100)
    physical_verification = models.BooleanField()