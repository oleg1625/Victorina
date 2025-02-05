import pygame
import sys

pygame.init()

# Настройка окна
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Викторина "Женщины Великой Отечественной войны"')

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)

# Шрифты
font1 = pygame.font.SysFont("Times New Roman", 24, bold=True)
font2 = pygame.font.SysFont("Times New Roman", 20)
font3 = pygame.font.SysFont("Times New Roman", 30, bold=True)


# Вопросы и ответы
class Question:
    def init(self, text, answers, correct):
        self.text = text
        self.answers = answers
        self.correct = correct


questions = [
    Question(
        "Кто из этих женщин совершила первый в истории ночной таран?",
        ["Людмила Павличенко", "Марина Раскова", "Екатерина Буданова", "Зоя Космодемьянская"],
        1
    ),
    Question(
        'Какая женщина-снайпер уничтожила 309 фашистов?',
        ["Мария Октябрьская", "Зинаида Туснолобова", "Людмила Павличенко", "Алия Молдагулова"],
        2
    ),
    Question(
        'Какое звание получила Людмила Павличенко?',
        ['Генерал-майор', 'Герой Советского Союза', 'Маршал Советского Союза'],
        1
    ),
    Question(
        'В каком городе находился знаменитый женский полк ночных бомбардировщиков?',
        ['Москва', 'Ленинград', 'Краснодар'],
        1
    ),
    Question(
        'Какое оружие чаще всего использовали женщины-снайперы?',
        ['Пулемёты', 'Винтовки', 'Гранатомёты'],
        1
    ),
    Question(
        'В каком году был сформирован 588-й ночной бомбардировочный авиационный полк (полк ночных ведьм)?',
        ['1942', '1943', '1944'],
        0
    ),
    Question(
        'Какая из этих женщин была известной партизанкой?',
        ['Зоя Космодемьянская', 'Валентина Терешкова', 'Мария Склодовская-Кюри'],
        0
    ),
    Question(
        'Где в основном работали женщины в тылу во время войны?',
        ['Только в магазинах', 'На заводах, в колхозах, в госпиталях', 'Только на фермах'],
        1
    ),
    Question(
        'Какую роль играли женщины-медики на фронте?',
        ['Только лечили раненых в тылу', 'Оказывали медицинскую помощь на передовой и в тылу', 'Не участвовали в боевых действиях'],
        1
    ),
    Question(
        'Какой из этих орденов часто присуждался женщинам за боевые заслуги?',
        ['Орден Андрея Первозванного', 'Орден Красной Звезды', 'Орден Святой Анны'],
        1
    ),
    Question(
        'Какие задачи выполняли женщины-разведчицы?',
        ['Только доставляли письма', 'Сбор разведывательных данных, диверсии', 'Не участвовали в разведывательных операциях',],
        1
    ),
    Question(
        'Как часто женщины участвовали в танковых боях?',
        ['Очень часто, как и мужчины', ' Редко, в основном в качестве механиков-водителей или связистов', 'Практически не участвовали'],
        2
    ),
    Question(
        'Что символизирует образ женщины-матери в контексте войны?',
        ['Силу и жестокость', 'Жертвенность и надежду', 'Равнодушие'],
        1
    ),
    Question(
        'Сколько женщин-летчиц было в составе 46-го гвардейского Таманского ночного бомбардировочного авиационного полка?',
        ['Менее 10', 'Более 100', 'Примерно 50'],
        1
    ),
    Question(
        'Какие трудности испытывали женщины-снайперы, помимо боевых действий?',
        ['Только голод и холод', 'Голод, холод, психологическое давление, физическая усталость', 'Никаких трудностей не испытывали'],
        1
    ),
    Question(
        'Как война повлияла на семейные отношения?',
        ['Не повлияла', 'Укрепила', 'Привела к распаду многих семей'],
        2
    ),
    Question(
        'Какие последствия войны сказались на здоровье женщин?',
        ['Никаких', 'Физические и психологические травмы', 'Только физические травмы'],
        1
    ),
    Question(
        'Какую роль играли письма женщин с фронта?',
        ['Не имели значения', 'Поддерживали моральный дух бойцов', 'Только доставляли плохие новости'],
        1
    ),
    Question(
        'Какое из этих действий часто совершали женщины-партизанки?',
        ['Танковые атаки', 'Подрыв мостов и путей сообщения', 'Строили военную технику'],
        1
    ),
    Question(
        'Как часто женщины работали на оборонных предприятиях?',
        ['Очень редко', 'Составляли значительную часть рабочей силы', 'Работала только часть женщин'],
        1
    ),
    Question(
        'Какие навыки были особенно ценны у женщин, работавших на заводе?',
        ['Навыки вождения', 'Навыки точной работы, сборки', 'Навыки программирования'],
        1
    ),
    Question(
        'Как война повлияла на роль женщин в обществе после ее окончания?',
        ['Не изменила', ' Уменьшила их роль', 'Расширила их права и возможности'],
        2
    )



]