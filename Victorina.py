import pygame
import sys

pygame.init()

#Настройка окна
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Викторина "Женщины Великой Отечественной войны"')

#Цвета
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)

#Шрифты
font1 = pygame.font.SysFont("Times New Roman", 24, bold = True)
font2 = pygame.font.SysFont("Times New Roman", 20)
font3 = pygame.font.SysFont("Times New Roman", 30, bold = True)
