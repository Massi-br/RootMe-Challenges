import socket as sock
import re
import math

HOST = "challenge01.root-me.org"
PORT = 52002

def squareRoot(data):
    line = data.split("\n")
    numbers =re.findall(r'\d+',line[6])
    r_carre = math.sqrt(int(numbers[0])) 
    rslt = r_carre *(int(numbers[1]))
    rounded_result=round(rslt,2)
    return rounded_result


def main():
    s=sock.socket(sock.AF_INET,type=sock.SOCK_STREAM)
    s.connect((HOST,PORT))
    print("connected")

    data =s.recv(1024).decode()
    res = squareRoot(data)

    s.send((str(res)+"\n").encode(),0)

    data =s.recv(1024).decode()
    print(data)

    s.close()
if __name__== "__main__":
    main()