from django.db import models


class StatisticYear(models.Model):
    year = models.IntegerField("Год")
    salary_avg = models.IntegerField("Средняя з/п")
    count = models.IntegerField("Количество вакансий")
    objects = models.Manager()
    class Meta:
        db_table = "stat_year"
    pass

class StatisticYearOnlyVac(models.Model):
    year = models.IntegerField("Год")
    salary_avg = models.IntegerField("Средняя з/п")
    count = models.IntegerField("Количество вакансий")
    objects = models.Manager()
    class Meta:
        db_table = "stat_year_only_vac"
    pass

class StatisticCitySalary(models.Model):
    city = models.CharField("Город", max_length=100)
    salary_avg = models.IntegerField("Средняя з/п")
    class Meta:
        db_table = "stat_city_salary"
    pass

class StatisticCitySalaryOnlyVac(models.Model):
    city = models.CharField("Город",max_length=100)
    salary_avg = models.IntegerField("Средняя з/п")
    class Meta:
        db_table = "stat_city_salary_only_vac"
    pass

class StatisticCityPercent(models.Model):
    city = models.CharField("Город",max_length=100)
    percent = models.FloatField("Процент вакансий")
    class Meta:
        db_table = "stat_city_percent"
    pass

class StatisticCityPercentOnlyVac(models.Model):
    city = models.CharField("Город",max_length=100)
    percent = models.FloatField("Процент вакансий")
    class Meta:
        db_table = "stat_city_percent_only_vac"
    pass

class StatisticSkillsByYearOnlyVac(models.Model):
    skill = models.CharField("Навык", max_length=100)
    number = models.IntegerField("Количество упоминаний")
    year = models.IntegerField("Год")

    class Meta:
        db_table = "stat_skill_by_year"
    pass

class StatisticSkillsByYear(models.Model):
    skill = models.CharField("Навык", max_length=100)
    number = models.IntegerField("Количество упоминаний")
    year = models.IntegerField("Год")

    class Meta:
        db_table = "stat_skill_by_year_only_vac"
    pass