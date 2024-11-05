import random
import math
import tkinter
import tkinter.messagebox as messagebox
import time

# 初期設定
version = tkinter.Tcl().eval('info patchlevel')
window = tkinter.Tk()
window.geometry("1000x1000")
window.title("Mine Crash")
 
canvas = tkinter.Canvas(window, bg = "#deb887", height = 1000, width = 1000)
canvas.place(x = 0, y = 0)

imagesize = 150 #サイズの変更は出来ません
stagesize_x = 5 #サイズの変更は出来ません
stagesize_y = 5 #サイズの変更は出来ません

Stage = tkinter.PhotoImage(file = "描いたイラスト/Stage.png", width = imagesize, height = imagesize)
Miritary = tkinter.PhotoImage(file = "描いたイラスト/miritari-.png", width = imagesize, height = imagesize)


txt = ""
direct = ""
ansx = random.randint(0,stagesize_x - 1)
ansy = random.randint(0,stagesize_y - 1)
xin = random.randint(0,stagesize_x - 1)
yin = random.randint(0,stagesize_y - 1)
posx = xin
posy = yin

nowTime = 0
setTime = str(int(time.time()))
setTime = setTime[-7:]
setTime = int(setTime)

Limit = nowTime - setTime

lbl = tkinter.Label(text='What will you do?')
lbl.place(x=300, y=10)
txt = tkinter.Entry(width=10)
txt.place(x = 445, y = 10)

# 地雷の場所を検索する関数
def Search():
    messagebox.showinfo('調査完了のお知らせ',"地雷との距離は" + 
                        str(math.sqrt((xin - ansx)*(xin - ansx)+(yin - ansy)*(yin - ansy))) + "だ")

# 「地雷をCrash！」ボタンを押されたら地雷があるかを判定する
def Crash():
    # もしあればメッセージボックスを表示して画面を閉じる
    if (xin,yin) == (ansx,ansy):
        messagebox.showinfo('朗報　除去成功', '処理が完了しました。')
        window.destroy()
    # なければメッセージボックスを表示して再開する
    else:
        messagebox.showinfo('除去失敗のお知らせ', 'MINE IS FINE.\nFIND IT!')

# それぞれボタンの配置と設定
check_button = tkinter.Button(window,text="距離を測る", width = 10, height = 3, font = ('MSゴシック',14),
                                bg = "light coral", relief = "raised", bd = 14, command = Search)
check_button.place(x = 840, y =150 )

crash_button = tkinter.Button(window,text="地雷をCrash！", width = 12, height = 3, font = ('MSゴシック',14),
                                bg = "pale turquoise", relief = "raised", bd = 14,command = Crash)
crash_button.place(x = 830, y =400 )

# 時間切れの処理
def TimeOver():
    if Limit <0:
        messagebox.showinfo('TIMEOVER', '判断が遅い！')
        window.destroy()        

# ボタンが押された時の処理
def btn_click():
  global direct
  global txtcheck
  direct = txt.get()
  txtcheck = 1
  print(txtcheck)
  txt.delete(0, tkinter.END)
  print(direct)

# 無限ループ
def loopWindow():
    global xin
    global yin
    global posx
    global posy
    global direct
    global setTime
    global Limit
    
    nowTime = str(int(time.time()))
    nowTime = nowTime[-7:]
    nowTime = int(nowTime)
    
    # 制限時間の計測
    Limit = 30 -( nowTime - setTime )
    
    TimeOver()
    
    # 制限時間の配置と設定
    lbl = tkinter.Label(text=Limit, width = 4, height = 2, font = ('ゴシック',30),
                                bg = "white", relief = "raised", bd = 5)
    lbl.place(x=830, y=20)
    
    # 入力された文字を調べる
    # 「a」、「d」、「w」、「s」でそれぞれ左右、上下の仮想的な座標変数を１だけ変更する
    if direct != "":
        if direct == "a":
            posx -= 1
        elif direct == "d":
            posx += 1
        elif direct == "s":
            posy += 1
        elif direct == "w":
            posy -= 1
            
        # elif direct == "crash":
        #     if (xin,yin) == (ansx,ansy):
        #         messagebox.showinfo('朗報　除去成功', '処理が完了しました。')
        #         window.destroy()
        #     else:
        #         messagebox.showinfo('除去失敗のお知らせ', 'MINE IS FINE.\nFIND IT!')
        # elif direct == "search":
            # messagebox.showinfo('調査完了のお知らせ',"地雷との距離は" + str(math.sqrt((xin - ansx)*(xin - ansx)+(yin - ansy)*(yin - ansy))) + "だ")
        
        # 関係ないコマンドが入力された場合
        else:
            messagebox.showinfo('間違いのお知らせ', 'その文字列には非対応です\na, d, w, s, searchもしくはcrashのいずれかを入力してください')
        
        # もしプレイヤーが画面外の座標に移動したらメッセージボックスを表示し、実際の座標に仮想的な座標変数を代入しない
        if posx >= stagesize_x or posy >= stagesize_y or posx < 0 or posy < 0:
            messagebox.showinfo('間違いのお知らせ', '捜索範囲外です')
            posx = xin
            posy = yin
        # プレイヤーが画面内を移動している場合は、仮想的な変数を実際の座標に反映する
        else:
            xin = posx
            yin = posy
        direct = ""
    
    #print(xin,yin)
    # 画面の描画をし直すため、画面を全消去する
    canvas.delete("all")
    for y in range(stagesize_y):
        for x in range(stagesize_x):
            if (x,y) == (xin,yin):
                canvas.create_image(30 + x * imagesize, 30 + y * imagesize, image = Stage, anchor = tkinter.NW)
                canvas.create_image(30 + x * imagesize, 30 + y * imagesize, image = Miritary, anchor = tkinter.NW)
            else:
                canvas.create_image(30 + x * imagesize, 30 + y * imagesize, image = Stage, anchor = tkinter.NW)  
    # if posx >= stagesize_x or posy >= stagesize_y or posx < 0 or posy < 0:
    #     posx = xin
    #     posy = yin
    # else:
    #     xin = posx
    #     yin = posy

    # 描画しなおす間隔を設定する（Frame Per Secondのようなもの）
    window.after(50, loopWindow)

# Enterキーが押されたときの関数
def checker(event):
    global direct
    # 入力された文字を変数に代入する
    direct = txt.get()
    # もし入力されたらテキストボックス内の文字を取り除く
    if direct != "":
        txt.delete(0, tkinter.END)

# 前述の関数を実行する
loopWindow()   

# Enterキーが押されたらchackerという関数を実行する
window.bind("<Return>", checker)

window.mainloop()

