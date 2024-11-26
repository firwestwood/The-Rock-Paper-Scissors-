import random

def player(prev_play, opponent_history=[]):
    if prev_play == "":
        # No previous play, choose randomly for the first move
        return random.choice(["R", "P", "S"])
    
    # Track opponent's moves
    if prev_play != "":
        opponent_history.append(prev_play)

    # If opponent played Rock, play Paper
    if prev_play == "R":
        return "P"
    # If opponent played Paper, play Scissors
    elif prev_play == "P":
        return "S"
    # If opponent played Scissors, play Rock
    else:
        return "R"
