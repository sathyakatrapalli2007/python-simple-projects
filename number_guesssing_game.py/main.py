import customtkinter as ctk
import random
class NumberGuess(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("450x600")
        self.configure(fg_color="#FFF5E1")
        self.target=random.randint(1,100)
        self.lives=7

        self.blue_frame=ctk.CTkFrame(self,fg_color="#D1E9FF",
                                     corner_radius=20, border_color="#004A99", border_width=3)
        self.blue_frame.pack(pady=30,padx=30,fill="both")

        self.digit_one=ctk.CTkLabel(self.blue_frame,text="?",font=("Arial", 100, "bold"), text_color="#004A99")
        self.digit_one.place(relx=0.35,rely=0.5,anchor="center")

        self.digit_two=ctk.CTkLabel(self.blue_frame,text="?",font=("Arial", 100, "bold"), text_color="#004A99")
        self.digit_two.place(relx=0.65,rely=0.5,anchor="center")

        self.user_guess=ctk.CTkEntry(self,placeholder_text="Enter 1-100", 
                                      width=200, height=40, corner_radius=10)
        self.user_guess.pack(pady=10)

        self.button=ctk.CTkButton(self,text="PULL LEVER",command=self.check_logic,
                                       fg_color="#004A99", hover_color="#003366")
        self.button.pack(pady=10)
        
        self.status_msg = ctk.CTkLabel(self, text="Start Guessing!", text_color="#004A99")
        self.status_msg.pack(pady=5)

        self.lives_msg = ctk.CTkLabel(self, text=f"Lives left: {self.lives}!", text_color="#004A99")
        self.lives_msg.pack(pady=5)

    def check_logic(self):

        raw_value=self.user_guess.get()
        if not raw_value.isdigit():
            self.status_msg.configure(text="Error: Enter a number!")
            return
        
        val=int(raw_value)
        guess_val=f"{val:02d}"
        self.digit_one.configure(text=guess_val[0])
        self.digit_two.configure(text=guess_val[1])

        self.lives-=1
        self.lives_msg.configure(text=f"Tries left:{self.lives}")

        
        if val==self.target:
            self.end_game(True)
            self.status_msg.configure(text="CORRECT! 🎉", text_color="green")

        elif self.lives==0:
            self.end_game(False)
        
        else:
            if val < self.target:
                self.status_msg.configure(text="Too Low! Try again.")
            elif val > self.target:
                self.status_msg.configure(text="Too High! Try again.")
            self.user_guess.delete(0, "end")

        
    def end_game(self,won):
        self.user_guess.configure(state="disabled")
        self.button.configure(state="disabled")
        if won:
            self.status_msg.configure(text="MISSION SUCCESS", text_color="green")
        else:
            self.status_msg.configure(text=f"GAME OVER. It was {self.target}", text_color="red")
            self.digit_one.configure(text=str(self.target)[0])
            self.digit_two.configure(text=str(self.target)[1])

        self.after(2000,self.change_status)
        
    def change_status(self):
        self.button.configure(state="disabled",text="Processing")
        self.after(2000,self.play_game)

    def play_game(self):
        self.button.configure(
        state="normal", 
        text="PLAY AGAIN", 
        command=self.start_reset_game
    )
        
    def start_reset_game(self):
        self.button.configure(state="disabled",text="Resetting....")
        self.after(2000,self.reset_game)


    def reset_game(self):

        self.target=random.randint(1,100)
        self.lives=7
        self.lives_msg.configure(text=f"Tries left:{self.lives}")
        self.digit_one.configure(text="?")
        self.digit_two.configure(text="?")
        self.status_msg.configure(text="New Game Started!", text_color="#004A99")

        self.button.configure(
        state="normal", 
        text="PULL LEVER", 
        command=self.check_logic # Point back to the game logic
    )


if __name__=="__main__":
    number=NumberGuess()
    number.mainloop()

    