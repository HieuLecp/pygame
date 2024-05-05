import pygame
import os
import time
import random
import sys
pygame.font.init()

WIDTH, HEIGHT = 850, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Tutorial")
game_paused= False

#Hình ảnh địch
RED_SPACE_SHIP = pygame.image.load(os.path.join("Pygame", "turorial", "assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("Pygame", "turorial", "assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("Pygame", "turorial", "assets", "pixel_ship_blue_small.png"))

#Hình ảnh Người chơi
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("Pygame", "turorial", "assets", "pixel_ship_yellow.png"))

# Đạn
RED_LASER = pygame.image.load(os.path.join("Pygame", "turorial", "assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("Pygame", "turorial", "assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("Pygame", "turorial", "assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("Pygame", "turorial", "assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("Pygame", "turorial", "assets", "background.jpg")), (WIDTH, HEIGHT))

#Kiểm tra va chạm
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

#Tàu
class Ship:
    COOLDOWN = 35

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

#Tàu Người chơi
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

#Tàu địch
class Enemy(Ship):
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    # di chuyển tàu địch
    def move(self, vel):
        self.y += vel
    # đạn của tàu địch
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

#menu game
class Button:
    def __init__(self, text, x, y, width, height, color, highlight_color, function):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.highlight_color = highlight_color
        self.function = function
def draw_button(button):
    screen.blit(BG, (0,0))
    pygame.draw.rect(screen, button.color, (button.x, button.y, button.width, button.height))
    pygame.draw.rect(screen, button.highlight_color, (button.x, button.y, button.width, button.height), 3)
    font = pygame.font.Font(None, 36)
    text = font.render(button.text, True, (255, 255, 255))
    text_rect = text.get_rect(center=(button.x + button.width / 2, button.y + button.height / 2))
    screen.blit(text, text_rect)        
def handle_click(buttons, mouse_pos):
    for button in buttons:
        if button.x < mouse_pos[0] < button.x + button.width and button.y < mouse_pos[1] < button.y + button.height:
            button.function()

def pause_game():
    global game_paused
    game_paused= not game_paused
#kiểm tra va chạm
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)
    enemies = []
    wave_length = 5
    enemy_vel = 1
    player_vel = 5
    laser_vel = 5
    player = Player(300, 630)
    clock = pygame.time.Clock()
    lost = False
    lost_count = 0
    
    #cửa sổ trò chơi
    def redraw_window():
        screen.blit(BG, (0,0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        screen.blit(lives_label, (10, 10))
        screen.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(screen)

        player.draw(screen)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            screen.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        # if keys[pygame.K_p]:
        #     pause_game()
        # if not game_paused:
        #     pass

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)

def quit_game():
    pygame.quit()
    sys.exit()

# def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        screen.blit(BG, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        screen.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()
def main_menu():
    start_button = Button("Start", 350, 300, 200, 50, (0, 0, 255), (0, 0, 150), main)
    #options_button = Button("Options", 100, 200, 200, 50, (0, 0, 255), (0, 0, 150), open_options)
    quit_button = Button("Quit", 350, 400, 200, 50, (255, 0, 0), (150, 0, 0), quit_game)

    buttons = [start_button, quit_button]

    running = True
    while running:
        screen.blit(BG, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(buttons, pygame.mouse.get_pos())
        screen.fill((0, 0, 0))
        for button in buttons:
            draw_button(button)
        pygame.display.flip()
    pygame.quit()

main_menu()