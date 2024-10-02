import pygame
import pygame.locals
import time

pygame.init()

intro = True

game_over = False
score = 0

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
grey = (211,211,211)
yellow = (255,255,0)

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Triangle Evader")

font = pygame.font.Font("/Users/Bennet/Documents/Python/DofE Projects/Week 8.py/PublicPixel-z84yD.ttf", 10)
bigger_font = pygame.font.Font("/Users/Bennet/Documents/Python/DofE Projects/Week 8.py/PublicPixel-z84yD.ttf",20)
biggest_font = pygame.font.Font("/Users/Bennet/Documents/Python/DofE Projects/Week 8.py/PublicPixel-z84yD.ttf", 32)
huge_font = pygame.font.Font("/Users/Bennet/Documents/Python/DofE Projects/Week 8.py/PublicPixel-z84yD.ttf", 95)

#og tri 15 112.5
#menu set up
#use rects to move everything and do flashing animation for keys
menu_rect = pygame.Rect(600, 35, 1, 1)
menu_text = "Bennet Thomas presents..."
menu_text = font.render(menu_text, True, white)

game_rect = pygame.Rect(-480, 110, 1, 1)
game_text = "Triangle Evader"
game_text = biggest_font.render(game_text, True, yellow)

comment_rect = pygame.Rect(45, 152.5, 1, 1)
comment = "(NOT from the authors of Rectangle Dodger)"
comment = font.render(comment, True, red)

triangle_rect = pygame.Rect(500, 105, 1, 1)
triangle = pygame.image.load("/Users/Bennet/Documents/Python/DofE Projects/Week 8.py/yellow-triangle-sign-in-pixel-art-style-vector.png")
triangle = pygame.transform.scale(triangle, (75,75))

def menu():
    screen.fill(black)
    
    screen.blit(menu_text, (menu_rect.x, menu_rect.y))
    if menu_rect.x > 180:
        menu_rect.x -= 2.5
        
    screen.blit(game_text, (game_rect.x, game_rect.y))
    if game_rect.x < 21 and menu_rect.x <= 180:
        game_rect.x += 3
    screen.blit(triangle, (triangle_rect.x, triangle_rect.y))
    
    if game_rect.x >= 21:
        time.sleep(0.75)
        screen.blit(comment, (comment_rect.x, comment_rect.y))
    
    
def draw_game():
    screen.fill(white)
    if game_over == True:
        screen.fill(black)
        game_over_text = "Game Over!"
        game_over_text_display = bigger_font.render(game_over_text, True, red)
        final_score = "Score: " + str(score)
        final_score_display = font.render(final_score, True, white)
        screen.blit(final_score_display, (139, 270))
        screen.blit(game_over_text_display, (90, 240))



run = True
while run:
    clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    if intro:
        menu()
    else:
        draw_game()
    pygame.display.update()
    

pygame.quit()
