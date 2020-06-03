import pygame
import sys
import Network
import Player
import Button
import Calculate

pygame.init()

screen_width = 1280
screen_height = 720

# colors
black = (0, 0, 0)
white = (255, 255, 255)
light_grey = (200, 200, 200)
red = (255, 51, 51)
orange = (255, 153, 51)
yellow = (255, 255, 51)
green = (153, 255, 51)

# cards
deck = 'Images/red_back.png'

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Black Jack')
clock = pygame.time.Clock()
bg_color = pygame.Color('grey12')
font = pygame.font.SysFont('comicsans', 60)
deckImg = pygame.transform.scale(pygame.image.load(deck), (150, 200))


def deck(x, y):
    win.blit(deckImg, (x, y))


def redrawWindow(win, p1, p2, b1, b2, result):
    global turn, stand, player, dealer
    win.fill(bg_color)
    p2.card(win, 50, 50, 0)
    if stand:
        p2.card(win, 250, 50, 1)
    else:
        deck(250, 50)
    p1.card(win, 50, 400, 0)
    p1.card(win, 250, 400, 1)
    b1.draw(win, black)
    b2.draw(win, black)
    if len(player) > 2:
        p1.card(win, 450, 400, len(player) - 1)
    if len(dealer) > 2:
        p2.card(win, 450, 50, len(dealer) - 1)
    deck(900, screen_height / 2 - 125)
    if turn % 2 == 0:
        turn_text = font.render('Your turn', 1, red)
        win.blit(turn_text, (50, 300))
    else:
        turn_text = font.render('Dealer turn', 1, red)
        win.blit(turn_text, (50, 300))
    if stand:
        text = font.render(result.handcal(), 1, red)
        win.blit(text, (900, screen_height / 2 - 300))
    pygame.display.update()


def selectRule(win):
    win.fill(bg_color)


turn = 0
stand = False
player = []
dealer = []


def main():
    global turn, stand, player, dealer
    run = True
    n = Network.Network()
    player = eval(n.getPlayer())
    print(type(player))
    p1 = Player.Player(player)
    dealer = eval(n.send('dealer'))
    print(type(dealer))
    p2 = Player.Player(dealer)
    hit_button = Button.Button(light_grey, 50, 625, 200, 70, 'Hit')
    stand_button = Button.Button(light_grey, 300, 625, 200, 70, 'Stand')
    result = Calculate.Calculate(dealer, player)
    while run:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hit_button.isOver(pos):
                    if turn % 2 == 0:
                        player.append(n.send('draw'))
                    turn += 1
                if turn % 2 == 1 and not result.handcheck():
                    dealer.append(n.send('draw'))
                    turn += 1
                if stand_button.isOver(pos):
                    stand = True
                    turn += 1
                    if stand:
                        n.send(result.handcal())

        redrawWindow(win, p1, p2, hit_button, stand_button, result)
        clock.tick(60)


main()
