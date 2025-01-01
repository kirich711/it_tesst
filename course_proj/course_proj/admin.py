from django.contrib import admin

from .models import StatisticYear, StatisticYearOnlyVac, StatisticCitySalary, StatisticCitySalaryOnlyVac, StatisticCityPercent, StatisticCityPercentOnlyVac, StatisticSkillsByYear, StatisticSkillsByYearOnlyVac

admin.site.register(StatisticYear)
admin.site.register(StatisticYearOnlyVac)
admin.site.register(StatisticCitySalary)
admin.site.register(StatisticCitySalaryOnlyVac)
admin.site.register(StatisticCityPercent)
admin.site.register(StatisticCityPercentOnlyVac)
admin.site.register(StatisticSkillsByYear)
admin.site.register(StatisticSkillsByYearOnlyVac)