from django.db import models

class Face(models.Model):
    face = models.CharField(max_length=30)
    content = models.TextField()
    artist = models.TextField()

    def __str__(self):
        return '{}'.format(self.face)

class FaceHist(models.Model):
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='face/%Y/%m')
    message = models.TextField()
    face = models.ForeignKey(Face, on_delete=models.CASCADE)

    def __str__(self):
        return '{} : {}'.format(self.face, self.message)
