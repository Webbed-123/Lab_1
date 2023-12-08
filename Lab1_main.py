from Lab1_gui import *

def main():
    window = tk.Tk()
    window.title('Voting Menu')
    window.geometry('200x200')
    window.resizable(True, True)
        
    Gui(window)
    window.mainloop()
        
if __name__ == '__main__':
    main()