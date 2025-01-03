from djongo import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        app_label = 'feedback'

    def __str__(self):
        return self.name
