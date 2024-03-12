import random

class TournamentService:
    @staticmethod
    def create_pairings(players):
        pairings = []
        while len(players) >= 2:
            pair = (players.pop(), players.pop())
            pairings.append(pair)
        return pairings

    @staticmethod
    def play_game(player1, player2):
        winner = random.choice([player1, player2])
        winner.strength += 1
        return winner

    @staticmethod
    def play_round(players, ui):
        pairings = TournamentService.create_pairings(players)
        winners = []
        for player1, player2 in pairings:
            ui.display_game(player1, player2)
            winner_input = ui.get_winner_input()
            winner = player1 if winner_input == 1 else player2
            winners.append(winner)
            ui.display_winner(winner)
        return winners