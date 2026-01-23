# RGB Color Mixer mit tkinter
# Quelle: https://www.youtube.com/watch?v=ip-lZb_yL8U
#         Stephen Hustedde - Python Programming (CIS156)
#         Python 11C More tkinter GUI RGB Color Mixer

import tkinter

class MyGUI:
    def __init__(self):
        bgcolor = '#e0e0ff'
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.config(background=bgcolor)  # config() or configure()
        self.main_window.geometry("350x570+300+100") # WidthxHeight+xpos+ypos
        self.main_window.title("CIS156 GUI RGB Color Mixer")

        # now add a label
        self.lblTitle = tkinter.Label(self.main_window, text="RGB Swatch")
        self.lblTitle.config(bg=bgcolor)
        self.lblTitle.config(font=("Arial", 24, "bold", "italic"))
        self.lblTitle.pack()

        self.swatch = tkinter.Canvas(self.main_window, width=200, height=200, bg='black')
        self.swatch.pack()
        self.spacer1 = tkinter.Label(self.main_window,text=" ", bg=bgcolor, font="Arial 10").pack()

        self.frameSliders = tkinter.Frame(self.main_window, bg=bgcolor)
        # now add the sliders
        self.sliderRed = tkinter.Scale(self.frameSliders, bg='red', length=256, tickinterval=32, from_=255, to_=0, command=self.setColor)
        self.sliderGreen = tkinter.Scale(self.frameSliders, bg='green', length=256, tickinterval=32, from_=255, to_=0, command=self.setColor)
        self.sliderBlue = tkinter.Scale(self.frameSliders, bg='blue', length=256, tickinterval=32, from_=255, to_=0, command=self.setColor)
        self.sliderRed.pack(side='left') # left puts them side by side within the frame
        self.sliderGreen.pack(side='left')
        self.sliderBlue.pack(side='left')
        self.frameSliders.pack()

        self.lblHex = tkinter.Label(self.main_window, text="#000000", bg=bgcolor, font="Arial 18 bold")
        self.lblHex.pack()

    def setColor(self, x):
        r = self.sliderRed.get()
        g = self.sliderGreen.get()
        b = self.sliderBlue.get()
        hexVal = "#" + self.dec2Hex(r) + self.dec2Hex(g) + self.dec2Hex(b)
        self.swatch.configure(bg=hexVal)
        self.lblHex.config(text = hexVal)

    def dec2Hex(self, decimal):
        hexValues = "0123456789ABCDEF"
        sixteens = decimal // 16
        ones = decimal % 16
        hex = hexValues[sixteens] + hexValues[ones]
        return hex

# Create an instance of the MyGUI class
my_gui = MyGUI()

# Main loop
my_gui.main_window.mainloop()        
