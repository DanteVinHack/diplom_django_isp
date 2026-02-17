from django.db import models


# Create your models here.
class Passport(models.Model):
    serial = models.CharField(max_length=10)
    number = models.CharField(max_length=20)
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    date_issue = models.DateField(verbose_name="Дата выдачи")

    class Meta:
        verbose_name = ("Паспорт")
        verbose_name_plural = ("Паспорта")

    def __str__(self):
        return self.serial + " " + self.number


class Position(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = ("Должности")
        verbose_name_plural = ("Должности")

    def __str__(self):
        return self.name

class Worker(models.Model):
    fio = models.CharField(max_length=150)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    passport_id = models.ForeignKey(Passport, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Position, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("Работник")
        verbose_name_plural = ("Работники")

    def __str__(self):
        return self.login
