import tkinter as tk
from tkinter import Menu
import random,time
import sys,os


BG_COLOR = '#afafaf'
DIR = os.path.dirname(os.path.abspath(__file__))
file_board = os.path.join(DIR,'assets','board.png')
file_show = os.path.join(DIR,'assets','show.png')
random.seed(time.asctime)

which_quote=None #记录选择了哪个音
dot_id = None # 记录canvas画的点，为方便删除
#前面一个数字表示第几弦，剩下的数字表示第几品。112表示1弦12品。
##answer={
##    '10': 'E', '20': 'B', '30': 'G', '40': 'D', '50': 'A', '60': 'E',
##    '11': 'F', '21': 'C', '31': '#G','41': '#D','51': '#A','61': 'F',
##    '12': '#F','22': '#C','32': 'A', '42': 'E', '52': 'B', '62': '#F',
##    '13': 'G', '23': 'D', '33': '#A','43': 'F', '53': 'C', '63': 'G',
##    '14': '#G','24': '#D','34': 'B', '44': '#F','54': '#C','64': '#G',
##    '15': 'A', '25': 'E', '35': 'C', '45': 'G', '55': 'D', '65': 'A',
##    '16': '#A','26': 'F', '36': '#C','46': '#G','56': '#D','66': '#A',
##    '17': 'B', '27': '#F','37': 'D', '47': 'A', '57': 'E', '67': 'B',
##    '18': 'C', '28': 'G', '38': '#D','48': '#A','58': 'F', '68': 'C',
##    '19': '#C','29': '#G','39': 'E', '49': 'B', '59': '#F','69': '#C',
##    '110':'D', '210':'A', '310':'F', '410':'C', '510':'G', '610':'D',
##    '111':'#D','211':'#A','311':'#F','411':'#C','511':'#G','611':'#D',
##    '112':'E', '212':'B', '312':'G', '412':'D', '512':'A', '612':'E'
##}
answer={
    '10': '3', '20': '7', '30': '5', '40': '2', '50': '6', '60': '3',
    '11': '4', '21': '1', '31': '#5','41': '#2','51': '#6','61': '4',
    '12': '#4','22': '#1','32': '6', '42': '3', '52': '7', '62': '#4',
    '13': '5', '23': '2', '33': '#6','43': '4', '53': '1', '63': '5',
    '14': '#5','24': '#2','34': '7', '44': '#4','54': '#1','64': '#5',
    '15': '6', '25': '3', '35': '1', '45': '5', '55': '2', '65': '6',
    '16': '#6','26': '4', '36': '#1','46': '#5','56': '#2','66': '#6',
    '17': '7', '27': '#4','37': '2', '47': '6', '57': '3', '67': '7',
    '18': '1', '28': '5', '38': '#2','48': '#6','58': '4', '68': '1',
    '19': '#1','29': '#5','39': '3', '49': '7', '59': '#4','69': '#1',
    '110':'2', '210':'6', '310':'4', '410':'1', '510':'5', '610':'2',
    '111':'#2','211':'#6','311':'#4','411':'#1','511':'#5','611':'#2',
    '112':'3', '212':'7', '312':'5', '412':'2', '512':'6', '612':'3'
}
#-------------------------------------------------------------------
def show_key():
    pass


def check_answer(selected_quote):
    correct_answer.config(text=which_quote)
    if selected_quote == which_quote:
        you_answer.config(text=selected_quote, fg='blue')
        root.after(1000,random_dot) # 答对了，1s后自动下一个
    else:
        you_answer.config(text=selected_quote, fg='red')


def draw_dot(X, P):
    '''
    在吉他指板上显示一个点。
    X：第几根弦
    P：第几品
    '''
    l_pin=82 # 两品间隔：x方向
    l_xian=32 # 两弦间隔：y方向
    start_location=[30,69]
    dot_size=20
    x1= start_location[0]+ P * l_pin - dot_size/2
    y1= start_location[1]+ (X-1) * l_xian - dot_size/2
    x2= start_location[0]+ P * l_pin + dot_size/2
    y2= start_location[1]+ (X-1) * l_xian + dot_size/2

    dot_id = main_can.create_oval(x1,y1,x2,y2,fill='yellow',outline='')
    return dot_id
    

def random_dot():
    '''
    随机选择指板上一个位置
    '''
    global dot_id
    global which_quote
    #弦:[1-6]
    xian=[1,2,3,4,5,6]
    #品:[0-12]
    pin=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    X=random.choice(xian)
    P=random.choice(pin)
    which_quote= answer.get(str(X)+str(P))
    # print(X,P)
    if dot_id: # 先清除上一个点，再画新的
        main_can.delete(dot_id)
    dot_id = draw_dot(X, P)

    #清空答案
    you_answer.config(text='')
    correct_answer.config(text='')


