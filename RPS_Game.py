import tkinter as tk
import random

class  Game:
    def __init__(self,root):
        self.root = root
        self.root.title("Rock, Paper, Scissor Game")
        self.root.geometry("400x400")
        
        self.choices = ("Rock","Paper","Scissor")
        
        self.user_score=0
        self.comp_score=0
        
        self.Label = tk.Label(root, text="Choosse Rock, Paper, or Scissor", font=("Arial",12))
        self.Label.pack(pady=10)
        
        self.scrore_lable = tk.Label(root, text="You: 0 | computer: 0",font=("Arial",12))
        self.scrore_lable.pack(pady=10)
        
        self.result = tk.Label(root, text="", font=("Arial", 12))
        self.result.pack(pady=10)

        
        for choice in self.choices:
            btn = tk.Button(root, text=choice, width=15,
                         command=lambda c=choice: self.play(c))
            btn.pack(pady=5)
            
    def play(self, user_choice):
        comp_choice = random.choice(self.choices)
        result_text = f"You chose {user_choice}, Computer chose {comp_choice}."
        
        if user_choice == comp_choice:
            result_text += "It's a Draw!"
        elif (user_choice== "Rock" and comp_choice=="Scissor") or \
            (user_choice== "Paper" and comp_choice=="Rock") or \
            (user_choice== "Sciccors" and comp_choice=="Paper"):
                result_text += "You Win!"
                self.user_score += 1
        else:
            result_text += "Computer Wins!"
            self.comp_score +=1
        
        self.result.config(text= result_text)
        self.scrore_lable.config(text= f"You: {self.user_score} | Computer: {self.comp_score}")

root = tk.Tk()
game = Game(root)
root.mainloop()