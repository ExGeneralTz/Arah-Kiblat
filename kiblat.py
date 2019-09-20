# Author : Satria Andhika Adi Saputra
# Codename : ./ExGeneralTz
# Lang = Python3

# Mengimport Modul Yang Digunakan
import os
import requests
import sys
import time
import random

#Warna-Banner
B='\033[34;1m'
G='\033[32;1m'
P='\033[35;1m'
C='\033[36;1m'
R='\033[31;1m'
W='\033[37;1m'
Y='\033[33;1m'

#Banner-Program
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

def tampilan():
    os.system('clear')
    mengetik('#####################################')
    mengetik('#### </> \033[31;1mProgram Information \033[37;1m</> ####')
    mengetik('#####################################')
    mengetik('- Author       : ./ExGeneralTz')
    mengetik('- Name Program : Informasi Arah Kiblat')
    mengetik('- Created Date : 15-09-2019')
    print('')

# Fungsi Def Ini Adalah Buat Mengambil Data Api
def kiblat():
    kota = input('Masukan nama kota: ')
    os.system('clear')
    r = requests.get('https://time.siswadi.com/qibla/{}'.format(kota))
    print (R+'---------------------------------------------')
    print (W+'     Informasi Kiblat Dari Kota {}'.format(kota))
    print (R+'---------------------------------------------')
    print (W+'Kabah   : ',r.json()["data"]["kabah"])
    print ('Derajat   : ',r.json()["data"]["derajat"])
    print ('Kompas    : ',r.json()["data"]["kompas"])
    print ('Latitude  : ',r.json()["location"]["latitude"])
    print ('Longitude : ',r.json()["location"]["longitude"])
    print ('Lokasi    : ',r.json()["location"]["address"])

try:
    if __name__ == '__main__':
        tampilan()
        kiblat()
except KeyboardInterrupt():
    print('Anda telah keluar dari program :)')
