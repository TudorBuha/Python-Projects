class TournamentUI:
    @staticmethod
    def display_players(players):
        sorted_players = sorted(players, key=lambda x: x.strength, reverse=True)
        for player in sorted_players:
            print(player)

    @staticmethod
    def display_round(round_name):
        print(f"\nCurrent Round: {round_name}")

    @staticmethod
    def display_game(player1, player2):
        print(f"\nGame: {player1.name} vs. {player2.name}")

    @staticmethod
    def display_winner(winner):
        print(f"Winner: {winner.name}")

    @staticmethod
    def get_winner_input():
        return int(input("Enter the winner (1 or 2): "))
