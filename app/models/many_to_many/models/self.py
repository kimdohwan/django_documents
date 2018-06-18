from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    # self의 역할
    #  - a가 b를 friends에 추가 -> b의 friends에도 a가 추가되어있음
    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name
