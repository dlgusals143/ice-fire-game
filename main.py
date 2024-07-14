import pygame
from main_circle import Main_circle
from main_circle import Orbit
from block import Block
from sub_circle import Sub_circle
import pygame
from pydub import AudioSegment
from pydub.playback import play

# 음악 파일 로드 및 속도 조절 함수

pygame.init()
# 기본 게임판
BLACK = (0, 0, 0)
size = [1915, 1000]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

hp = 4

miss_count = 0

stage = 1

myFont = pygame.font.SysFont(None, 50) #(글자체, 글자크기)
mainFont = pygame.font.SysFont(None, 150) #(글자체, 글자크기)
hudFont = pygame.font.SysFont(None, 70)





# 좌상단에 스테이지 1, 2, 3, 띄우기, 우상단에 남은 목숨 띄우기, 클리어하면 스테이지 넘어가고, 회전 속도 빨라지기

# 4. pygame 무한루프
def runGame():
    
    global hp
    global miss_count
    global stage
    
    done = False
    while not done: 
        # pygame.mixer.music.play()
        
        blocks = []

        isClicked = False

        blockIdx = 1

        
        delayFrame = (55 + stage * 20) * 1.5

        # block_count = int(input("생성할 블록 수를 입력하세요: "))
        for i in range(20):
            new_block = Block(screen, 919 + i * 120, 480, 120, 62)
            if i == 19:
                new_block.color = (0, 255, 0)
            blocks.append(new_block)
        
        orbit = Orbit(screen, 979, 508, 120, 2)
        block = Block(screen, 910, 480, 120, 62)
        sc = Sub_circle(screen, 30, orbit)
        allow = 180
        mc = Main_circle(950, 481, 60)
        
        x_bias = 0
        perfect_text = 0
        miss_text = 0
        is_cleared = False
        
        while not done:
            
            
            
            clock.tick(55 + stage * 20)
            screen.fill(BLACK)
            for event in pygame.event.get():
                # done 변수를 True로 설정하여 게임 루프를 종료합니다.
                if event.type == pygame.QUIT:
                    done=True
                # 이벤트의 타입이 키 다운(KEYDOWN)이고 해당 키가 스페이스 바인지 확인합니다.
                # 누락된 횟수(miss_count)가 생명력(hp)보다 적고 게임이 아직 클리어되지 않았을 경우를 확인합니다.
                # sc.angle과 180 사이의 각도 차이를 계산하여 allow 변수에 저장합니다.
                # sc.angle의 값을 출력합니다.
                # isClicked 변수를 True로 설정합니다.
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and miss_count < hp and not is_cleared:
                    allow = abs(abs(sc.angle - 180) - 180)                    
                    isClicked = True
                # 이벤트의 타입이 키 업(KEYUP)이고 해당 키가 스페이스 바인지 확인합니다.
                # 이벤트의 타입이 키 업(KEYUP)이고 해당 키가 스페이스 바인지 확인합니다.
                # isClicked 변수를 False로 설정하여 사용자가 현재 스페이스 바를 놓았음을 나타냅니다.
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and miss_count < hp and not is_cleared:
                    isClicked = False
                    # 스페이스 바를 눌렀을때의 각도가 51 미만이라면 다음 블록으로 넘어간다
                    if allow < 51:
                        mc.move(blocks[blockIdx])
                        sc.move(blocks[blockIdx])
                        blocks[blockIdx].color = (255, 255, 0)
                        if blockIdx == 19:
                            is_cleared = True
                            hp += 2
                            
                        # blocks의 모든 블록을 순회하면서, block의 x좌표 이동
                        x_bias += 120
                        perfect_text = 20
                        blockIdx = blockIdx + 1
                        
                    else:
                        miss_text = 20
                        miss_count += 1
            
            
            if x_bias >= 0:
                dx = x_bias / 20
                for block in blocks:
                    block.rect_x -= dx
                # main원, sub원의 x좌표를 이동
                mc.x -= dx
                sc.orbit.x -= dx
                x_bias -= dx

            if perfect_text >= 0:
                dc = 255 - int(perfect_text * 12.75)
                myText = myFont.render("Perfect", True, (255 - dc, 255 - dc, 255 - dc))
                screen.blit(myText, (mc.x - 50, mc.y - 50))
                perfect_text -= 1
                
            if miss_text >= 0:
                dc = 255 - int(miss_text * 12.75)
                myText = myFont.render("Miss", True, (255 - dc, 0, 0))
                screen.blit(myText, (sc.x - 40, sc.y - 80))
                miss_text -= 1
            
            # # 사각형
            # pygame.draw.rect(screen, (255, 255, 255), (880, 450, 180, 80))
            # #사각형 윤곽선
            # pygame.draw.rect(screen, (0, 0, 0), (880, 450, 180, 80), 1)
            # #궤도
            # pygame.draw.circle(screen, (255, 255, 255), (970, 490), 200, 2)
            
        
            
            for block in blocks:
                block.draw()
            mc.draw(screen)     
            sc.draw(screen)       
            
            if miss_count >= hp:
                myText = mainFont.render("Game over", True, (255, 0, 255))
                screen.blit(myText, (700, 400))
                
            if is_cleared:
                myText = mainFont.render("Game Clear", True, (0, 255, 0))
                screen.blit(myText, (700, 400))
                
            myText = hudFont.render("Stage " + str(stage), True, (255, 255, 255))
            screen.blit(myText, (0, 0))
                
            myText = hudFont.render("HP : " + str(hp - miss_count), True, (255, 255, 255))
            screen.blit(myText, (1500, 0))
            
            pygame.display.update()
            
            if is_cleared:
                if delayFrame < 0:
                    stage += 1
                    break
                else:
                    delayFrame -= 1
        

runGame()
pygame.quit()

