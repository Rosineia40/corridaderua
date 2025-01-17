import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações básicas
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Corrida de Rua - Roguelike")
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Carregar sprites
player_sprite = pygame.image.load("assets/sprites/player.png")
player_sprite = pygame.transform.scale(player_sprite, (50, 50))

obstacle_sprite = pygame.image.load("assets/sprites/obstacle.png")
obstacle_sprite = pygame.transform.scale(obstacle_sprite, (50, 50))

# Configuração inicial do jogador
player_pos = [WIDTH // 2, HEIGHT - 100]
player_speed = 5

# Obstáculos
obstacles = []
obstacle_speed = 3
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1000)

# Função para desenhar o jogador
def draw_player():
    screen.blit(player_sprite, player_pos)

# Função para desenhar obstáculos
def draw_obstacles():
    for obstacle in obstacles:
        screen.blit(obstacle_sprite, obstacle)

# Loop principal
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_EVENT:
            x_pos = random.randint(0, WIDTH - 50)
            obstacles.append([x_pos, -50])

    # Movimentação do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - 50:
        player_pos[0] += player_speed

    # Movimentação dos obstáculos
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)

    # Verificar colisão
    for obstacle in obstacles:
        if (
            player_pos[0] < obstacle[0] + 50
            and player_pos[0] + 50 > obstacle[0]
            and player_pos[1] < obstacle[1] + 50
            and player_pos[1] + 50 > obstacle[1]
        ):
            print("Game Over!")
            running = False

    # Desenhar elementos
    draw_player()
    draw_obstacles()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()