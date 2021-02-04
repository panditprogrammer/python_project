
import pygame
import random

pygame.init()

# Colors
white = (220, 220, 220)
green = (252 , 142 , 69)
black = (87 , 68 , 79)
red = (200,22,22)

# Creating window
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snack_PY : PanditProgrammer.com")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game Loop

def gameloop():
	# Game specific variables
	exit_game = False
	game_over = False
	snake_x = 45
	snake_y = 55
	velocity_x = 0
	velocity_y = 0
	snk_list = []
	snk_length = 1

	food_x = random.randint(20, screen_width -10)
	food_y = random.randint(20, screen_height -10)
	score = 0
	init_velocity = 5
	snake_size = 30
	fps = 30
	while not exit_game:
		if game_over:
			gameWindow.fill(white)
			text_screen("Game Over ! ", red, 275, 220)
			text_screen("Press Enter To Play Again", black, 200, 260)
			text_screen(f"Your Score is {score}", (13 , 142 , 16), 250, 300)
			

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						gameloop()

		else:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						velocity_x = init_velocity
						velocity_y = 0

					if event.key == pygame.K_LEFT:
						velocity_x = - init_velocity
						velocity_y = 0

					if event.key == pygame.K_UP:
						velocity_y = - init_velocity
						velocity_x = 0

					if event.key == pygame.K_DOWN:
						velocity_y = init_velocity
						velocity_x = 0

			snake_x = snake_x + velocity_x
			snake_y = snake_y + velocity_y

			if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
				score +=1
				food_x = random.randint(20, screen_width -10)
				food_y = random.randint(20, screen_height -10)
				snk_length +=5

			gameWindow.fill(white)
			text_screen("Score: " + str(score ), (0 , 193 , 49), 600, 5)
			pygame.draw.rect(gameWindow, green, [food_x, food_y, snake_size, snake_size])


			head = []
			head.append(snake_x)
			head.append(snake_y)
			snk_list.append(head)

			if len(snk_list)>snk_length:
				del snk_list[0]

			if head in snk_list[:-1]:
				game_over = True

			if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
				game_over = True
			plot_snake(gameWindow, black, snk_list, snake_size)
		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	quit()
gameloop()