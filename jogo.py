import pygame
import random

# --- Configurações Iniciais ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SNAKE_BLOCK_SIZE = 20
FPS = 10 # Velocidade do jogo (frames por segundo)

# --- Cores ---
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# --- Inicializa o Pygame ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

# --- Funções do Jogo ---

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])

def message(msg, color):
    font_style = pygame.font.SysFont("bahnschrift", 25)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    # Posição inicial da cobrinha
    lead_x = SCREEN_WIDTH / 2
    lead_y = SCREEN_HEIGHT / 2

    # Mudança de direção
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Posição inicial da comida
    food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Você Perdeu! Pressione C-Jogar Novamente ou Q-Sair", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop() # Reinicia o jogo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -SNAKE_BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = SNAKE_BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -SNAKE_BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = SNAKE_BLOCK_SIZE
                    lead_x_change = 0

        # --- Lógica de Colisão com as Bordas ---
        if lead_x >= SCREEN_WIDTH or lead_x < 0 or lead_y >= SCREEN_HEIGHT or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])

        # Adiciona a cabeça da cobrinha à lista
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        # Remove o último segmento se a cobrinha não cresceu
        if len(snake_list) > snake_length:
            del snake_list[0]

        # --- Lógica de Colisão com o Próprio Corpo ---
        for x in snake_list[:-1]: # Verifica todos os segmentos, exceto a cabeça
            if x == snake_head:
                game_close = True

        draw_snake(snake_list)
        pygame.display.update()

        # --- Lógica de Comer Comida ---
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE) / 20.0) * 20.0
            snake_length += 1 # Aumenta o tamanho da cobrinha

        clock.tick(FPS)

    pygame.quit()
    quit()

# --- Inicia o Jogo ---
game_loop()