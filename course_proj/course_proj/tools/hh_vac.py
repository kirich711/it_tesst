import requests
from datetime import datetime
import re

en_ru_money = {
    "AZN": "Манаты",
    "BYR": "Белорусские рубли",
    "EUR": "Евро",
    "GEL": "Грузинский лари",
    "KGS": "Киргизский сом",
    "KZT": "Тенге",
    "RUR": "Рубли",
    "UAH": "Гривны",
    "USD": "Доллары",
    "UZS": "Узбекский сум"
}


def __clearString(_string):
    string = str(_string)
    pattern = re.compile('<.*?>')
    string = re.sub(pattern, '', string)

    return string


def __split_key_skills(lst):
    if len(lst) == 0:
        return "Нет"
    skills = []
    for value in lst:
        skills.append(value["name"])
    result = ', '.join(skills)
    return result


def __change_gross(gross):
    if gross == None:
        return ""
    if (gross == True):
        return "(до вычета налогов)"
    return "(после вычета налогов)"


def __change_currency(curr):
    if curr == None:
        return ""
    if curr not in en_ru_money.keys():
        return curr
    return en_ru_money[curr]

def __format_salary(salary):
    if salary == 0 or salary == "None" or salary == "0" or salary == None:
        return None
    else:
        return salary

def __get_salary(salary_from, salary_to, curr, gross):
    gross = __change_gross(gross)
    curr = __change_currency(curr)
    salary_from = __format_salary(salary_from)
    salary_to = __format_salary(salary_to)
    salary = ""
    if salary_from is None and salary_to is None :
        if curr == "" and gross == "":
            salary = "Неизвестно"
        else:
            salary = f" {curr} {gross}"
    elif salary_from is None or salary_to is None:
        if salary_from is None:
            salary = f"{salary_to} {curr} {gross}"
        elif salary_to is None:
            salary = f"{salary_from} {curr} {gross}"
        else:
            salary = "Неизвестно"
    else:
        salary = f"{salary_from} - {salary_to} {curr} {gross}"
    return salary


def __fromat_date(str_date):
    date_obj = datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S%z")
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date


def __get_vacancy_description_and_skills(vacancy_id):
    url = f"https://api.hh.ru/vacancies/{vacancy_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        description = data.get("description", "")
        key_skills = data.get("key_skills", [])
        return description, key_skills
    else:
        return "", []


def __get_vacancy(vacancy):
    vacancy_id = vacancy.get("id")
    vacancy_title = vacancy.get("name")
    vacancy_url = vacancy.get("alternate_url")
    company_name = vacancy.get("employer", {}).get("name")
    region_name = vacancy.get("area", {}).get("name")
    published_at = vacancy.get("published_at")

    salary_info = vacancy.get("salary", {})
    if salary_info:
        salary_from = salary_info.get("from", 0)
        salary_to = salary_info.get("to", 0)
        currency = salary_info.get("currency")
        gross = salary_info.get("gross")

    else:
        salary_from = salary_to = 0
        currency = gross = None
    return {
        "id": vacancy_id,
        "url": vacancy_url,
        "name": vacancy_title,
        "company": company_name,
        "salary": __get_salary(salary_from, salary_to, currency, gross),
        "area": region_name,
        "date": __fromat_date(published_at)
    }


def get_top20_vac():
    keywords = ['backend', 'бэкэнд', 'бэкенд', 'бекенд', 'бекэнд', 'back end', 'бэк энд', 'бэк енд', 'django', 'flask', 'laravel', 'yii', 'symfony']
    url = "https://api.hh.ru/vacancies"
    today = datetime.now().replace(hour=0, minute=0, second=0)
    params = {
        "text": f"name:(({' OR '.join(keywords)}) AND (Разработчик OR Программист)) AND description:(({' OR '.join(keywords)}) AND NOT JavaScript)",
        "date_from": today.isoformat(),
        "per_page": 5,
        "order_by": "publication_time"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])

        vacancy_list = []

        for vacancy in vacancies:
            vacancy = __get_vacancy(vacancy)

            vacancy_id = vacancy.get("id")
            description, key_skills = __get_vacancy_description_and_skills(vacancy_id)
            
            if __clearString(description)[200] == ' ':
                __clearString(description)[200] == ''

            vacancy["description"] = __clearString(description)[:200] + "..."
            vacancy["key_skills"] = __split_key_skills(key_skills)

            vacancy_list.append(vacancy)

        return vacancy_list

    else:
        return []
