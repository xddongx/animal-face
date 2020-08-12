from django.db import models

class Face(models.Model):
    face = models.CharField(max_length=30)
    content = models.TextField()
    artist = models.TextField()

    def __str__(self):
        return '{}'.format(self.face)

class FaceHist(models.Model):
    GENDER_CHOICES =( 
        ("남자", "남자"), 
        ("여자", "여자")
    ) 

    AGE_CHOICES =(
        ('10대', '10대'),
        ('20대', '20대'),
        ('30대', '30대'),
        ('40대 이상', '40대 이상'),
    )
    age = models.CharField(max_length=15, choices=AGE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='face/%Y/%m')
    message = models.TextField(blank=True, null=True)
    face = models.ForeignKey(Face, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{} : {}'.format(self.face, self.message)

    def get_absolute_url(self):
        return '/face/facehist/{}/'.format(self.pk)
