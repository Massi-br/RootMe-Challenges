import socket as sock
import numpy as np

HOST = "challenge01.root-me.org"
PORT = 	52018


def solve_quadratic(a, b, c, d):
 # Calcul du discriminant
    discriminant = b**2 - 4*a*(c - d)
    
    # Cas où il n'y a pas de racine réelle
    if discriminant < 0:
        print("Not possible")
    # Cas où il y a une seule racine réelle
    elif discriminant == 0:
        root = -b / (2*a)
        print("x:", round(root, 3))
    # Cas où il y a deux racines réelles
    else:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        print("x1:", round(root1, 3), "; x2:", round(root2, 3))



def main():
    s=sock.socket(sock.AF_INET,type=sock.SOCK_STREAM)
    s.connect((HOST,PORT))
    print("[+] connected to server")
    print("[+] receiving data ")
    data =s.recv(1024).decode()

    # res =decode(data=data)
    # print("[+] sending data ")
    # s.send((str(res)+"\n").encode(),0)
    # print("[+] receiving data ")
    # data =s.recv(1024).decode()
    
    print(data)

    s.close()
    
if __name__== "__main__":
    main()