import tkinter as tk

class PlayGame:
    def __init__(self):
        self.history=[] #Will contain the move history. Each element is a quadruple consisting of the state,action,reinforcement,new state.
        
        self.root=tk.Tk()
        for i in range(27):
            for j in range(27):
                    tk.Label(self.root,text='$',height=1,width=3).grid(row=i,column=j)
        self.I=[14,14]
        tk.Label(self.root,text='I',height=1,width=3).grid(row=14,column=14)
        self.root.bind('<KeyPress>',self.onKeyPress)
        self.root.mainloop()

    def onKeyPress(self,event):
        if event.keysym in ['Up','Right','Down','Left']:
            if event.keysym=='Up':
                tk.Label(self.root,text='',height=1,width=3).grid(row=self.I[0],column=self.I[1])
                tk.Label(self.root,text='I',height=1,width=3).grid(row=self.I[0]+1,column=self.I[1])
                self.I[0]+=1

PlayGame()
