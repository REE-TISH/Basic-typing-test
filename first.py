
from faker import Faker
from tkinter import *


fake = Faker('en_US')
def generate_paragraph():
    word = []
    while len(word) < 60:
        para = fake.text().split()
        word.extend(para)
    trimmed = word[:60]
    return " ".join(trimmed)

def enablingEntry():
      k = give_para()
      Typing_section.config(state='normal')
      start_button.destroy()
      Typing_section.place(y=250)
      time_label = Label(frame,font=("aria;",13),text="60")
      time_label.place(x=80,y=50,height=30,width=160)
      countdown(60,time_label,k)
      

def give_para():
        Para_section.config(text="")
        para_text = generate_paragraph()
        Para_section.config(text=para_text)
        return para_text
def countdown(time_left,time_label,k):
    if time_left >= 0:
        time_label.config(text=f"Time left: {time_left} sec")
        window.after(1000, countdown, time_left - 1,time_label,k)
        if time_left == 0:
            Typing_section.config(state='disabled')
            calc_Result(k) 

def result_Box(speed,acc):
        
        result_label.place(height=100,width=600,x=100,y=460)
        result_label.config(text=f"Wpm = {speed}.......Accuracy = {acc}%")

def calc_Result(text):
     written_text = Typing_section.get('1.0',END).split()
     para_text = text.split()
     right_word = 0
     wrong_word = 0
     for i in range(len(written_text)):
          if written_text[i] == para_text[i]:
               right_word += 1
          else:
               wrong_word += 1
     if right_word != 0:
        wpm = right_word
        accuracy = (right_word/(wrong_word + right_word))*100
     else:
          wpm = 0
          accuracy = 0
     result_Box(wpm,int(accuracy))
   

     

window = Tk()
window.title('Typing Speed Test')
window.geometry("800x600")

Label_typing = Label(window,text="TYPING TEST",font=("Arial",30)).pack()

frame = Frame(window,height=500).pack(fill=X)

Para_section = Label(frame,text="   Press the start button ",font=("Arial",14),wraplength=600,justify=LEFT)
Para_section.place(height=150,width=600,x=80,y=80)



start_button = Button(frame,text="start",command=enablingEntry)
start_button.place(height=40,width=80,x=350,y=230)

Typing_section = Text(frame,font=("Arial",14),wrap=WORD,state='disabled')
Typing_section.place(height=150,width=600,x=80,y=300)

result_label = Label(window,text="",font=("arial",14))


window.mainloop()





