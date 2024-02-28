import socket as sock
import zlib
import base64
import time

HOST = "challenge01.root-me.org"
PORT = 52022

def decode_zlib(encoded_data):
    try:
        # Décompression des données zlib
        decoded_data = zlib.decompress(base64.b64decode(encoded_data))
        # Supposons que les données décompressées sont des chaînes UTF-8
        return decoded_data.decode('utf-8') 
    except zlib.error as e:
        print(f"Erreur de décompression zlib : {e}")
        return None

def decode(data):
    line = data.split("\n")
    cipher_text= line[6].split("\'")
    zlib_decoded=decode_zlib(cipher_text[1])
    return zlib_decoded

def decode2(data):
    cipher_text= data.split("\'")
    flag=decode_zlib(cipher_text[1])
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

    while(True):
        d2=decode2(data)
        s.send((str(d2)+"\n").encode(),0)
        time.sleep(1)
        data=s.recv(1024).decode()
        print(data)
        if("RM{" in data):
            break

    s.close()
if __name__== "__main__":
    main()