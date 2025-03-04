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
