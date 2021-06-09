import socket
import _thread
import time
import os
import colorama
messages = []
def move (y, x):
    print("\033[%d;%dH" % (y, x))
def handleMessages(s):
    while True:
        d = s.recv(65536).decode()
        if not d:
            print(colorama.Fore.RED + "Sunucu bağlantısı koptu." + colorama.Fore.RESET)
            break
        os.system("clear")
        messages.append(d)
        for m in messages:
            print(m)
        #move(80, 0)
def sender(s):
    while True:
        
        inp = str(input("Mesaj yaz >> ")).strip()
        if len(inp) > 0:
            s.sendall(inp.encode())
        else:
            print(colorama.Fore.BLUE + "Boş mesaj gönderilemez." + colorama.Fore.RESET)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Aşırı ilkel Mono chat istemcisine hoşgeldiniz.")
print("Dikkat! Bu sürüm 0.01 sürümü olup herhangi bir uçtan uca ya da\nistemci-sunucu arası şifreleme içermemektedir.")
print("Sistem güvenliği oldukça zayıftır. Güncellemeler yavaş yavaş gelecektir.")
print("Sistemi bütün bunları bilerek kullanınız.\n")
print(colorama.Fore.YELLOW + "Sunucuya bağlanılıyor..." + colorama.Fore.RESET)
try:
    s.connect(("213.248.131.78", 43677))
    print(colorama.Fore.GREEN + "Sunucuya bağlanıldı." + colorama.Fore.RESET)
    time.sleep(3)
except:
    print(colorama.Fore.RED + "Sunucuya bağlanılamadı." + colorama.Fore.RESET)
    exit()
_thread.start_new_thread(handleMessages, (s,))
_thread.start_new_thread(sender, (s,))
os.system("clear")
while True:
    time.sleep(120)
