from django.db import models


class Car(models.Model):
    manufacturer = models.ForeignKey(
        # 문자열 'Manufacturer'하는 이유
        #  - 클래스 순서 관계없이 설정 가능
        'Manufacturer',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ForeignkeyUser(models.Model):
    name = models.CharField(max_length=50)
    instructer = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='students',
        blank=True,
        null=True,
    )
