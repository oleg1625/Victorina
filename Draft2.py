import pygame
import sys
import os

# Инициализация PyGame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
LEADERBOARD_FILE = "Draft2leaderboard.txt"

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200, 128)  # Полупрозрачный серый
TEXT_COLOR = (255, 255, 0)  # Желтый для контраста
green = (0, 255, 0)

# Шрифты
font = pygame.font.SysFont('Arial', 24)
title_font = pygame.font.SysFont('Arial', 36, bold=True)

# Загрузка фонового изображения
try:
    background = pygame.image.load("photo.jpg")  # Укажите свой файл
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except Exception as e:
    print(f"Ошибка загрузки фона: {e}")
    sys.exit()


class TextInput:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ''
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode


# Класс вопроса (остается без изменений)
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
    # Добавьте другие вопросы
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
        text_bg = pygame.Surface((WIDTH - 40, 100), pygame.SRCALPHA)
        text_bg.fill(GRAY)
        screen.blit(text_bg, (20, 50))

        # Текст вопроса
        text = title_font.render(question.text, True, TEXT_COLOR)
        screen.blit(text, (50, 70))

        # Кнопки ответов
        button_height = 50
        button_width = 600
        start_y = 200

        for i, answer in enumerate(question.answers):
            rect = pygame.Rect(
                (WIDTH - button_width) // 2,
                start_y + i * (button_height + 20),
                button_width,
                button_height
            )
            # Подложка для кнопки
            btn_bg = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
            btn_bg.fill((100, 100, 100, 128))
            screen.blit(btn_bg, rect.topleft)

            text = font.render(answer, True, TEXT_COLOR)
            screen.blit(text, (rect.x + 20, rect.y + 15))

    def check_answer(self, pos):
        question = self.questions[self.current_question]
        button_width = 600
        button_height = 50
        start_y = 200
        spacing = 20

        for i in range(len(question.answers)):
            rect = pygame.Rect(
                (WIDTH - button_width) // 2,
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
        background.fill(WHITE)
        text = font.render(f"Паравильных ответов: {self.score} из {len(questions)}", True, green)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        background.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        self.running = False

    def run(self):
        while self.running:
            background.fill(WHITE)

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
                score_text = font.render(f"Счёт: {self.score}", True, BLACK)
                background.blit(score_text, (20, 20))

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
    pygame.time.wait(5000)
    pygame.quit()


if __name__ == "__main__":
    main()