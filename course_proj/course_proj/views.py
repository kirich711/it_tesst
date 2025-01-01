from django.shortcuts import render
import itertools
from course_proj.tools import hh_vac
from .models import StatisticYear, StatisticYearOnlyVac, StatisticCitySalary, StatisticCityPercent, StatisticCityPercentOnlyVac, StatisticCitySalaryOnlyVac, StatisticSkillsByYear, StatisticSkillsByYearOnlyVac

def main_page(request):
    return render(request, "index.html")

def relevance_page(request):
    data_statyear = StatisticYear.objects.all().values()
    data_statyearvac = StatisticYearOnlyVac.objects.all().values()
    return render(request, "relevance.html",
{
            'data_statyear': data_statyear,
            'data_statyearvac': data_statyearvac
        })

def area_page(request):
    data_statcity_salary = StatisticCitySalary.objects.all().values()
    data_statcity_percent = StatisticCityPercent.objects.all().values()
    data_statcity_salary_vac = StatisticCitySalaryOnlyVac.objects.all().values()
    data_statcity_percent_vac = StatisticCityPercentOnlyVac.objects.all().values()
    return render(request, "area.html",
                  {
                      'data_statcity_salary': data_statcity_salary,
                      'data_statcity_percent': data_statcity_percent,
                      'data_statcity_salary_vac':data_statcity_salary_vac,
                      'data_statcity_percent_vac':data_statcity_percent_vac
                  })

def skill_page(request):
    data_statskill = StatisticSkillsByYear.objects.all().values()
    data_statskill_vac = StatisticSkillsByYearOnlyVac.objects.all().values()

    data_statskill_grouped = itertools.groupby(data_statskill, key=lambda x: x['year'])
    data_statskill_vac_grouped = itertools.groupby(data_statskill_vac, key=lambda x: x['year'])
    grouped_lists = {}
    grouped_lists_vac = {}

    for year, group in data_statskill_grouped:
        grouped_lists[year] = list(group)

    for year, group in data_statskill_vac_grouped:
        grouped_lists_vac[year] = list(group)

    return render(request, "skills.html",
                  {
                      'data_statskill': grouped_lists,
                      'data_statskill_vac': grouped_lists_vac
                  })

def vac_page(request):
    data_vac = hh_vac.get_top20_vac()
    #data_vac = []
    return render(request, "vacancies.html",{'data_vac': data_vac})