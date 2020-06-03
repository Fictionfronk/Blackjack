import socket
from _thread import *
import random

# game screen
screen_width = 1280
screen_height = 720

host = "127.0.0.1"
port = 2475

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((host, port))
except socket.error as e:
    print(e)

server.listen(2)
print("waiting")

currentplayer = 0



cards = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
         '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
         '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
         '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS', ]

random.shuffle(cards)

dealer = []
player = []

player.append(cards.pop())
dealer.append(cards.pop())
player.append(cards.pop())
dealer.append(cards.pop())

print(player)
print(dealer)


def thread_client(conn, currentplayer):
    conn.send(str.encode(str(player)))
    while True:
        try:
            data = conn.recv(2048).decode()

            if not data:
                print('disconnected')
                break
            else:
                if data == 'dealer':
                    reply = str(dealer)
                elif data == 'draw':
                    reply = cards.pop()
                else:
                    reply = 'Game Ended'
                print("received: ", data)
                print("sending: ", reply)
            conn.sendall(str.encode(reply))
        except socket.error as e:
            print(e)
            break

    print('lost connection')
    conn.close()


while True:
    conn, addr = server.accept()
    print("connected => ", addr)

    start_new_thread(thread_client, (conn, currentplayer))
    currentplayer += 1
