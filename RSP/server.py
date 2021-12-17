import socket
from _thread import *
import pickle
from game import Game

# server = socket.gethostbyname(socket.getfqdn())

server = "localhost"
print(server)

port = 55555

s = socket.socket()

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(1)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset_went()
                    elif data != "get":
                        game.play(p, data)
                        print('player', p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except Exception as exception:
            print(exception)
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except Exception as exception:
        print(exception)
        pass
    idCount -= 1
    conn.close()


while True:
    conn_, addr_ = s.accept()
    print("Connected to:", addr_)

    idCount += 1
    p = 0
    gameId_ = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId_] = Game(gameId_)
        print("Creating a new game...")
    else:
        games[gameId_].ready = True
        p = 1

    start_new_thread(threaded_client, (conn_, p, gameId_))
