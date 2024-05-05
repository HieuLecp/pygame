
import pygame
import os
import random
import sys
pygame.init()

font = pygame.font.Font(None, 30)
WIDTH, HEIGHT = 850, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
start = True
pygame.display.set_caption("Chicken Invaders")
pygame.display.set_icon(pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "icon-chicken.png")))
sound = pygame.mixer.Sound(os.path.join("Pygame", "Chicken_Invaders", "sound.wav"))
sound1 = pygame.mixer.Sound(os.path.join("Pygame", "Chicken_Invaders", "sound1.wav"))

# kẻ địch
# RED_SPACE_CHICKEN = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets","chicken-red.png"))
# RED_SPACE_CHICKEN = pygame.transform.scale(RED_SPACE_CHICKEN, (60, 60))
# GREEN_SPACE_CHICKEN = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "chicken-green.png"))
# GREEN_SPACE_CHICKEN = pygame.transform.scale(GREEN_SPACE_CHICKEN, (60, 60))
BLUE_SPACE_CHICKEN = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "chicken-blue.png"))
BLUE_SPACE_CHICKEN = pygame.transform.scale(BLUE_SPACE_CHICKEN, (60, 60))
BIG_SPACE_CHICKEN = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "chicken-1.png"))
BIG_SPACE_CHICKEN = pygame.transform.scale(BIG_SPACE_CHICKEN, (60, 60))
POLICE_SPACE_CHICKEN = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "chicken-2.png"))
POLICE_SPACE_CHICKEN = pygame.transform.scale(POLICE_SPACE_CHICKEN, (70, 70))
W_SPACE_CHICKEN = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "chicken-3.png"))
W_SPACE_CHICKEN = pygame.transform.scale(W_SPACE_CHICKEN, (65, 80))
FLY_SPACE_CHICKEN = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "chicken-fly.png"))
FLY_SPACE_CHICKEN = pygame.transform.scale(FLY_SPACE_CHICKEN, (60, 95))

BOSS_CHICKEN =  pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "boss.png"))
BOSS_CHICKEN = pygame.transform.scale(BOSS_CHICKEN, (500, 300))

# Vật phẩm
BOX_RED = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets","bandage.png"))
BOX_RED = pygame.transform.scale(BOX_RED, (90, 70))
BOX_GREEN = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets","box-bullet1.png"))
BOX_GREEN = pygame.transform.scale(BOX_GREEN, (35, 35))
BOX_PURPLE = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets","box-bullet3.png"))
BOX_PURPLE = pygame.transform.scale(BOX_PURPLE, (35, 35))
BOX_ORANGE = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets","box-bullet4.png"))
BOX_ORANGE = pygame.transform.scale(BOX_ORANGE, (35, 35))
BOX_BLUE = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets","box-bullet5.png"))
BOX_BLUE = pygame.transform.scale(BOX_BLUE, (35, 35))

# người chơi
PLANE = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "plan.png"))
PLANE = pygame.transform.scale(PLANE, (80, 90))
GREEN_LASER = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "bullet1.png"))
GREEN_LASER = pygame.transform.scale(GREEN_LASER, (80, 68))
RED_LASER = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "bullet2.png"))
RED_LASER = pygame.transform.scale(RED_LASER, (80, 68))
PURPLE_LASER = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "bullet3.png"))
PURPLE_LASER = pygame.transform.scale(PURPLE_LASER, (80, 68))
ORANGE_LASER = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "bullet4.png"))
ORANGE_LASER = pygame.transform.scale(ORANGE_LASER, (90, 80))
BLUE_LASER = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "bullet5.png"))
BLUE_LASER = pygame.transform.scale(BLUE_LASER, (85, 60))
CHICKEN = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "duiga.png"))
CHICKEN = pygame.transform.scale(CHICKEN, (30, 40))
ROCKET = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "rocket.png"))
MINI_ROCKET = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "rocket.png"))
ROCKET = pygame.transform.scale(ROCKET, (40, 40))
ROCKET_LASER = pygame.transform.scale(MINI_ROCKET, (600, 600))

# trung
EGG_1 = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "egg.png"))
EGG_1 = pygame.transform.scale(EGG_1, (20, 20))
EGG_2 = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "egg1.png"))
EGG_2 = pygame.transform.scale(EGG_2, (35,38))
EGG_3 = pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "egg3.png"))
EGG_3 = pygame.transform.scale(EGG_3, (20,25))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "background.png")), (WIDTH, HEIGHT))
BG1 = pygame.transform.scale(pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "bg1.jpg")), (WIDTH, HEIGHT))
BG2 = pygame.transform.scale(pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "BG2.jpg")), (WIDTH, HEIGHT))
BG3 = pygame.transform.scale(pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "BG3.JPEG")), (WIDTH, HEIGHT))
BG4 = pygame.transform.scale(pygame.image.load(os.path.join("Pygame", "Chicken_Invaders", "assets", "BG4.jpeg")), (WIDTH, HEIGHT))


