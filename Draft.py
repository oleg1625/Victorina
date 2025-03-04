import pygame
import sys
import os

# Инициализация PyGame
pygame.init()

# Константы
width = 1280
height = 720
LEADERBOARD_FILE = "Draftleaderboard.txt"  # Файл для хранения результатов

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

# Шрифты
font1 = pygame.font.SysFont("Times New Roman", 24, bold=True)
font2 = pygame.font.SysFont("Times New Roman", 20)
font3 = pygame.font.SysFont("Times New Roman", 30, bold=True)

# Загрузка фонвого изображения
try:
    background = pygame.image.load("photo.jpg")
    background = pygame.transform.scale(background, (width, height))
except Exception as e:
    print(f"Ошибка загрузки фона: {e}")
    sys.exit()

# Класс для обработки текстового ввода (регистрация)
class TextInput:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ''
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:  # Завершение ввода по Enter
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode


# Функции для работы с таблицей лидеров
def save_to_leaderboard(username, score):
    """Сохраняет результат в файл"""
    with open(LEADERBOARD_FILE, 'a') as f:
        f.write(f"{username},{score}\n")


def load_leaderboard():
    """Загружает и сортирует результаты из файла"""
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    scores = []
    with open(LEADERBOARD_FILE, 'r') as f:
        for line in f:
            username, score = line.strip().split(',')
            scores.append((username, int(score)))

    # Сортировка по убыванию очков
    return sorted(scores, key=lambda x: x[1], reverse=True)[:5]  # Топ-5


# Вопросы и ответы
class Question:
    def __init__(self, text, answers, correct):
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

class QuizGame:
    def __init__(self):
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.running = True

    def draw_question(self, screen):
        # Рисуем фон
        screen.blit(background, (0, 0))

        question = self.questions[self.current_question]

        # Полупрозрачная подложка для текста
        text_bg = pygame.Surface((width - 40, 100), pygame.SRCALPHA)
        text_bg.fill(gray)
        screen.blit(text_bg, (20, 50))

        # Текст вопроса
        text = font1.render(question.text, True, yellow)
        screen.blit(text, (50, 70))

        # Кнопки ответов
        button_height = 50
        button_width = 600
        start_y = 200

        for i, answer in enumerate(question.answers):
            rect = pygame.Rect(
                (width - button_width) // 2,
                start_y + i * (button_height + 20),
                button_width,
                button_height
            )
            # Подложка для кнопки
            btn_bg = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
            btn_bg.fill((100, 100, 100, 128))
            screen.blit(btn_bg, rect.topleft)

            text = font2.render(answer, True, yellow)
            screen.blit(text, (rect.x + 20, rect.y + 15))

    def check_answer(self, pos):
        question = self.questions[self.current_question]
        button_width = 600
        button_height = 50
        start_y = 200
        spacing = 20

        for i in range(len(question.answers)):
            rect = pygame.Rect(
                (width - button_width) // 2,
                start_y + i * (button_height + spacing),
                button_width,
                button_height
            )
            if rect.collidepoint(pos):
                if i == question.correct:
                    self.score += 1
                self.current_question += 1
                if self.current_question >= len(self.questions):
                    self.show_final_score()
                return

    def show_final_score(self):
        screen.fill(white)
        text = font3.render(f"Паравильных ответов: {self.score} из {len(questions)}", True, green)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        self.running = False

    def run(self):
        while self.running:
            screen.fill(white)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_answer(event.pos)

                if self.current_question < len(self.questions):
                    self.draw_question()
                else:
                    self.show_final_score()

                # Отображение счёта
                score_text = font3.render(f"Счёт: {self.score}", True, black)
                screen.blit(score_text, (20, 20))

                pygame.display.update()

    # Функции для работы с таблицей лидеров
    def save_to_leaderboard(username, score):
        with open(LEADERBOARD_FILE, 'a') as f:
            f.write(f"{username},{score}\n")

    def load_leaderboard():
        if not os.path.exists(LEADERBOARD_FILE):
            return []
        scores = []
        with open(LEADERBOARD_FILE, 'r') as f:
            for line in f:
                username, score = line.strip().split(',')
                scores.append((username, int(score)))
        return sorted(scores, key=lambda x: x[1], reverse=True)[:5]

    def main():
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Викторина ВОВ с фоном")

        # Регистрация пользователя
        username = ""
        text_input = TextInput(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
        done = False

        while not done:
            # Рисуем фон
            screen.blit(background, (0, 0))

            # Отрисовка элементов регистрации
            title = title_font.render("Введите ваше имя:", True, TEXT_COLOR)
            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

            pygame.draw.rect(screen, (255, 255, 255), text_input.rect)
            text_surface = font.render(text_input.text, True, BLACK)
            screen.blit(text_surface, (text_input.rect.x + 5, text_input.rect.y + 5))

            pygame.display.flip()

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                text_input.handle_event(event)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if len(text_input.text) > 0:
                        username = text_input.text
                        done = True

        # Запуск викторины
        game = QuizGame()
        game.run()

        # Сохранение результата
        save_to_leaderboard(username, game.score)
        leaderboard = load_leaderboard()

        # Отображение таблицы лидеров
        screen.blit(background, (0, 0))
        title = title_font.render("Таблица лидеров", True, TEXT_COLOR)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        y = 150
        for i, (name, score) in enumerate(leaderboard):
            text = font.render(f"{i + 1}. {name}: {score} правильных ответов", True, TEXT_COLOR)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y))
            y += 50

        pygame.display.flip()
        pygame.time.wait(30000)
        pygame.quit()

    if __name__ == "__main__":
        main()