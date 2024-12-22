import pygame
import numpy as np
import math
from queue import PriorityQueue

# Initialize Pygame
pygame.init()

# Constants for the window
tile_size = 20
width, height = 600, 400
tiles_x, tiles_y = width // tile_size, height // tile_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Robot Vacuum Pathfinding")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Initialize grid and robot
grid = [[0 for _ in range(tiles_x)] for _ in range(tiles_y)]
robot_position = [5, 5]
end_point = [25, 15]
robot_speed = 0.1  # Time in seconds per tile
robot_direction = [0, 0]
lidar_range = 5
lidar_error = 0.1
path_traveled = []

# Timing
clock = pygame.time.Clock()
FPS = 60

autonomous_mode = False
path = []
steps_timer = 0

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_path(start, goal):
    open_set = PriorityQueue()
    open_set.put((0, tuple(start)))
    came_from = {}
    g_score = {tuple(start): 0}
    f_score = {tuple(start): heuristic(start, goal)}

    while not open_set.empty():
        _, current = open_set.get()
        current = list(current)
        if current == goal:
            reconstructed_path = []
            while tuple(current) in came_from:
                reconstructed_path.append(current)
                current = came_from[tuple(current)]
            reconstructed_path.reverse()
            return reconstructed_path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = [current[0] + dx, current[1] + dy]
            if 0 <= neighbor[0] < tiles_x and 0 <= neighbor[1] < tiles_y and grid[neighbor[1]][neighbor[0]] == 0:
                tentative_g_score = g_score[tuple(current)] + 1
                if tuple(neighbor) not in g_score or tentative_g_score < g_score[tuple(neighbor)]:
                    came_from[tuple(neighbor)] = current
                    g_score[tuple(neighbor)] = tentative_g_score
                    f_score[tuple(neighbor)] = tentative_g_score + heuristic(neighbor, goal)
                    open_set.put((f_score[tuple(neighbor)], tuple(neighbor)))

    return []

# Functions
def draw_grid():
    for x in range(0, width, tile_size):
        pygame.draw.line(screen, GRAY, (x, 0), (x, height))
    for y in range(0, height, tile_size):
        pygame.draw.line(screen, GRAY, (0, y), (width, y))

def draw_robot():
    pygame.draw.rect(screen, BLUE, pygame.Rect(
        robot_position[0] * tile_size,
        robot_position[1] * tile_size,
        tile_size, tile_size
    ))

def draw_end_point():
    pygame.draw.rect(screen, GREEN, pygame.Rect(
        end_point[0] * tile_size,
        end_point[1] * tile_size,
        tile_size, tile_size
    ))

def draw_obstacles():
    for y in range(tiles_y):
        for x in range(tiles_x):
            if grid[y][x] == 1:
                pygame.draw.rect(screen, BLACK, pygame.Rect(
                    x * tile_size, y * tile_size, tile_size, tile_size
                ))

def draw_lidar():
    for angle in range(0, 360, 10):
        rad_angle = math.radians(angle)
        x = robot_position[0] + math.cos(rad_angle)
        y = robot_position[1] + math.sin(rad_angle)
        distance = 0
        while distance < lidar_range:
            x_step = int(x + distance * math.cos(rad_angle))
            y_step = int(y + distance * math.sin(rad_angle))
            if 0 <= x_step < tiles_x and 0 <= y_step < tiles_y and grid[y_step][x_step] == 1:
                break
            distance += lidar_error
        pygame.draw.line(screen, RED,
                         (robot_position[0] * tile_size + tile_size // 2, robot_position[1] * tile_size + tile_size // 2),
                         ((robot_position[0] + math.cos(rad_angle) * distance) * tile_size + tile_size // 2,
                          (robot_position[1] + math.sin(rad_angle) * distance) * tile_size + tile_size // 2),
                         1)

def draw_path_traveled():
    for step in path_traveled:
        pygame.draw.rect(screen, ORANGE, pygame.Rect(
            step[0] * tile_size, step[1] * tile_size, tile_size, tile_size
        ))

def draw_info():
    font = pygame.font.SysFont(None, 24)
    coords_text = font.render(f"Coords: {robot_position}", True, BLACK)
    speed_text = font.render(f"Speed: {robot_speed:.1f}s/tile", True, BLACK)
    screen.blit(coords_text, (10, 10))
    screen.blit(speed_text, (10, 30))

def move_robot():
    global robot_position, path, steps_timer, path_traveled
    steps_timer += clock.get_time() / 1000.0
    if steps_timer >= robot_speed:
        steps_timer = 0
        if autonomous_mode and path:
            next_step = path.pop(0)
            robot_position = next_step
            path_traveled.append(list(robot_position))
        elif not autonomous_mode:
            new_x = robot_position[0] + robot_direction[0]
            new_y = robot_position[1] + robot_direction[1]
            if 0 <= new_x < tiles_x and 0 <= new_y < tiles_y and grid[new_y][new_x] != 1:
                robot_position = [new_x, new_y]
                path_traveled.append(list(robot_position))

# Main loop
running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    draw_obstacles()
    draw_path_traveled()
    draw_end_point()
    draw_robot()
    draw_lidar()
    draw_info()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x, grid_y = mouse_x // tile_size, mouse_y // tile_size
            if event.button == 1:
                grid[grid_y][grid_x] = 1
            elif event.button == 3:
                grid[grid_y][grid_x] = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if not (robot_direction[0] == 0 and robot_direction[1] == -1):
                    robot_direction = [0, -1]
            elif event.key == pygame.K_s:
                if not (robot_direction[0] == 0 and robot_direction[1] == 1):
                    robot_direction = [0, 1]
            elif event.key == pygame.K_a:
                if not (robot_direction[0] == -1 and robot_direction[1] == 0):
                    robot_direction = [-1, 0]
            elif event.key == pygame.K_d:
                if not (robot_direction[0] == 1 and robot_direction[1] == 0):
                    robot_direction = [1, 0]
            elif event.key == pygame.K_SPACE:
                robot_direction = [0, 0]
            elif event.key == pygame.K_p:  # Activate autonomous mode
                autonomous_mode = True
                path = find_path(robot_position, end_point)
            elif event.key == pygame.K_UP:  # Decrease speed
                robot_speed = max(0.1, robot_speed - 0.5)
            elif event.key == pygame.K_DOWN:  # Increase speed
                robot_speed += 0.5

    move_robot()
    clock.tick(FPS)

pygame.quit()