class Egg: 
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    # def off_screen(self, height):
    #     return not(self.y <= height  and self.y >= -10)

    def off_screen(self,height, self_height = 0):
        return not(self.y - self_height <= height  and self.y + self_height >= -10)
    
    def collision(self, obj):
        return collide(self, obj)

class Plane:
    COOLDOWN = 60

    def __init__(self, x, y, health=200):
        self.x = x
        self.y = y
        self.health = health
        self.img = None
        self.laser_img = None
        self.lasers = []
        self.rockets = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
        
        for rocket in self.rockets:
            rocket.draw(window)

    #move_laser: di chuyển vs tốc độ "vel", off_screen thì remove khỏi lasers -> mất khỏi màn hình
    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    #cooldown chiêu bắn
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
    
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Egg(self.x, self.y-25, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
    #add_rocket: thêm rocket vào rockets, rocket là 1 Egg()
    def add_rocket(self):
        if self.cool_down_counter == 0:
            rocket = Egg(self.x - 260, self.y, ROCKET_LASER)
            self.rockets.append(rocket)
            self.cool_down_counter = 1
    
    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()

# class Plan:
#     COOLDOWN = 30

#     def __init__(self, x, y, health=200):
#         self.x = x
#         self.y = y
#         self.health = health
#         self.img = None
#         self.laser_img = None
#         self.lasers = []
#         self.rocket = []
#         self.cool_down_counter = 0

#     def draw(self, window):
#         window.blit(self.img, (self.x, self.y))
#         for laser in self.lasers:
#             laser.draw(window)

#     def move_lasers(self, vel, obj):
#         self.cooldown()
#         for laser in self.lasers:
#             laser.move(vel)
#             if laser.off_screen(HEIGHT):
#                 self.lasers.remove(laser)
#             elif laser.collision(obj):
#                 obj.health -= 10
#                 self.lasers.remove(laser)

#     def cooldown(self):
#         if self.cool_down_counter >= self.COOLDOWN:
#             self.cool_down_counter = 0
#         elif self.cool_down_counter > 0:
#             self.cool_down_counter += 1

#     def shoot(self):
#         if self.cool_down_counter == 0:
#             laser = Egg(self.x, self.y-25, self.laser_img)
#             self.lasers.append(laser)
#             self.cool_down_counter = 1

#     def get_width(self):
#         return self.img.get_width()

#     def get_height(self):
#         return self.img.get_height()



class Player(Plane):
    def __init__(self, x, y, health=200):
        super().__init__(x, y, health)
        self.img = PLANE
        self.laser_img = BLUE_LASER
        self.mask = pygame.mask.from_surface(self.img)
        self.max_health = health
        self.chicken = []
        
    #off_screen : Xóa khỏi lasers, 
    #nếu objs là 1 list: laser var obj thì remove obj, add chicken_thighs vào chicken
    # nếu chicken thighs đủ 10 thì có rocket

    #shoot_rocket: khi obj là 1 (boss) thì boss health - 50, nếu là objs thì remove hết những obj chạm vào
    def shoot_rocket(self, vel, objs):
        self.cooldown()
        for rocket in self.rockets:
            rocket.move(vel)
            if rocket.off_screen(HEIGHT, self_height=300):
                self.rockets.remove(rocket)
            else:
                if type(objs) is list:
                    for obj in objs:
                        if rocket.collision(obj):
                            objs.remove(obj)
                        
                else:
                    if rocket.collision(objs):
                        objs.health -= 50
                        self.rockets.remove(rocket)
        
    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                if type(objs) is list:
                    for obj in objs:
                        if laser.collision(obj):
                            x = obj.x
                            y = obj.y
                            chicken_thighs = Egg(x+20,y+10, CHICKEN)
                            objs.remove(obj)
                            i= random.randrange(1, 3)
                            if i == 1:
                                self.chicken.append(chicken_thighs)
            
                            if laser in self.lasers:
                                self.lasers.remove(laser)
                else:
                    if laser.collision(objs):
                        objs.health -= 10    
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (50, 60, (self.img.get_width()-40), 10))
        #pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.img.get_height() + 10, self.img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (50, 60, (self.img.get_width()-40) * (self.health/self.max_health), 10))


