from django.db import models

class Face(models.Model):
    face = models.CharField(max_length=30)
    content = models.TextField()
    artist = models.TextField()

    def __str__(self):
        return '{}'.format(self.face)

class FaceHist(models.Model):
    GENDER_CHOICES =( 
        ("1", "남자"), 
        ("2", "여자")
    ) 

    AGE_CHOICES =(
        ('0', '0~9'),
        ('1', '10~19'),
        ('2', '20~29'),
        ('3', '30~39'),
        ('4', '40~'),
    )
    age = models.CharField(max_length=5, choices=GENDER_CHOICES)
    gender = models.CharField(max_length=10, choices=AGE_CHOICES)
    image = models.ImageField(upload_to='face/%Y/%m')
    message = models.TextField(blank=True, null=True)
    face = models.ForeignKey(Face, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{} : {}'.format(self.face, self.message)

    def get_absolute_url(self):
        return '/face/facehist/{}/'.format(self.pk)
