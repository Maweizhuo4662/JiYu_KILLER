import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as msgbox
import ctypes
import threading
import fnmatch
import os


def KillXSJFGLZS(n):
    try:
        def get_exe_files():
            # 获取 C 盘下所有以's'开头后面一堆数字的文件夹
            folders = [folder for folder in os.listdir('C:') if fnmatch(folder, 's*')]

            exe_files = []

            for folder in folders:
                # 进入每个符合条件的文件夹
                folder_path = os.path.join('C:', folder)
                for file in os.listdir(folder_path):
                    # 过滤出以'.exe'结尾的文件
                    if fnmatch(file, '.exe'):
                        exe_files.append(os.path.join(folder_path, file))
            return exe_files
        exe_files = get_exe_files()
        for i in range(len(exe_files)):
            os.system("TaskK.exe /f /im "+exe_files[i])
        os.system("shutdown -a")
        if n != 114514:
            msgbox.showinfo("提示", "已经调用TaskK.exe(taskkill)关闭了学生机房管理助手")
    except:
        msgbox.showinfo("提示", "学生机房管理助手失败!可能是文件缺失")

def AboutBox():
    msgbox.showinfo("关于", " 作者:Maweizhuo4662 马维卓 QQ:3041185240\n 第一版是使用WindowsAPI做的图形界面 但是实在太丑了\n 第二版是使用Qt做的 但是打包出来体积21MB \n\n 随意才有了这个版本 使用Python的Tkinter库制作 算是一个平衡了\n 真的要夸一句VisualStudioCode的自动填充太好用了")

def jieCInternet():
    try:
        os.system("TaskK.exe /f /t /im GATESRV.exe")
        os.system("TaskK.exe /f /t /im MasterHelper.exe")
        os.system("sc stop TDNetFilter")
        msgbox.showinfo("提示", "已经调用TaskK.exe和sc命令解除了网络限制")
    except:
        msgbox.showinfo("提示", "网络限制解除失败!可能是文件缺失")

def jieCK():
    try:
        os.system("pssuspend.exe -accepteula StudentMain")
        os.system("explorer.exe shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}")
        os.system("explorer.exe shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}")
        msgbox.showinfo("运行结束", "已经调用同路径下的pssuspend.exe执行了解除控屏命令!")
    except:
        msgbox.showinfo("运行结束", "解除控屏命令执行失败!可能是文件缺失")

def huiFK():
    try:
        os.system("pssuspend.exe -accepteula StudentMain -r")
        os.system("start \"C:\Program Files (x86)\Mythware\极域课堂管理系统软件V6.0 2016 豪华版\MasterHelper.exe\"")
        os.system("start \"C:\Program Files (x86)\Mythware\极域课堂管理系统软件V6.0 2016 豪华版\GATESRV.exe\"")
        msgbox.showinfo("运行结束", "已经调用同路径下的pssuspend.exe执行了恢复控屏命令!")
    except:
        msgbox.showinfo("运行结束", "恢复控屏命令执行失败!可能是文件缺失")

