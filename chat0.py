import socket
import _thread
import time
import os
messages = []
def move (y, x):
    print("\033[%d;%dH" % (y, x))
def handleMessages(s):
    while True:
        d = s.recv(65536).decode()
        os.system("clear")
        messages.append(d)
        for m in messages:
            print(m)
        move(80, 0)
def sender(s):
    while True:
        
        inp = str(input("Mesaj yaz >> "))
        s.sendall(inp.encode())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Aşırı ilkel Mono chat istemcisine hoşgeldiniz.")
print("Dikkat! Bu sürüm 0.01 sürümü olup herhangi bir uçtan uca ya da\nistemci-sunucu arası şifreleme içermemektedir.")
print("Sistem güvenliği oldukça zayıftır. Güncellemeler yavaş yavaş gelecektir.")
print("Sistemi bütün bunları bilerek kullanınız.\n")
s.connect(("213.248.131.78", 43677))
_thread.start_new_thread(handleMessages, (s,))
_thread.start_new_thread(sender, (s,))
while True:
    time.sleep(120)
