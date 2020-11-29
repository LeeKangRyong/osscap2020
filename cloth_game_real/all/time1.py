
import pygame
import random

pygame.init()

total_time = 4
start_ticks = pygame.time.get_ticks()
test = [1,3,5,7,9]
def tested():
    print(randint(1,100))
    

running = True
while running:
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
    pygame.time.delay(1000)
    timer = print("Time : {}".format(int(total_time - elapsed_time)))
    # screen.blit(timer, (10, 10))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                    print(tested())
                        
                elif event.key == pygame.K_RIGHT:
                    print(tested())
                    # elif event.key == pygame.K_SPACE: # 무기 발사
                        
                        

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0



    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

   
        

