import pandas as pd
import glob
import os

# Укажите путь к вашим CSV файлам
path = r'C:\Git\it_vacancy\years_to\\'  # Используйте 'r' для необработанной строки или двойные обратные слэши
all_files = glob.glob(os.path.join(path, "*.csv"))  # Получаем список всех CSV файлов в указанной директории

# Проверка наличия файлов
if not all_files:
    print("Не найдено файлов CSV в указанной директории.")
else:
    print(f"Найдено файлов: {len(all_files)}")

# Создаем пустой DataFrame для объединения
combined_df = pd.DataFrame()

# Цикл по всем файлам и их объединение
for filename in all_files:
    try:
        df = pd.read_csv(filename)  # Читаем файл
        print(f"Чтение файла: {filename}, количество строк: {len(df)}")  # Вывод количества строк
        if not df.empty:  # Проверка на пустоту DataFrame
            combined_df = pd.concat([combined_df, df], ignore_index=True)  # Объединяем с основным DataFrame
        else:
            print(f"Файл {filename} пуст.")
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")

# Сохраняем объединенный DataFrame в новый CSV файл, если он не пуст
if not combined_df.empty:
    combined_df.to_csv(os.path.join(path, 'combined_output.csv'), index=False)  # Замените на желаемое имя выходного файла
    print("Объединение завершено! Файл сохранен как 'combined_output.csv'.")
else:
    print("Объединенный файл пуст. Проверьте исходные файлы.")
