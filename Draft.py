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
    )
]

class QuizGame:
    def __init__(self):
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.running = True

    def draw_question(self):
        question = self.questions[self.current_question]

        #Отрисовка текста вопроса
        text = font1.render(question.text, True, black)
        text_rect = text.get_rect(center=(width//2, 100))
        screen.blit(text, text_rect)

        #Отрисовка кнопок с ответами
        button_height =  50
        button_width = 600
        spacing = 20
        start_y = 200

        for i, answer in enumerate(question.answers):
            rect = pygame.Rect(
                (width - button_width)//2,
                start_y + i*(button_height + spacing),
                button_width,
                button_height
            )

            pygame.draw.rect(screen, gray, rect)
            text = font2.render(answer, True, black)
            text_rect = text.get_rect(center = rect.center)
            screen.blit(text, text_rect)
    def check_answer(self, pos):
        question = self.questions[self.current_question]
        button_width = 600
        button_height = 50
        start_y = 200
        spacing = 20

        for i in range(len(question.answers)):
            rect = pygame.Rect(
                (width - button_width)//2,
                start_y + i*(button_height + spacing),
                button_width,
                button_height
            )
            if rect.collidepoint(pos):
                if i == question.correct:
                    self.score += 1
                self.current_question +=1
                if self.current_question >= len(self.questions):
                    self.show_final_score()
                return
    def show_final_score(self):
        screen.fill(white)
        text = font3.render(f"Паравильных ответов: {self.score} из {len(questions)}", True, green)
        text_rect = text.get_rect(center = (width//2 , height//2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        self.running =  False

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

                #Отображение счёта
                score_text = font3.render(f"Счёт: {self.score}", True, black)
                screen.blit(score_text, (20, 20))

                pygame.display.update()
if __name__ == "__main__":
    game = QuizGame()
    game.run()
    pygame.quit()
