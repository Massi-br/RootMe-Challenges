import socket as sock
import time
import numpy as np
import re

HOST = "challenge01.root-me.org"
PORT = 	52018


def solve_quadratic(a, b, c, d):
    # Calcul du discriminant
    discriminant = b**2 - 4*a*(c - d)
    
    # Cas où il n'y a pas de racine réelle
    if discriminant < 0:
        return "Not possible"
    # Cas où il y a une seule racine réelle
    elif discriminant == 0:
        root = -b / (2*a)
        return "x1: " + str(round(root, 3)) + " ; x2: " + str(round(root, 3))
    # Cas où il y a deux racines réelles
    else:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        return "x1: " + str(round(root1, 3)) + " ; x2: " + str(round(root2, 3))

def resolv(data):
    eq1 = data.split("please")[1]
    eq2 = eq1.split()
    coeff1 = re.search(r'([-+]?\d+\.\d+|[-+]?\d+)', eq2[1]).group(0)
    coeff2 = re.search(r'([-+]?\d+\.\d+|[-+]?\d+)', eq2[3]).group(0)
    coeff3 = eq2[5]
    coeff4 = eq2[7]
    signe1 = eq2[2]
    signe2 = eq2[4]
    coeff22 = signe1 + coeff2
    coeff33 = signe2 + coeff3

    res = solve_quadratic(int(coeff1), int(coeff22), int(coeff33), int(coeff4))
    return res



def main():
    s = sock.socket(sock.AF_INET, type=sock.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("[+] connected to server")
    print("[+] receiving data ")

    data = s.recv(1024).decode()
    res=resolv(data)
    print(res,"\n")
    
    print("[+] sending data ")
    s.send((str(res) + "\n").encode(), 0)

    for i in range(25):
        print(f"[+] receiving data (Equation {i+1}/25)")
        data = s.recv(1024).decode()
        print(data)
        res = resolv(data)
        print(res)
        print(f"[+] sending data (Equation {i+1}/25)")
        s.send((str(res) + "\n").encode(), 0)
        time.sleep(1)
    s.close()

    
if __name__== "__main__":
    main()