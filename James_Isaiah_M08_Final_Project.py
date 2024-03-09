# m08 final project
# isaiah james
# 2024-03-09
# nba team stat tracker

# import tkinter GUI
import tkinter as tk


class MidSeasonStatTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Mid-Season Stat Tracker")
        self.root.geometry("400x400")
        self.root.configure(bg="navy")

        self.logo_image = tk.PhotoImage(file=r"C:\Users\Isaia\Desktop\nba-logo.png")  # load image file path

        # nba logo at the top
        self.logo_label = tk.Label(root, image=self.logo_image,)
        self.logo_label.pack(pady=10)

        # team selection window
        self.team_names = [
            "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls",
            "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons",
            "Golden State Warriors", "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers",
            "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat", "Milwaukee Bucks",
            "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks", "Oklahoma City Thunder",
            "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers",
            "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards"
        ]
        # team stat dictionary
        self.stats = {
            "Atlanta Hawks": {"Wins": 29, "Losses": 34, "Points Per Game": 123.8, "Points Allowed": 121.5},
            "Boston Celtics": {"Wins": 48, "Losses": 14, "Points Per Game": 120.8, "Points Allowed": 109.9},
            "Brooklyn Nets": {"Wins": 25, "Losses": 38, "Points Per Game": 112.0, "Points Allowed": 114.1},
            "Charlotte Hornets": {"Wins": 15, "Losses": 48, "Points Per Game": 107.2, "Points Allowed": 117.6},
            "Chicago Bulls": {"Wins": 31, "Losses": 32, "Points Per Game": 112.0, "Points Allowed": 113.3},
            "Cleveland Cavaliers": {"Wins": 41, "Losses": 22, "Points Per Game": 114.0, "Points Allowed": 109.4},
            "Dallas Mavericks": {"Wins": 35, "Losses": 28, "Points Per Game": 118.7, "Points Allowed": 118.1},
            "Denver Nuggets": {"Wins": 43, "Losses": 20, "Points Per Game": 114.4, "Points Allowed": 110.4},
            "Detroit Pistons": {"Wins": 10, "Losses": 52, "Points Per Game": 112.2, "Points Allowed": 120.8},
            "Golden State Warriors": {"Wins": 33, "Losses": 29, "Points Per Game": 118.7, "Points Allowed": 116.9},
            "Houston Rockets": {"Wins": 28, "Losses": 35, "Points Per Game": 113.0, "Points Allowed": 112.8},
            "Indiana Pacers": {"Wins": 35, "Losses": 29, "Points Per Game": 123.3, "Points Allowed": 121.8},
            "Los Angeles Clippers": {"Wins": 40, "Losses": 21, "Points Per Game": 117.2, "Points Allowed": 112.6},
            "Los Angeles Lakers": {"Wins": 35, "Losses": 30, "Points Per Game": 117.2, "Points Allowed": 117.6},
            "Memphis Grizzlies": {"Wins": 22, "Losses": 42, "Points Per Game": 106.0, "Points Allowed": 112.3},
            "Miami Heat": {"Wins": 35, "Losses": 28, "Points Per Game": 110.5, "Points Allowed": 109.9},
            "Milwaukee Bucks": {"Wins": 41, "Losses": 23, "Points Per Game": 120.9, "Points Allowed": 117.1},
            "Minnesota Timberwolves": {"Wins": 44, "Losses": 20, "Points Per Game": 113.2, "Points Allowed": 106.6},
            "New Orleans Pelicans": {"Wins": 38, "Losses": 25, "Points Per Game": 116.4, "Points Allowed": 111.2},
            "New York Knicks": {"Wins": 37, "Losses": 26, "Points Per Game": 113.0, "Points Allowed": 109.3},
            "Oklahoma City Thunder": {"Wins": 44, "Losses": 19, "Points Per Game": 120.8, "Points Allowed": 113.2},
            "Orlando Magic": {"Wins": 37, "Losses": 27, "Points Per Game": 110.9, "Points Allowed": 109.4},
            "Philadelphia 76ers": {"Wins": 35, "Losses": 28, "Points Per Game": 116.5, "Points Allowed": 113.6},
            "Phoenix Suns": {"Wins": 37, "Losses": 26, "Points Per Game": 117.1, "Points Allowed": 114.3},
            "Portland Trail Blazers": {"Wins": 17, "Losses": 45, "Points Per Game": 107.8, "Points Allowed": 116.0},
            "Sacramento Kings": {"Wins": 36, "Losses": 26, "Points Per Game": 118.5, "Points Allowed": 118.0},
            "San Antonio Spurs": {"Wins": 13, "Losses": 50, "Points Per Game": 112.4, "Points Allowed": 120.4},
            "Toronto Raptors": {"Wins": 23, "Losses": 40, "Points Per Game": 114.1, "Points Allowed": 118.0},
            "Utah Jazz": {"Wins": 28, "Losses": 35, "Points Per Game": 117.7, "Points Allowed": 120.4},
            "Washington Wizards": {"Wins": 10, "Losses": 53, "Points Per Game": 114.5, "Points Allowed": 124.2},
        }

        # select button to open 2nd window
        self.team_listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg="navy", fg="white", selectbackground="gray") #colors of the window
        for team in self.team_names:
            self.team_listbox.insert(tk.END, team)
        self.team_listbox.pack(pady=10)
        # open team window with select button
        self.select_button = tk.Button(root, text="Select Team", command=self.open_team_window, bg="gray", fg="black")
        self.select_button.pack()

        # open 2nd window
    def open_team_window(self):
        selected_team = self.team_listbox.get(tk.ACTIVE) # select team
        if selected_team:
            team_window = tk.Toplevel(self.root)
            team_window.title(selected_team) # open team window
            # fetch stats
            stats_labels = [] # import stats into team window
            for stat, value in self.stats[selected_team].items():
                label = tk.Label(team_window, text=f"{stat}: {value}", font=("Helvetica", 12))
                label.pack(pady=10)
                stats_labels.append(label)


            # team stat window close button
            close_button = tk.Button(team_window, text="Close", command=team_window.destroy, bg="gray", fg="black")
            close_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = MidSeasonStatTracker(root)
    root.mainloop()
