import pandas as pd

# Загрузка CSV файла
file_path = r'C:\Git\it_vacancy\years_to\2024.csv'  # Замените на путь к вашему CSV файлу
data = pd.read_csv(file_path)

# Заменяем NaN на пустые строки в столбцах name и key_skills
data['name'] = data['name'].fillna('')
data['key_skills'] = data['key_skills'].fillna('')

# Заменяем символы новой строки на запятые для корректного разделения навыков
data['key_skills'] = data['key_skills'].str.replace('\r\n', ', ')

# Создаем словарь для нормализации ключевых навыков
skill_mapping = {
    'backend': 'backend',
    'бэкэнд': 'backend',
    'бэкенд': 'backend',
    'бекенд': 'backend',
    'бекэнд': 'backend',
    'back end': 'backend',
    'бэк энд': 'backend',
    'бэк енд': 'backend',
    'django': 'django',
    'flask': 'flask',
    'laravel': 'laravel',
    'yii': 'yii',
    'symfony': 'symfony',
}

# Функция для нормализации навыков
def normalize_skills(skills):
    normalized_skills = []
    for skill in skills.split(','):
        skill = skill.strip().lower()  # Приводим к нижнему регистру и убираем пробелы
        normalized_skills.append(skill_mapping.get(skill, skill))  # Заменяем на нормализованный навык
    return ', '.join(normalized_skills)

# Применяем нормализацию к столбцу key_skills
data['key_skills'] = data['key_skills'].apply(normalize_skills)

# Заменяем NaN на 0 в столбце salary_average и преобразуем его в числовой тип
data['salary_average'] = pd.to_numeric(data['salary_average'], errors='coerce')

# Проверяем, есть ли данные
if not data.empty:
    # Рассчитываем среднюю зарплату и количество вакансий
    average_salary = data['salary_average'].mean()
    vacancy_count = data['name'].count()

    # Создаем результат в виде DataFrame
    result = pd.DataFrame({
        'average_salary': [average_salary],
        'vacancy_count': [vacancy_count]
    })

    # Вывод результатов
    print("Общая информация по вакансиям:")
    print(result)

    # Фильтруем вакансии, чтобы оставить только те, которые содержат указанные ключевые навыки
    relevant_skills = ['backend', 'django', 'flask', 'laravel', 'yii', 'symfony']
    filtered_data = data[data['key_skills'].str.contains('|'.join(relevant_skills), case=False)]

    # Обработка ключевых навыков для отфильтрованных данных
    if not filtered_data.empty:
        all_skills = filtered_data['key_skills'].str.cat(sep=', ')  # Объединяем все навыки в одну строку
        skills_list = [skill.strip() for skill in all_skills.split(',')]  # Разбиваем строку на список
        skills_series = pd.Series(skills_list)  # Преобразуем список в Series для подсчета частоты

        # Подсчитываем частоту каждого навыка и выбираем топ-20
        top_skills = skills_series.value_counts().head(20)

        # Выводим топ-20 ключевых навыков
        print("\nТоп-20 ключевых навыков:")
        print(top_skills)
    else:
        print("Нет вакансий с указанными ключевыми навыками.")
else:
    print("Нет вакансий в данных.")

