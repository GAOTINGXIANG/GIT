import socket
import time 
listenIP="0.0.0.0"
listenPORT=8080
bufSIZE=1024
def show_log(msg):
    print(msg)
def byte_hex(data):
    return " ".join([f"{byte:02X}" for byte in data])
def main():
    server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    try:
        server_sock.bind((listenIP,listenPORT))
        server_sock.listen(5)
        show_log(f"TCP服务端启动成功-端口:{listenPORT}")
        show_log("等待客户端连接")
        while True:
            client_sock,client_addr=server_sock.accept()
            show_log(f"客户端已连接:{client_addr}")
            while True:
                recv_data=client_sock.recv(bufSIZE)
                if not recv_data:
                    show_log(f"客户端断开:{client_addr}")
                    break
                text_data=recv_data.decode("utf-8",errors="ignore")
                hex_data=byte_hex(recv_data)
                show_log(f"收到文本:{text_data}")
                show_log(f"收到HEX{hex_data}\n")
    except KeyboardInterrupt:
        show_log("程序手动退出")
    except Exception as e:
        show_log(f"程序错误:{e}")
    finally:
        server_sock.close()
        show_log("服务器已关闭")
if __name__=="__main__":
    main()