import tkinter as tk
import pyautogui as pag
import os
os.system('pip install -r requirements.txt')

#tkinter
root = tk.Tk()
root.title("hacomtaja-macro")
root.geometry("300x100")
root.minsize(300,100)
root.maxsize(300,100)
root.iconbitmap('icon.ico')
frame = tk.Frame(root)
frame.pack(pady=20)

status_label = tk.Label(root, text="ro1004bin", font=("Arial", 12))
status_label.pack(pady=10)

def start():
    status_label.config(text="Start")
    root.update()

    root.after(3000, macro)
    status_label.config(text="Waiting 3sec...")
    root.update()


#Macro
pag.PAUSE = 0.0001
def macro():
    #애국가
    status_label.config(text="macroing..")
    root.update()
    pag.press('d') #ㅇ
    pag.press('o') #ㅐ
    pag.press('r') #ㄱ
    pag.press('n') #ㅜ
    pag.press('r') #ㄱ
    pag.press('r') #ㄱ
    pag.press('k') #ㅏ
    pag.press('enter')

    #동해물과 백두산이
    pag.press('1')
    pag.press('.')
    pag.press('space')
    pag.press('e') #ㄷ
    pag.press('h') #ㅗ
    pag.press('d') #ㅇ
    pag.press('g') #ㅎ
    pag.press('o') #ㅐ
    pag.press('a') #ㅁ
    pag.press('n') #ㅜ
    pag.press('f') #ㄹ
    pag.press('r') #ㄱ
    pag.press('h') #ㅗ
    pag.press('k') #ㅏ
    pag.press('space') #띄어쓰기
    pag.press('q') #ㅂ
    pag.press('o') #ㅐ
    pag.press('r') #ㄱ
    pag.press('e') #ㄷ
    pag.press('n') #ㅜ
    pag.press('t') #ㅅ
    pag.press('k') #ㅏ
    pag.press('s') #ㄴ
    pag.press('d') #ㅇ
    pag.press('l') #ㅣ
    pag.press('space') #띄어쓰기

    #마르고 닳도록
    pag.press('a') #ㅁ
    pag.press('k') #ㅏ
    pag.press('f') #ㄹ
    pag.press('m') #ㅡ
    pag.press('r') #ㄱ
    pag.press('h') #ㅗ
    pag.press('space') #띄어쓰기
    pag.press('e') #ㄷ
    pag.press('k') #ㅏ
    pag.press('f') #ㄹ
    pag.press('g') #ㅎ
    pag.press('e') #ㄷ
    pag.press('h') #ㅗ
    pag.press('f') #ㄹ
    pag.press('h') #ㅗ
    pag.press('r') #ㄱ
    pag.press('enter')
    #하느님이 보우하사
    pag.press('g') #ㅎ
    pag.press('k') #ㅏ
    pag.press('s') #ㄴ
    pag.press('m') #ㅡ
    pag.press('s') #ㄴ
    pag.press('l') #ㅣ
    pag.press('a') #ㅁ
    pag.press('d') #ㅇ
    pag.press('l') #ㅣ
    pag.press('space') #띄어쓰기
    pag.press('q') #ㅂ
    pag.press('h') #ㅗ
    pag.press('d') #ㅇ
    pag.press('n') #ㅜ
    pag.press('g') #ㅎ
    pag.press('k') #ㅏ
    pag.press('t') #ㅅ
    pag.press('k') #ㅏ
    pag.press('space') #띄어쓰기
    #우리나라 만세
    pag.press('d') #ㅇ
    pag.press('n') #ㅜ
    pag.press('f') #ㄹ
    pag.press('l') #ㅣ
    pag.press('s') #ㄴ
    pag.press('k') #ㅏ
    pag.press('f') #ㄹ
    pag.press('k') #ㅏ
    pag.press('space') #띄어쓰기
    pag.press('a') #ㅁ
    pag.press('k') #ㅏ
    pag.press('s') #ㄴ
    pag.press('t') #ㅅ
    pag.press('p') #ㅔ
    pag.press('enter')
    #무궁화 삼천리
    pag.press('a') #ㅁ
    pag.press('n') #ㅜ
    pag.press('r') #ㄱ
    pag.press('n') #ㅜ
    pag.press('d') #ㅇ
    pag.press('g') #ㅎ
    pag.press('h') #ㅗ
    pag.press('k') #ㅏ
    pag.press('space') #띄어쓰기
    pag.press('t') #ㅅ
    pag.press('k') #ㅏ
    pag.press('a') #ㅁ
    pag.press('c') #ㅊ
    pag.press('j') #ㅓ
    pag.press('s') #ㄴ
    pag.press('f') #ㄹ
    pag.press('l') #ㅣ
    pag.press('space') #띄어쓰기
    #화려강산
    pag.press('g') #ㅎ
    pag.press('h') #ㅗ
    pag.press('k') #ㅏ
    pag.press('f') #ㄹ
    pag.press('u') #ㅕ
    pag.press('r') #ㄱ
    pag.press('k') #ㅏ
    pag.press('d') #ㅇ
    pag.press('t') #ㅅ
    pag.press('k') #ㅏ
    pag.press('s') #ㄴ
    pag.press('enter')
    #대한사람 대한으로
    pag.press('e') #ㄷ
    pag.press('o') #ㅐ
    pag.press('g') #ㅎ
    pag.press('k') #ㅏ
    pag.press('s') #ㄴ
    pag.press('t') #ㅅ
    pag.press('k') #ㅏ
    pag.press('f') #ㄹ
    pag.press('k') #ㅏ
    pag.press('a') #ㅁ
    pag.press('space') #띄어쓰기
    pag.press('e') #ㄷ
    pag.press('o') #ㅐ
    pag.press('g') #ㅎ
    pag.press('k') #ㅏ
    pag.press('s') #ㄴ
    pag.press('d') #ㅇ
    pag.press('m') #ㅡ
    pag.press('f') #ㄹ
    pag.press('h') #ㅗ
    pag.press('space') #띄어쓰기
    #길이 보전하세.
    pag.press('r') #ㄱ
    pag.press('l') #ㅣ
    pag.press('f') #ㄹ
    pag.press('d') #ㅇ
    pag.press('l') #ㅣ
    pag.press('space') #띄어쓰기
    pag.press('q') #ㅂ
    pag.press('h') #ㅗ
    pag.press('w') #ㅈ
    pag.press('j') #ㅓ
    pag.press('s') #ㄴ
    pag.press('g') #ㅎ
    pag.press('k') #ㅏ
    pag.press('t') #ㅅ
    pag.press('p') #ㅔ
    pag.press('.') #.
    pag.press('enter')
    print('finished')
    status_label.config(text="Finished")
    root.update()
    root.after(5000, lambda: status_label.config(text="ro1004bin"))
 
#Tkbuttons
btn1 = tk.Button(frame, text="매크로 시작", command=start)
btn1.pack(side='left', padx=10)

exitbtn = tk.Button(frame, text="exit", command=exit)
exitbtn.pack(side='left', padx=10)

root.mainloop()
