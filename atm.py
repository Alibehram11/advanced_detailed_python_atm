import sys,time
import requests


def get_dolar_kuru():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    dolar_kuru = data["rates"]["TRY"]
    return dolar_kuru
dolar_kuru = get_dolar_kuru()

#################

def get_euro_exchange_rate():
    url = 'https://api.exchangerate-api.com/v4/latest/EUR'
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['rates']['TRY']  # TRY (Türk Lirası) cinsinden Euro kurunu alıyoruz
    return exchange_rate

euro_kuru = get_euro_exchange_rate()



print("""
****** Atm ye Hoşgeldiniz ******

çıkış yapmak için "a" ya basınız 

Para yatırmak için "1" basınınz

Para çekmek için "2" ye basınız

Mevcut bakiyenizi görmek için "3" e basınız 

dolar ile işlem yapmak için "4" e basınız

euro ile işlem yapmak için "5" e basınız 
""")




hesap = 1000
dolarhesap = 100
eurohesap = 100
while True:
    işlem = str(input("işlem yapmak istediğiniz numarayı giriniz:"))
    if işlem == "a":
        print("\033[1;34;40mProgram bitiriliyor....... \033[0m")
        time.sleep(0.5)
        break
    elif işlem == "1":
        yatırma = int(input("Hesabınıza kaç lira yatıracaksınız:"))
        hesap=hesap+yatırma
        print(f"\033[1;34;40mHesabınıza {yatırma} lira para yatırılmıştır \033[0m")
    elif işlem == "2":
        çekme = int(input("Miktar giriniz:"))
        if hesap-çekme<0:
            print("\033[1;34;40myetersiz bakiye \033[0m")
            continue


        else:
            hesap=hesap-çekme
            print(f"\033[1;34;40mHesabınızda {çekme} lira eksilmiştir \033[0m")
    elif işlem == "3":
        print(hesap,"TL")
        print(dolarhesap,"Dolar")
        print(eurohesap,"Euro")
    ########
    elif işlem == "4":
        print("\033[1;34;40mdolar ile yapmak istediğiniz işlem nedir? \033[0m")
        dolar = str(input("hesabınızdaki parayı dolara çevirmek için  (1)e basınız başka işlemler için (2) ye basınız:"))
        if dolar == "1":
            çevirme = int(input("hesabınızdaki kaç lirayı dolara çevirmek istiyorsunuz:")) 
            if hesap-çevirme<0 :
                print("\033[1;34;40yetersiz bakiye \033[0m")  
            else:
                hesap=hesap-çevirme
                a=çevirme/dolar_kuru    
                print(f"{dolarhesap+a}dolarınız var")
                continue



        if dolar == "2":
           kur = str(input("Doların kaç tl olduğunu öğrenmek için (1)e hesabınızdaki doları  tl ye çevirmek için (2)ye basınız:"))

        if kur == "1":
            print("1TL=",dolar_kuru)
        if kur == "2":
            tl = int(input("hesabınızdaki kaç doları TL'ye çevirmek istersiniz:"))
            if dolar_kuru-tl<0:
                print("\033[1;34;40myetersiz bakiye \033[0m")
                continue
            else:
               dolarhesap=dolarhesap-tl
               hesap=tl*dolar_kuru
               print("\033[1;34;40mişlem gerçekleşti \033[0m")
    ########
    elif işlem == "5":
        print("\033[1;34;40meuro ile yapmak istediğiniz işlem nedir? \033[0m")
        euro = str(input("hesabınızdaki parayı euro çevirmek için  (1)e basınız başka işlemler için (2) ye basınız:"))
        if euro == "1":
            çevirme1 = int(input("hesabınızdaki kaç lirayı euro çevirmek istiyorsunuz:")) 
            if hesap-çevirme1<0 :
                print("\033[1;34;40myetersiz bakiye \033[0m")  
            else:
                hesap=hesap-çevirme1
                a1=çevirme1/euro_kuru   
                print(f"{eurohesap+a1}euronuz var")
                continue



        if euro == "2":
           kur1 = str(input("Euro kaç tl olduğunu öğrenmek için (1)e hesabınızdaki euro yu  tl ye çevirmek için (2)ye basınız:"))

        if kur1 == "1":
            print("1TL=",euro_kuru)
        if kur1 == "2":
            tl1 = int(input("hesabınızdaki kaç euro TL'ye çevirmek istersiniz:"))
            if eurohesap-tl1<0:
                print("\033[1;34;40myetersiz bakiye \033[0m")
                continue
            else:
               eurohesap=eurohesap-tl1
               hesap=tl1*euro_kuru
               print("\033[1;34;40mişleminiz gerçekleşti \033[0m")
    else:
        print("\033[1;31;40mGeçersiz bir işlem girdiniz \033[0m")
        
 


