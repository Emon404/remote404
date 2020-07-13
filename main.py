import socket

def creat_socket():
    try:
        global host
        global port
        global s
        host=socket.gethostname()
        port=1555
        s=socket.socket()
    except socket.error() as msg:
        print("error occured"+ str(msg))


def binding():
    try:
        global host
        global port
        global s
        print("Binding port: "+str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error() as msg:
        print("error occured"+ str(msg)+"\n"+"retrying...")
        binding()

def accept():
    conn,addr=s.accept()
    print("connection established: "+addr[0])
    send(conn)
    conn.close()

def send(conn):
    while True:
        cmd=input()
        if cmd=='quit':
            conn.close()
            s.close()
            
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            print("command sending...")
            cl=str(conn.recv(1024),"utf-8")
            print(cl, end="")


def main():
    creat_socket()
    binding()
    accept()
main()
