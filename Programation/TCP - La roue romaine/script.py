import socket as sock
import codecs


HOST = "challenge01.root-me.org"
PORT = 52021

def decode(data):
    line = data.split("\n")
    cipher_text= line[6].split("\'")
    flag = codecs.decode(cipher_text[1],'rot_13')
    return flag


def main():
    s=sock.socket(sock.AF_INET,type=sock.SOCK_STREAM)
    s.connect((HOST,PORT))
    print("[+] connected to server")
    print("[+] receiving data ")
    data =s.recv(1024).decode()


    res = decode(data=data)
    print("[+] sending data ")
    s.send((str(res)+"\n").encode(),0)
    print("[+] receiving data ")
    data =s.recv(1024).decode()
    print(data)

    s.close()
if __name__== "__main__":
    main()