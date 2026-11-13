#==========================
# WELCOME AND LOGIN SECTION
#==========================

# Display a welcome message to the user
print("Welcome to the Tournament Game")

# Ask the user to enter their username
username = input("Enter username: ")

# Ask the user to enter their password
password = input("Enter password: ")

# Check if the username and password are correct
if username == "admin" and password == "1234":
    print("Login successful")






    # MODE SELECTION SECTION


    # Show the game mode options
    print("Select a game mode:")
    print("1. Single Player (Individual)")
    print("2. Team Mode")

    # Ask the user to choose a mode
    mode = input("Enter 1 or 2: ")


    # DATA STORAGE


    # Allows users to type there names so the game temporaly stores it
    teams = {}

    # List to store individual players
    individual_players = []


    # TEAM MODE

    if mode == "2":
        print("Team Mode selected")

        # Loop so that 4 teams can be entered
        for i in range(4):
            # Ask the user to enter a team name
            team_name = input("Enter team name: ")

            # creates a list for users to type their name
            teams[team_name] = []

            # Loops so 5 players can join each team
            for j in range(5):
                # lets users enter player name
                player_name = input("Enter player name: ")

                # puts the name into the teams list
                teams[team_name].append(player_name)

                # Confirm the players was added
                print("Player added")

        # Show all teams and players
        print("\nTeams and players:")
        for team in teams:
            print(team, ":", teams[team])



    # INDIVIDUAL MODE

    elif mode == "1":
        print("Single Player mode selected")

        # Ask how many individual are playing
        num_players = int(input("How many players? (max 20): "))

        # Loop to add all individual players
        for i in range(num_players):
            # Ask the user to enter a player name
            player_name = input("Enter player name: ")

            # Add player name to players list
            individual_players.append(player_name)

            # Confirm the player was added
            print("Player added")

        # Show all individual players
        print("\nIndividual players:")
        for player in individual_players:
            print(player)


    #show invalid choice if they try to enter something which will not work for a name (e.g. an image)

    else:
        print("Invalid choice")



    # GAMES SECTION

    # List of games
    games = ["Draughts", "Ping Pong", "Football", "Virtual Darts", "Speed Trivia Sprint"]

    # track how many games have been played
    game_count = 0

    # Loop to play 5 games
    while game_count < 5:
        # Display message before starting a game
        print("Selecting a starting game...")

        # Select the current game based on the counter
        current_game = games[game_count]

        # Display the game being played
        print("Now playing:", current_game)

        # (Scoring will be added here later)

        # Display end of game messages
        print("Game finished")
        print("Next game loading...")

        # Increase the game counter
        game_count = game_count + 1

    # display message after all games are completed
    print("All games completed")


    # CREATE SCORE DICTIONARIES


    # stores total scores for teams
    team_scores = {}

    # store total scores for individual players
    individual_scores = {}

    # Set starting scores for teams
    if mode == "2":
        for team in teams:
            team_scores[team] = 0

    # Set starting scores for individuals
    elif mode == "1":
        for player in individual_players:
            individual_scores[player] = 0


    # GAMES AND SCORING


    games = ["Draughts", "Ping Pong", "Football", "Virtual Darts", "Speed Trivia Sprint"]
    game_count = 0

    while game_count < 5:

        print("Selecting a starting game...")
        current_game = games[game_count]
        print("Now playing:", current_game)


        # TEAM MODE SCORING

        if mode == "2":

            # Loop through each team and enter scores
            for team in team_scores:
                score = int(input("Enter score for " + team + ": "))
                team_scores[team] = team_scores[team] + score

            # Display current team scores
            print("Current team scores")
            for team in team_scores:
                print(team)
                print(team_scores[team])


        # INDIVIDUAL MODE SCORING

        elif mode == "1":

            # Loop through each player and enter scores
            for player in individual_scores:
                score = int(input("Enter score for " + player + ": "))
                individual_scores[player] = individual_scores[player] + score

            # Display current individual scores
            print("Current individual scores")
            for player in individual_scores:
                print(player)
                print(individual_scores[player])

        print("Game finished")
        print("Next game loading...")

        game_count = game_count + 1

    print("All games completed")



# CHAMPION SECTION
# Check which mode was played
if mode == "2":

    # store the winning team and highest score
    winner = ""
    highest_score = 0

    # Loop through each team to find the highest score
    for team in team_scores:
        if team_scores[team] > highest_score:
            highest_score = team_scores[team]
            winner = team

    # Display the winning team
    print("Tournament Champion")
    print(winner)
    print("Score")
    print(highest_score)

elif mode == "1":

    # store the winning player and highest score
    winner = ""
    highest_score = 0

    # Loop through each individual player to find the highest score
    for player in individual_scores:
        if individual_scores[player] > highest_score:
            highest_score = individual_scores[player]
            winner = player

    # Display the winning player
    print("Tournament Champion")
    print(winner)
    print("Score")
    print(highest_score)

#==========================
# LOGIN FAILED
# =========================

else:
    print("Login failed")