class Chicken(Plane):
    COLOR_MAP = {
                "blue": (BLUE_SPACE_CHICKEN, EGG_1),
                "white": (W_SPACE_CHICKEN, EGG_1),
                "brown": (BIG_SPACE_CHICKEN, EGG_2),
                "police": (POLICE_SPACE_CHICKEN, EGG_3),
                "fly" :(FLY_SPACE_CHICKEN, EGG_3),
                }

    def __init__(self, x, y, color, health=200):
        super().__init__(x, y, health)
        self.img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Egg(self.x+20, self.y+30, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


class Boss(Plane):   
    def __init__(self, x, y, vel_boss_x, vel_boss_y, health=300):
        super().__init__(x, y, health)
        self.img = BOSS_CHICKEN
        self.mask = pygame.mask.from_surface(self.img)
        self.vel_boss_x = vel_boss_x
        self.vel_boss_y = vel_boss_y
        self.max_health = health
        self.egg = EGG_3

    def move(self):
        if self.x <= 0 or self.x + self.img.get_width() >= WIDTH:
            self.vel_boss_x = - self.vel_boss_x
        self.x += self.vel_boss_x
            
        if self.y <= 40 or self.y + self.img.get_height() >= HEIGHT-200:    
            self.vel_boss_y = -self.vel_boss_y
        self.y += self.vel_boss_y

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Egg(self.x + random.randrange(50, 400), self.y+250, self.egg)
            self.lasers.append(laser)
            self.cool_down_counter = 1    
        
    def draw(self, window):
        super().draw(window)   
        self.healthbar(window)   

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (270, 30, (self.img.get_width()-40), 10))
        pygame.draw.rect(window, (0,255, 0), (270, 30, (self.img.get_width()-40) * (self.health/self.max_health), 10))


class Drop_box():
    COLOR = {
                "red": (BOX_RED, RED_LASER),
                "green": (BOX_GREEN, GREEN_LASER),
                "blue": (BOX_BLUE, BLUE_LASER),
                "purple": (BOX_PURPLE, PURPLE_LASER),
                "orange": (BOX_ORANGE, ORANGE_LASER)
            }

    def __init__(self, x, y , color):
        self.x = x
        self.y = y
        self.color = color
        self.img, self.laser = self.COLOR[color]
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y)) 

    def drop(self, vel):
        self.y += vel   
        if self.y >= HEIGHT:
            self.img, self.laser = self.COLOR[random.choice(["red", "green","blue", "purple", "orange"])]
            self.x = random.randint(100, WIDTH-150)
            self.y = -700

    def creat_box_new(self):
        color_picker = random.choice(["red", "green","blue", "purple", "orange"])
        self.img, self.laser = self.COLOR[color_picker]
        self.color = color_picker        
        self.x = random.randrange(100, WIDTH-150)
        self.y = -700        


class Back_ground_shoot:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.img = BG1
        self.heigt = self.img.get_height()

    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        screen.blit(self.img, (self.x, self.y-self.heigt))
        
    def uppdate(self):
        self.y += self.speed
        if self.y == self.heigt:
            self.y = 0        
    
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
def start_game():
    pygame.mixer.Sound.stop(sound1)
    pygame.mixer.Sound.play(sound)
    main()
