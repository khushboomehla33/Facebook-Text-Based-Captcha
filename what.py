from tkinter import *
def what1():
    root=Tk()
    head=Frame(root,width=1366,height=45,bg='#3b5998')
    head.place(x=0,y=0)
    heading=Label(head,text="What is Captcha?",bg='#3b5998',fg='white',font=('Segoe UI',20,'bold'),justify="center")
    heading.place(x=5,y=5)
    text = Label(root, text='\nCAPTCHA is Completely Automated Public Turing Test To Tell Computers and Humans Apart .\nIt was coined in 2000 by Luis von Ahn, Manuel Blum, Nicholas Hopper and John Langford of Carnegie Mellon University.\nA CAPTCHA is a program that protects websites against bots by generating and grading tests that humans can pass but current computer programs cannot.\n For example, humans can read distorted text as the one shown below, but current computer programs can not.\nIf your website needs protection from abuse, it is recommended that you use a CAPTCHA. \nThere are many CAPTCHA implementations, some better than others.',bg='white',font=('verdana' ,12, 'bold'))
    text.place(x=0,y=50)
    root.configure(background='white')
    root.geometry("1366x700+0+0")
    root.mainloop()
