import socket
import _thread
import time
import os
import colorama
from Crypto.PublicKey import RSA
import json
messages = []
version = 1

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
versioncontrol = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Aşırı ilkel Mono chat istemcisine hoşgeldiniz.")
print("Dikkat! Bu sürüm 0.01 sürümü olup herhangi bir uçtan uca ya da\nistemci-sunucu arası şifreleme içermemektedir.")
print("Sistem güvenliği oldukça zayıftır. Güncellemeler yavaş yavaş gelecektir.")
print("Sistemi bütün bunları bilerek kullanınız.\n")
print(colorama.Fore.BLUE + "Güncellemeler kontrol ediliyor..." + colorama.Fore.RESET)
connected = False
try:
    versioncontrol.connect(("localhost", 43678))
    connected = True
except:
    print("Güncellemeler kontrol edilemedi.")
if connected:
    srvVer = versioncontrol.recv(16).decode()
    if int(srvVer) > version:
        print(colorama.Fore.GREEN + "Yeni sürüm bulundu. İndirmeye hazırlanılıyor..." + colorama.Fore.RESET)
        versioncontrol.sendall(b"true")
        f = open("mono.py", "wb")
        data = versioncontrol.recv(1024)
        while data:
            f.write(data)
            data = versioncontrol.recv(1024)
        f.close()
        print("Güncelleme indirildi!")
    else:
        print(colorama.Fore.BLUE + "En yeni sürümdesiniz." + colorama.Fore.RESET)

        versioncontrol.sendall(b"false")
        versioncontrol.close() 
if os.path.isfile("./keys.json"):
    print("Önceden oluşturulmuş RSA şifresi bulundu. Oluşturulmayacak.")
else:
    print(colorama.Fore.YELLOW + "Yerel RSA 4096-bit özel anahtarı oluşturuluyor...\nBu biraz sürebilir." + colorama.Fore.RESET)
    key = RSA.generate(4096).export_key().decode()
    f = open("keys.json", "w")
    x = {
        "GeneratedAt": time.time(),
        "PrivateKey": key,
    }
    f.write(json.dumps(x))
    f.close()
    print("Başarıyla oluşturuldu ve kaydedildi.")


print(colorama.Fore.YELLOW + "Sunucuya bağlanılıyor..." + colorama.Fore.RESET)
try:
    s.connect(("localhost", 43677))
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