def quit():
    root.destroy()
    # sys.exit()


def open_about():
    global pay_img1,pay_img2
    about_win = tk.Toplevel()
    about_win.title('关于')
    file_path1 = os.path.join(DIR,'assets','alipay.png')
    file_path2 = os.path.join(DIR,'assets','wechatpay.png')
    pay_img1 = tk.PhotoImage(file=file_path1)
    pay_img2 = tk.PhotoImage(file=file_path2)
    pay_img1 = pay_img1.subsample(4,4) # 缩小为1/4
    pay_img2 = pay_img2.subsample(4,4) # 缩小为1/4
    # img_canvas = tk.Canvas(about_win,bg=BG_COLOR,width=200,height=200)
    # img_canvas.pack(side='left')
    # img_canvas.create_image(100,100,anchor='center',image=pay_img)
    tk.Label(about_win,text='作者：wdh99 QQ:1628430840').pack(side='top')
    tk.Label(about_win,text='更多软件请访问：https://wdh99.github.io').pack(side='top')
    tk.Label(about_win,text='请开发者喝瓶饮料').pack(side='top')
    tk.Label(about_win,image=pay_img1,height=380).pack(side='left')
    tk.Label(about_win,image=pay_img2,height=380).pack(side='left')


root=tk.Tk()
root.title("吉他指板记忆V1.1")
root.resizable(False,False)

# 菜单栏: 退出, 关于
menu_main = Menu(root)
act_menu = Menu(menu_main)
about_menu = Menu(menu_main)
# menu_main.add_cascade(label='操作', menu=act_menu)
# menu_main.add_cascade(label='关于',menu=about_menu)
menu_main.add_command(label='关于',command=open_about)
menu_main.add_command(label='退出',command=quit)
root.config(menu=menu_main)
root['width']=1250
root.config(pady=5)

#创建一个框[上框],用于放[吉他画布]和[答案框]
frame_up=tk.Frame(height=380,bg=BG_COLOR)
frame_up.grid(row=0,column=0)
#吉他画布
canva_rect=(1100,300) # width, height
board_center=[canva_rect[0]/2, canva_rect[1]/2]#x, y
#
main_can=tk.Canvas(frame_up, bg=BG_COLOR,width=canva_rect[0], height=canva_rect[1])
main_can.pack(side='left')
img = tk.PhotoImage(file=file_board)
main_can.create_image(board_center[0],board_center[1],anchor='center',image=img)
#[答案框]
key_frame = tk.Frame(frame_up)
key_frame.pack()
#答案显示标签
font=('',20,'bold')
tk.Label(key_frame, text='你的答案：',padx=10,pady=20,font=font,bg=BG_COLOR).pack()
you_answer = tk.Label(key_frame, text='',padx=10,pady=20,font=font,bg=BG_COLOR)
you_answer.pack(fill=tk.X)
tk.Label(key_frame, text='正确答案：',padx=10,pady=20,font=font,bg=BG_COLOR).pack()
correct_answer = tk.Label(key_frame, text='',padx=10,pady=20,font=font,bg=BG_COLOR,fg='blue')
correct_answer.pack(fill=tk.X)

#这个frame用于放 radio[升号][还原][降号][按钮：七个音名][按钮:下一个]
frame_down=tk.Frame(height=100)
frame_down.grid(row=1,column=0)
#[按钮:七个音]
quote=   ['1', '#1','2', '#2','3','4', '#4','5', '#5','6','#6', '7']
# up_quote=['#1','#2','4','#4','#5','#6','1'] # 升音
# quote=   ['C', 'D', 'E','F', 'G', 'A', 'B']
# up_quote=['#C','#D','F','#F','#G','#A','C'] # 升音
quote_btns=[]
quote_rect=[1,2] # 按钮高、宽
for index,value in enumerate(quote):
    quote_btns.append(tk.Button(frame_down,
                              text=value,
                              height=quote_rect[0],
                              width=quote_rect[1],
                              bd=0,bg=BG_COLOR,
                              font=font,
                              border=1,
                              command=lambda x=value:check_answer(x)
                              ))
for btn in quote_btns:
    btn.pack(side='left')
    
#-------------------------------------------------------------------
#[按钮:下一个]
next_question=tk.Button(frame_down,text='下一个',
                        height=1,bd=0,bg='gray',
                        font=font,
                        command=random_dot)
next_question.pack(side='left')



root.mainloop()