def remoteCommand():
    subwindow = tk.Tk()
    subwindow.geometry("525x150")
    subwindow.title("远程执行 !!!BETA!!!     Psexec远程执行+vbs弹窗做的")
    computerName = tk.StringVar()
    message = tk.StringVar()
    title = tk.StringVar()
    command = tk.StringVar()
    LabelI = ttk.Label(subwindow, text="↓要发送消息/执行命令的计算机名↙", foreground="red")
    LabelM = ttk.Label(subwindow, text="↓发送的消息↓", foreground="green")
    LabelT = ttk.Label(subwindow, text="↓发送消息的标题↓", foreground="green")
    LabelS = ttk.Label(subwindow, text="示例 如此排列 \n老师电脑填写TEACHER\n       讲台     教室门\nF1 E1 D1 C1 B1 A1\nF2 E2 D2 C2 B2 A2\nF3 E3 D3 C3 B3 A3\nF4 E4 D4 C4 B4 A4\n      ......更多......", foreground="orange")
    LabelS2 = ttk.Label(subwindow, text="↑使用\"& vbCrLf &\"换行↑", foreground="green")
    LabelC = ttk.Label(subwindow, text="↓远程执行CMD命令↓", foreground="blue")
    LabelC2 = ttk.Label(subwindow, text="↑例如shutdown -p关机↑", foreground="blue")
    
    EntryI = ttk.Entry(subwindow, textvariable=computerName)
    EntryM = ttk.Entry(subwindow, textvariable=message)
    EntryT = ttk.Entry(subwindow, textvariable=title)
    EntryC = ttk.Entry(subwindow, textvariable=command)

    def runCommand():
        try:
            psexec = "PsExec.exe -accepteula \\\\"+EntryI.get()+"-u DELL -p \"\" cmd /c "+EntryC.get()
            os.system(psexec)
            msgbox.showinfo("运行结束", "远程执行成功!")
        except:
            msgbox.showinfo("运行结束", "  远程命令执行失败!请仔细检查计算机名和执行的命令")
    def SEND():
        try:
            psexec = "PsExec.exe -accepteula \\\\"+EntryI.get()+" -u Administrator -p \"ASDFGHJKL;'\" cmd /c echo MsgBox "+EntryM.get()+" "+EntryT.get()+" :: WScript.Quit > temp.vbs & cscript //nologo temp.vbs & del temp.vbs"
            os.system(psexec)
            msgbox.showinfo("运行结束", "消息发送成功!")
        except:
            msgbox.showinfo("运行结束", "  发送消息命令执行失败!请仔细检查计算机名和发送的消息 换行连\"\"也需要带上")
    ButtonF = ttk.Button(subwindow, text="           发送消息           ", command=SEND)
    ButtonR = ttk.Button(subwindow, text="           执行命令           ", command=runCommand)
    LabelS.place(x=375, y=0)
    LabelS2.place(x=10, y=100)
    LabelI.place(x=175, y=5)
    LabelM.place(x=10, y=55)
    LabelT.place(x=10, y=5)
    LabelC.place(x=175, y=55)
    LabelC2.place(x=175, y=100)
    EntryI.place(x=175, y=25)
    EntryM.place(x=10, y=75)
    EntryT.place(x=10, y=25)
    EntryC.place(x=175, y=75)
    ButtonF.place(x=10, y=120)
    ButtonR.place(x=175, y=120)

window = tk.Tk()
window.wm_attributes("-topmost", 1)
window.geometry("275x115")
window.title("Tk+PSTool+tkill做的")

label = ttk.Label(window, text="PageUp解控屏 PageDown恢复控屏")
label.place(x=35, y=0)

button = ttk.Button(window, text="         解除控屏         ", command=jieCK)

button.place(x=15, y=20)
button1 = ttk.Button(window, text="         恢复控屏         ", command=huiFK)
button1.place(x=15, y=50)
button2 = ttk.Button(window, text="关闭学生机房管理助手", command=KillXSJFGLZS)
button2.place(x=15, y=80)
buttonA = ttk.Button(window, text="         关于         ", command=AboutBox)
buttonA.place(x=155, y=80)
buttonI = ttk.Button(window, text="   解除网络限制   ", command=jieCInternet)
buttonI.place(x=155, y=50)
buttonM = ttk.Button(window, text="   远程命令/消息  ", command=remoteCommand)
buttonM.place(x=155, y=20)

GetAsyncKeyState = ctypes.windll.user32.GetAsyncKeyState
def check_key_pressed(key):
    return GetAsyncKeyState(key) & 0x8000

def while_loop():
    while True:
        if check_key_pressed(0x21):
            jieCK()
        elif check_key_pressed(0x22):
            huiFK()
        else:
            pass
        
threading.Thread(target=while_loop).start()

window.mainloop()
