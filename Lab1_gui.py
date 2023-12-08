import tkinter as tk
import Lab1_logic


class Gui:
    
    def __init__(self, window):
        self.window = window
        self.label_heading = tk.Label(self.window, text="Voting Menu", font=('Arial', 30))
        self.label_heading.grid()
        self.vote_button = tk.Button(self.window, text='VOTE', font=(('Arial'),18),command=self.vote)
        self.vote_button.grid()
        self.submit_button = tk.Button(self.window, text='SUBMIT', font=(('Arial'),18),command=self.submit)
        self.results_label = tk.Label(self.window, text="", font=('Arial', 30))
        #self.results_label.grid()
        self.results_button = tk.Button(self.window, text='RESULTS', font=(('Arial'),18),command=self.results)
        #self.results_button.grid()
        
    def vote(self):
        self.radio_1 = tk.IntVar()
        self.radio_1.set(0)
        self.radio_candidate_one = tk.Radiobutton(self.window, text='Cameron', variable=self.radio_1, value=1, command=self.submit_button.grid())
        self.radio_candidate_two = tk.Radiobutton(self.window, text='Allison', variable=self.radio_1, value=2, command=self.submit_button.grid())
        self.radio_candidate_three = tk.Radiobutton(self.window, text='Diego', variable=self.radio_1, value=3, command=self.submit_button.grid())
        self.radio_candidate_one.grid()
        self.radio_candidate_two.grid()
        self.radio_candidate_three.grid()
        self.vote_button.grid_forget()
        self.results_label.grid_forget()
        self.results_button.grid_forget()
    
    def submit(self):
        status = str(self.radio_1.get())
        Lab1_logic.add(status)
        self.radio_1.set(0)
        self.submit_button.grid_forget()
        self.radio_candidate_one.grid_forget()
        self.radio_candidate_two.grid_forget()
        self.radio_candidate_three.grid_forget()
        self.results_label.grid_forget()
        self.vote_button.grid()
        self.results_button.grid()
        
    def results(self):
        self.results_label = tk.Label(self.window, text=f'{Lab1_logic.results()}', font=(('Arial'),18))
        self.results_label.grid()
        self.results_button.grid_forget()
        
            
        
        
        
        