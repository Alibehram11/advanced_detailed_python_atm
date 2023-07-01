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
****** Welcome to ATM ******

press "a" to exit

Press "1" to deposit

Press "2" to withdraw money

Press "3" to see your current balance

Press "4" to trade with dollars

Press "5" to trade with euro
""")




hesap = 1000
dolarhesap = 100
eurohesap = 100
while True:
    işlem = str(input("Enter the number you want to trade:"))
    if işlem == "a":
        print("\033[1;34;40mthe program is ending.......\033[0m")
        time.sleep(0.5)
        break
    elif işlem == "1":
        yatırma = int(input("How much will you deposit into your account:"))
        hesap=hesap+yatırma
        print(f"\033[1;34;40mto your account {yatırma} money has been deposited \033[0m")
    elif işlem == "2":
        çekme = int(input("Enter quantity:"))
        if hesap-çekme<0:
            print("\033[1;34;40minsufficient balance\033[0m")
            continue


        else:
            hesap=hesap-çekme
            print(f"\033[1;34;40min your account {çekme} lira is missing\033[0m")
    elif işlem == "3":
        print(hesap,"TL")
        print(dolarhesap,"Dolar")
        print(eurohesap,"Euro")
    ########
    elif işlem == "4":
        print("\033[1;34;40mWhat is the transaction you want to do with dollars?\033[0m")
        dolar = str(input("Press (1) to convert the money in your account to dollars, press (2) for other operations:"))
        if dolar == "1":
            çevirme = int(input("How many liras in your account do you want to convert to dollars:")) 
            if hesap-çevirme<0 :
                print("\033[1;34;40insufficient balance\033[0m")  
            else:
                hesap=hesap-çevirme
                a=çevirme/dolar_kuru    
                print(f"{dolarhesap+a}you have dollars")
                continue



        if dolar == "2":
           kur = str(input("Press (1) to find out how much the dollar is in TL, and press (2) to convert the dollar in your account to TL:"))

        if kur == "1":
            print("1TL=",dolar_kuru)
        if kur == "2":
            tl = int(input("How many dollars in your account would you like to convert to TL:"))
            if dolar_kuru-tl<0:
                print("\033[1;34;40minsufficient balance \033[0m")
                continue
            else:
               dolarhesap=dolarhesap-tl
               hesap=tl*dolar_kuru
               print("\033[1;34;40mthe transaction took place \033[0m")
    ########
    elif işlem == "5":
        print("\033[1;34;40mWhat is the transaction you want to make with euro? \033[0m")
        euro = str(input("Press (1) to convert the money in your account into euros, press (2) for other transactions:"))
        if euro == "1":
            çevirme1 = int(input("How many liras in your account do you want to convert into euros:")) 
            if hesap-çevirme1<0 :
                print("\033[1;34;40minsufficient balance \033[0m")  
            else:
                hesap=hesap-çevirme1
                a1=çevirme1/euro_kuru   
                print(f"{eurohesap+a1}you have euro")
                continue



        if euro == "2":
           kur1 = str(input("Press (1) to find out how many TL in euros, and (2) to convert euros in your account to TL:"))

        if kur1 == "1":
            print("1TL=",euro_kuru)
        if kur1 == "2":
            tl1 = int(input("How many euros in your account would you like to convert to TL:"))
            if eurohesap-tl1<0:
                print("\033[1;34;40minsufficient balance \033[0m")
                continue
            else:
               eurohesap=eurohesap-tl1
               hesap=tl1*euro_kuru
               print("\033[1;34;40myour transaction has been completed \033[0m")
    else:
        print("\033[1;31;40mYou entered an invalid transaction \033[0m")
        
 


