import requests
from bs4 import BeautifulSoup
import time
URL = "http://challenge01.root-me.org/programmation/ch1/"
URL_RES ="http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="

def calculate_sequence(n, v1, v2, v3, v4):
    result = v4
    for i in range(0, n ):
        result = v1 + result + (i * v3) if v2 == "+" else v1 + result - (i * v3)
    return result


def parseCookie(Cookie):
    cookie =Cookie.split("PHPSESSID=")[1].split(':')[0]
    return cookie

if __name__=='__main__':
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.get_text())
    data_from_soup = soup.get_text().split("\n")
    print(data_from_soup)



    n_term=data_from_soup[2].split("U")[1].split("You")
    n = n_term[0]
   
    term1=data_from_soup[0]
    term2=data_from_soup[1]
    data_from_term_1=term1.split(" ")

    var1=data_from_term_1[3]
    var2=data_from_term_1[7]
    var3=data_from_term_1[11]

    data_from_term_2=term2.split(" ")
    var4=data_from_term_2[2]

    # Mesurer le temps d'exécution
    start_time = time.time()

    #print(calculate_sequence(int(n), int(var1), var2, int(var3), int(var4)))
    res=calculate_sequence(int(n), int(var1), var2, int(var3), int(var4))
    # Temps écoulé
    elapsed_time = time.time() - start_time

    # Afficher le résultat et le temps écoulé
    print("Résultat:", res)
    print("Temps écoulé:", elapsed_time, "secondes")

    # Si le temps écoulé est inférieur à 2 secondes, envoyer le résultat via la requête HTTP GET
    if elapsed_time < 2:
        url = URL_RES +str(res)
        cookie =parseCookie(response.headers['Set-Cookie'])
        headers={
            'cookie':'PHPSESSID=' + cookie +';'
        }
        response = requests.get(url , headers=headers)
        
        print("Réponse du serveur:", response.text)
    else:
        print("Le temps d'exécution est supérieur à 2 secondes.")
        print(response.text)



