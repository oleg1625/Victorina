# Викторина "Женщины Великой Отечественной войны"

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green)](https://www.pygame.org/)
[![Open Source](https://img.shields.io/badge/Open_Source-Yes-0066CC)]()
[![License](https://img.shields.io/badge/License-MIT-FFD700)]()


Курсовая работа по дисциплине **"Информатика"** в ГБПОУ "Волгоградский технологический колледж".  
Интерактивная викторина с графическим интерфейсом, посвящённая вкладу женщин в победу в Великой Отечественной войне.
## 📌 Цель проекта
Разработка образовательного приложения на Python с использованием библиотеки Pygame для:
- Проверки знаний о роли женщин в Великой Отечественной войне
- Демонстрации навыков работы с графическим интерфейсом
- Реализации системы сохранения результатов (таблица лидеров)
## 🎮 Особенности
- **21 вопрос** с вариантами ответов
- **Система подсчёта очков** и таблица лидеров (топ-5)
- **Полноэкранный интерфейс** с фоновым изображением
- **Регистрация игрока** по имени перед стартом
- **Полупроницаемые overlay** для улучшения читаемости текста

## 🛠 Технологии
- **Python 3.8+**
- **Pygame 2.0** (для графического интерфейса)
- **TXT-файлы** (хранение результатов в `leaderboardfinal.txt`)

## 📁 Структура проекта
```plaintext
.
├── Victorina3.0.py        # Основной код программы
├── photo.jpg              # Фоновое изображение
└── leaderboardfinal.txt   # Файл с результатами (создаётся автоматически)
```
## 📸 Скриншоты
### **Регистрация:**
![Victorina1.png](https://www.ibb.org.ru/images/2025/04/02/Victorina1f1143a6927e6beab.png)

### **Игровой процесс:**
![Victorina2.png](https://www.ibb.org.ru/images/2025/04/02/Victorina22074a54d21059ff5.png)

### **Таблица лидеров:**
![Victorina3.png](https://www.ibb.org.ru/images/2025/04/02/Victorina3.png)

## 👥 Разработчики

- [oleg1625 SadDeadinsider](https://github.com/oleg1625) - Основной разработчик
- [VanlyCrazy](https://github.com/VanlyCrazy) - Дизайнер/Тестировщик

# 🛠 Установка и запуск

### Требования
- Python 3.8 или новее
- Библиотека Pygame 2.0+

### Пошаговая инструкция:

1. **Клонирование репозитория**  
   ```bash
   git clone https://github.com/Oleg1625/Victorina.git
   cd Victorina
   ```
2. **Установка Python**
   ```bash
   https://www.python.org/downloads/windows/
   ```
3. **Установка зависимостей**
   ```bash
   pip install pygame
   ```
4. **Запуск викторины**
   ```bash
   python Victorina3.0.py
   ```
# 📜 Лицензия
Этот проект использует [MIT License](https://github.com/oleg1625/Victorina/blob/main/LICENSE).