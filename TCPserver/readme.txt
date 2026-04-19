#TCPserver简易上位机
import tkinter as tk
from tkinter import ttk
import socket
import threading

# 主窗口
root = tk.Tk()
root.title("简易TCP上位机")
root.geometry("600x400")

# 配置区
ttk.Label(root, text="端口：").place(x=20, y=20)
port_entry = ttk.Entry(root)
port_entry.place(x=60, y=20)
port_entry.insert(0, "8080")

# 日志区
log_text = tk.Text(root)
log_text.place(x=20, y=60, width=550, height=280)

# 全局变量
server_socket = None
run_flag = False

def log(msg):
    """日志打印"""
    log_text.insert(tk.END, msg + "\n")
    log_text.see(tk.END)

def tcp_server_thread(port):
    global server_socket, run_flag
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    run_flag = True
    log(f"TCP服务端已启动，端口:{port}")

    while run_flag:
        try:
            client, addr = server_socket.accept()
            log(f"客户端接入：{addr}")
        except:
            break

def start_server():
    """启动服务端按钮事件"""
    port = int(port_entry.get())
    t = threading.Thread(target=tcp_server_thread, args=(port,))
    t.daemon = True
    t.start()

# 启动按钮
ttk.Button(root, text="启动TCP服务", command=start_server).place(x=200, y=18)

root.mainloop()