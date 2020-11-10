import pygame
import random
import math
pygame.init()
#create a screen
screen = pygame.display.set_mode((800,600))
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
font2 = pygame.font.Font('freesansbold.ttf',64)


textX =10
textY = 10

def show_score(x,y):
	score1 = font.render("Score :"+str(score),True,(255,255,255))
	screen.blit(score1,(x,y))
def game_over_text():
	game_over = font2.render("GAME OVER", True,(255,255,255))
	screen.blit(game_over,(200,250))

	
#Title and icon

pygame.display.set_caption("space invaders")
icon = pygame.image.load("7.bmp")
pygame.display.set_icon(icon)
#background_image
backImg = pygame.image.load("155.jpg")
new_img = pygame.transform.scale(backImg,(800,600))
#bullet
bullet = pygame.image.load("bullet.png")
bullet = pygame.transform.scale(bullet,(25,25))
bulletx=0
bullety = 480
bullety_change = 10
bullet_state = "ready"

#player
playerImg = pygame.image.load("space-invaders.png")
playerx = 370
playery = 480
playerx_change = 0
playery_change = 0

#enemy
enemyImg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enimies = 5
for i in range(num_of_enimies):
	enemyImg.append(pygame.image.load("ufo.png"))
	enemyx.append(random.randint(0,736))
	enemyy.append(0)
	enemyx_change.append(3)
	enemyy_change.append(0)

def player(x,y):
	screen.blit(playerImg,(x,y))
def enemy(x,y,i):
	screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
	global bullet_state
	bullet_state="fire"
	screen.blit(bullet,(x+24,y-10))
#collision
def iscollision(w,x,y,z):
	distance = math.sqrt((math.pow(w-y,2))+(math.pow(x-z,2)))
	if distance<=35:
		return True
	else:
		return False
#collision of spaceship
def tocollision(w,x,y,z):
	distance = math.sqrt((math.pow(w-y,2))+(math.pow(x-z,2)))
	if distance<=35:
		return True
	else:
		return False 
#Game loop 
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerx_change = -5
			if event.key == pygame.K_RIGHT:
				playerx_change = +5
			if event.key == pygame.K_UP:
				playery_change = -5
			if event.key == pygame.K_DOWN:
				playery_change = +5
			if event.key == pygame.K_SPACE:
				bulletx=playerx
				bullety=playery
				fire_bullet(bulletx,bullety)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerx_change = 0
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				playery_change = 0
	screen.blit(new_img,(0,0))
	for i in range(num_of_enimies):
		if enemyy[i]>440:
			for j in range(num_of_enimies):
				enemyy[j]=2000
			game_over_text()
			break
		enemyx[i] = enemyx[i]  + enemyx_change[i] 
		if enemyx[i]  <= 0 :
			enemyx_change[i]  = 3
			enemyy[i]  = enemyy[i] +100
		elif enemyx[i] >=736:
			enemyx_change[i]  = -3
			enemyy[i]  = enemyy[i] +100
		collision = iscollision(bulletx,bullety,enemyx[i],enemyy[i])
		if collision:
			bullety = 480
			bullet_state = "ready"
			enemyx[i] = random.randint(0,736)
			enemyy[i] = 0
			score = score+1
			
		enemy(enemyx[i],enemyy[i],i)
	playerx = playerx+playerx_change
	playery = playery+playery_change
	if playerx <= 0 :
		playerx = 0
	if playerx >= 740:
		playerx = 740
	if playery <= 120:
		playery = 120
	if playery >= 480:
		playery = 480
	if bullety<=0:
		bullety = 480
		bullet_state = "ready"
	#RGB = red , Green , Blue
	
	if bullet_state == "fire":
		fire_bullet(bulletx,bullety)
		bullety=bullety-6

	
		

		
	player(playerx,playery)
	show_score(textX,textY)
	pygame.display.update()
