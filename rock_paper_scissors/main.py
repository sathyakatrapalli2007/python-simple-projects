import customtkinter as ctk
import random

class RockPaperScissors(ctk.CTk):
    """A class to deal with all widgets and game behaviour"""
    def __init__(self):
        """Initialize parent attributes"""
        super().__init__()

        self.title("ROCK PAPER SCISSORS")
        self.geometry("450x600")
        self.configure(fg_color="#1e1b26")

        self.player_score=0
        self.computer_score=0
        self.timer_id=None
        self.breather_id=None

        # Colors for the "Surgical" UI
        self.CARD_BG = "#e6e6fa"    # Lavender
        self.ACCENT = "#6b0033"     # Maroon
        self.TEXT_MAIN = "#6b0033"

        self.create_widgets()
        self.start_timer(7)

    def start_timer(self,count):
        if count==7:
            self.toggle_buttons("normal")
        self.time_label.configure(text=f"Time left:{count}s",text_color="pink")
        if count>0:
             self.timer_id=self.after(1000,lambda: self.start_timer(count-1))
        else:
             self.auto_play()
    
    def auto_play(self):
        self.toggle_buttons("disabled")
        self.kill_all_timers()
        self.computer_score+=1
        self.status_label.configure(text="TIME'S UP! CPU gets a point!", text_color="red")
        self.score_label.configure(text=f"Player: {self.player_score} | computer: {self.computer_score}")

        self.breather_id=self.after(2000, lambda:self.start_timer(7))      

    def create_widgets(self):

        self.main_card = ctk.CTkFrame(self, fg_color=self.CARD_BG, corner_radius=20)
        self.main_card.pack(pady=40, padx=30, fill="both", expand=True)

        self.score_frame = ctk.CTkFrame(self.main_card, fg_color="transparent")
        self.score_frame.pack(pady=(30, 20))

        self.score_border = ctk.CTkFrame(
            self.score_frame, 
            fg_color="transparent", 
            border_width=2, 
            border_color=self.ACCENT, 
            corner_radius=8
        )
        self.score_border.pack()

        score_style = {
            "font": ("Arial", 16),
            "text_color": self.TEXT_MAIN,
            "height": 40
        }

        #status label
        self.status_label = ctk.CTkLabel(self.main_card, text="Choose your weapon!", 
                                         font=("Arial", 18, "bold"), text_color=self.TEXT_MAIN)
        self.status_label.pack(pady=(20, 5))

        #score label
        self.score_label=ctk.CTkLabel(self.score_border,text="Player:0 | Computer:0",**score_style)
        self.score_label.pack(padx=20)

        #time label
        self.time_label = ctk.CTkLabel(self.main_card, text="Time left: 7s", 
                                       font=("Arial", 16), text_color=self.TEXT_MAIN)
        self.time_label.pack(pady=5)

        #create frame
        self.button_frame=ctk.CTkFrame(self.main_card,fg_color="transparent")
        self.button_frame.pack(pady=20)

        #buttons inside the frame

        weapons_data = [("✊", "Rock"), ("✋", "Paper"), ("✌️", "Scissor")]
        self.buttons_list=[]
        for icon,weapon in weapons_data:
            button = ctk.CTkButton(
                self.button_frame, 
                text=icon, 
                font=("Arial", 35),
                width=90, 
                height=90,
                fg_color="white",
                text_color=self.ACCENT,
                hover_color="#dcd0ff", # Light purple hover
                border_width=2,
                border_color=self.ACCENT,
                corner_radius=12,
                command=lambda w=weapon: self.play_round(w)
            )

            button.pack(padx=10,side="left")
            self.buttons_list.append(button)

        self.reset_button = ctk.CTkButton(
        self.main_card, text="Play Again", fg_color=self.ACCENT, 
        text_color="white", hover_color="#4d0025", 
        font=("Arial", 16, "bold"), height=45, corner_radius=10,
        command=self.reset_game)
        
        self.reset_button.pack(pady=(30, 20))
        
    def reset_game(self):
        self.kill_all_timers()

        self.player_score=0
        self.computer_score=0
        self.score_label.configure(text=f"Player:{self.player_score} | Computer:{self.computer_score}")
        self.status_label.configure(text="Chose your weapon",text_color="black")
        self.start_timer(7)

    def kill_all_timers(self):
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id=None

        if self.breather_id:
            self.after_cancel(self.breather_id)
            self.breather_id=None
         
    def toggle_buttons(self,state_value):
        for button in self.buttons_list:
             button.configure(state=state_value)

    def play_round(self,user_choice):
        self.toggle_buttons("disabled")
        self.kill_all_timers()
        weapons=["Rock","Paper","Scissor"]
        computer_choice=random.choice(weapons)
        result = None
        winning_pairs={
                        "Rock":"Scissor",
                        "Scissor":"Paper",
                        "Paper":"Rock",
                    }

        if computer_choice == user_choice:
            result = "It's a tie"
        elif winning_pairs[user_choice]==computer_choice:
                self.player_score += 1
                result = "You win!!"
        else:
                self.computer_score += 1
                result = "You loose!!"

        # Fallback in case logic fails
        if result is None:
            result = f"Unexpected: {user_choice} vs {computer_choice}"

        self.update_screen(user_choice, computer_choice, result)
        self.breather_id=self.after(2000,lambda:self.start_timer(7))

    def update_screen(self,user_choice,computer_choice,result):
        self.score_label.configure(text=f"Player:{self.player_score} | Computer:{self.computer_score}")
        final_color="black"
        if result=="You win!!":
            final_color="green"
        elif result=="You loose!!":
            final_color="red"
        self.status_label.configure(text=f"{user_choice} vs {computer_choice}: {result}",text_color=final_color)


if __name__=="__main__":
    rps=RockPaperScissors()
    rps.mainloop()