def totural_game():
    run= True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((0, 0, 0))   
        screen.blit(BG3, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            main_menu()
        pygame.display.update()

    main_menu()
def quit_game():
    pygame.quit()
    sys.exit()
def restart_game():
    lost= False
    main()
def end_menu():
    restart = Button("Restart", 350, 400, 200, 50, (255, 0, 0), (150, 0, 0), restart_game)
    menu = Button("Menu", 350, 500, 200, 50, (0, 0, 255), (0, 0, 150), main_menu)
    luachon= [restart, menu]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(luachon, pygame.mouse.get_pos())
            screen.fill((0, 0, 0))
            screen.blit(BG4, (0, 0))
            for button in luachon:
                draw_button(button)
            pygame.display.flip()
    pygame.quit()
def pause_menu():
    coutine = Button("Coutine", 350, 300, 200, 50, (255, 0, 0), (150, 0, 0))
    
def main():
    run = True
    paused = False
    FPS = 60
    level = 0
    lives = 5
    rocket = 1
    chicken_thigh_nums = 0
    main_font = pygame.font.SysFont("comicsans", 25)
    lost_font = pygame.font.SysFont("comicsans", 60)
    win_font = pygame.font.SysFont("comicsans", 60)
    
    enemies = []
    wave_length = 7
    enemy_vel = 1
    laser_vel_enemy = 2.5
    
    vel_boss_x = 1.2
    vel_boss_y = 1.2
    laser_vel_boss = 1.5
    
    player_vel = 5
    laser_vel_player = 4
    rocket_vel = 6
    
    vel_box = 2
    speed_bg = 1
    
    player = Player(300, 630)
    
    clock = pygame.time.Clock()
    lost = False
    lost_count = 0
    
    bg1 = Back_ground_shoot(0, 0, speed_bg)
    box_bullet = Drop_box(random.randrange(100, WIDTH-150), random.randrange(-900, -100), random.choice(["red", "green", "blue", "purple","orange"]))
    
    boss = Boss(50, 50, vel_boss_x, vel_boss_y)

    def redraw_window():
        bg1.draw()
        bg1.uppdate()  

        box_bullet.drop(vel_box)
        box_bullet.draw(screen)

        player.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)
        
        for chicken_thigh in player.chicken:
            chicken_thigh.draw(screen)

        if collide(box_bullet, player):
            if box_bullet.color == "red":
                player.health = player.health + 20
            else:
                player.laser_img = box_bullet.laser
            box_bullet.creat_box_new()
        
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        text_hp = main_font.render(f"HP: ", 1, (255,255,255))
        rocket_label = main_font.render(f": {rocket}", rocket , (255,255,255))

        screen.blit(lives_label, (10, 10))
        screen.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        screen.blit(text_hp, (10, 45))
        screen.blit(ROCKET, (10, 80))
        screen.blit(rocket_label, (60, 80))

        if level == 5:
            boss.move()        
            boss.draw(screen)  
            boss.shoot()
            boss.move_lasers(laser_vel_boss, player)
            player.move_lasers(-laser_vel_player, boss)
            player.shoot_rocket(-rocket_vel, boss)  
            if boss.health <= 0:
                win_label = win_font.render("You win!!", 1, (255,255,255))
                screen.blit(win_label, (WIDTH/2 - win_label.get_width()/2, 400))
                boss.y = -1000
                boss.lasers = []
                if keys[pygame.K_SPACE]:
                    end_menu()
        
        if level < 5:
            player.move_lasers(-laser_vel_player, enemies)    
            player.shoot_rocket(-rocket_vel, enemies)   

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            screen.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 400))
            bg1.speed = 0  
            pygame.mixer.Sound.stop(sound)
        
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if player.health <= 0 or lives <= 0:
            lost = True
            lost_count += 1

        for chicken_thigh in player.chicken:
            if collide(chicken_thigh, player):
                player.chicken.remove(chicken_thigh)
                chicken_thigh_nums += 1  

        if chicken_thigh_nums == 10:
            rocket += 1   
            chicken_thigh_nums = 0

        if lost:
            if lost_count > FPS * 3:
                end_menu()
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 10
            for i in range(wave_length):
                enemy = Chicken(random.randrange(60, WIDTH-100), random.randrange(-1500, -100), random.choice(["blue", "white", "brown", "police", "fly"]))
                enemies.append(enemy) 

        if level == 5:
            bg1.speed = 0     
            enemy_vel = 0           
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.mixer.Sound.stop(sound)
            if event.type == pygame.MOUSEBUTTONDOWN:	
                if event.button == 1: 
                    enemy_vel = 1
                    laser_vel_enemy = 2.5
                    laser_vel_player = 4
                    player_vel = 5
                    vel_box = 2
                    bg1.speed = 1
                if event.button == 1 and start:
                    player.shoot()
           
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > -50: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH+50: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 5 < HEIGHT+50: # down
            player.y += player_vel
        if keys[pygame.K_SPACE] :
            player.shoot()
            
        if keys[pygame.K_p] :
            if rocket > 0:
                player.add_rocket()
                rocket = 0
                
        if keys[pygame.K_ESCAPE] :
            enemy_vel = 0
            laser_vel_enemy = 0
            player_vel = 0
            laser_vel_player = 0
            vel_box = 0
            bg1.speed = 0
                
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel_enemy, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy) 

        for chicken_thigh in player.chicken:
            chicken_thigh.move(3)  

# def main_menu():
#     title_font = pygame.font.SysFont("comicsans", 60)
#     run = True
#     while run:
#         screen.blit(BG, (0,0))
#         title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
#         screen.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 650))
#         pygame.mixer.Sound.play(sound1)
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 pygame.mixer.Sound.stop(sound1)
#                 pygame.mixer.Sound.play(sound)
#                 main()
#     pygame.quit()

def main_menu(): 
    start_button = Button("Start", 330, 350, 200, 50, (0, 0, 255), (0, 0, 150), start_game)
    totural_button = Button("Totural", 330, 450, 200, 50, (0, 255, 0), (0, 150, 0), totural_game)
    #options_button = Button("Options", 100, 200, 200, 50, (0, 0, 255), (0, 0, 150), open_options)
    quit_button = Button("Quit", 330, 550, 200, 50, (255, 0, 0), (150, 0, 0), quit_game)
    
    buttons = [start_button, totural_button, quit_button]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(buttons, pygame.mouse.get_pos())
        pygame.mixer.Sound.stop(sound)
        pygame.mixer.Sound.play(sound1)
        screen.fill((0, 0, 0))
        screen.blit(BG2, (0,0))
        for button in buttons:
            draw_button(button)
        pygame.display.flip()
    pygame.quit()

# if __name__ == "__main__":
main_menu()

