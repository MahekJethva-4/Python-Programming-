
# This program explains all concepts of functions and arguments
# using a Sports / Games theme.

print("=" * 60)
print("SPORTS FUNCTIONS AND ARGUMENTS PROGRAM")
print("=" * 60)

# 1. TYPES OF FUNCTIONS
print("\n========== 1. TYPES OF FUNCTIONS ==========")

# (a) Function without arguments and without return value
def start_match():
    print("Match has started! Play fair. Good luck to both teams!")

# (b) Function with arguments and without return value
def show_score(team, runs):
    print(team, "scored", runs, "runs.")

# (c) Function without arguments and with return value
def ball_weight():
    return 5.5   # weight of a cricket ball in ounces

# (d) Function with arguments and with return value
def total_points(win, loss):
    win_points = win * 2      # 2 points for a win
    return win_points - loss  # 1 point deducted for a loss

print("-- (a) No args, no return --")
start_match()

print("\n-- (b) With args, no return --")
show_score("India", 320)

print("\n-- (c) No args, with return --")
print("Weight of cricket ball =", ball_weight(), "ounces")

print("\n-- (d) With args, with return --")
points = total_points(5, 2)
print("Total points after 5 wins and 2 losses =", points)


# ============================================================
# 2. TYPES OF ARGUMENTS
# ============================================================
print("\n========== 2. TYPES OF ARGUMENTS ==========")

# (a) Required / Positional Arguments
def player_info(name, jersey):
    print("Player:", name, "| Jersey No.:", jersey)

print("-- Required Arguments --")
player_info("Virat Kohli", 18)

# (b) Keyword Arguments
print("\n-- Keyword Arguments --")
player_info(jersey=10, name="Sachin Tendulkar")

# (c) Default Arguments
def team(name, sport="Cricket"):
    print("Team:", name, "| Sport:", sport)

print("\n-- Default Arguments --")
team("India")                  # uses default sport
team("Brazil", "Football")     # overrides default

# (d) Variable-length Arguments (*args) - tuple
# Passing any number of players to a team
def squad(*players):
    print("Squad members:", end=" ")
    for p in players:
        print(p, end=", ")
    print()
    print("Total players:", len(players))

print("\n-- Variable-length Arguments (*args) --")
squad("Rohit", "Rahul", "Hardik")
squad("Messi", "Ronaldo", "Neymar", "Mbappe", "Benzema")

# (e) Keyword Variable-length Arguments (**kwargs) - dictionary
def match_details(**info):
    for key, value in info.items():
        print(key, "=", value)

print("\n-- Keyword Variable-length Arguments (**kwargs) --")
match_details(venue="Wankhede", match_no=45, result="India won by 5 wickets")


# ============================================================
# 3. COMBINING FUNCTIONS IN A SPORTS TOURNAMENT
# ============================================================
print("\n========== 3. SPORTS TOURNAMENT (All concepts together) ==========")

# Default arguments
def register_team(name, members=11):
    print("Team", name, "registered with", members, "players.")

# *args - collect scores of all matches
def total_score(team, *scores):
    total = 0
    for s in scores:
        total += s
    print(team, "total score across matches =", total)
    return total

# **kwargs - store tournament details
def tournament_info(**details):
    print("Tournament Details:")
    for k, v in details.items():
        print("  ", k, ":", v)

# Function with return value used by another function
def average_score(team, *scores):
    total = sum(scores)
    avg = total / len(scores)
    print(team, "average score =", round(avg, 2))
    return avg

register_team("India")
register_team("Australia", 12)

total_score("India", 289, 320, 350)
average_score("India", 289, 320, 350)

tournament_info(name="World Cup",
                year=2023,
                host="India",
                teams=10)


# ============================================================
# 4. RECURSION (Function calling itself) - SPORTS THEME
# ============================================================
print("\n========== 4. RECURSION - COUNTDOWN TO MATCH ==========")

def countdown(seconds):
    if seconds == 0:
        print("MATCH START! Let the game begin!")
    else:
        print("Countdown:", seconds)
        countdown(seconds - 1)

countdown(3)

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("SUMMARY OF FUNCTIONS AND ARGUMENTS")
print("=" * 60)
print("1. TYPES OF FUNCTIONS")
print("   - no args, no return")
print("   - with args, no return")
print("   - no args, with return")
print("   - with args, with return")
print("2. TYPES OF ARGUMENTS")
print("   - Required (positional) arguments")
print("   - Keyword arguments")
print("   - Default arguments")
print("   - Variable-length *args (tuple)")
print("   - Keyword variable-length **kwargs (dict)")
print("3. Recursion - function calling itself")
print("=" * 60)
