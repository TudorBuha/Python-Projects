from src.domain.Player import *
from src.service.PlayerService import *
from src.repository.PlayerRepo import *
from src.ui.UI import *

def main():
    player_repo = PlayerRepository()
    player_repo.read_players('players.txt')
    players = player_repo.get_players()

    TournamentUI.display_players(players)

    num_players = len(players)
    if num_players & (num_players - 1):  # Check if the number of players is not a power of two
        qualifying_round_name = 'Qualifications'
        TournamentUI.display_round(qualifying_round_name)
        winners = TournamentService.play_round(players, TournamentUI)
        players = winners

    while len(players) > 1:
        if len(players) == 2:
            round_name = 'Final'
        elif len(players) == 4:
            round_name = 'Semifinals'
        else:
            round_name = f'Last {len(players)}'

        TournamentUI.display_round(round_name)
        winners = TournamentService.play_round(players, TournamentUI)
        players = winners

    print("\nTournament ended. Winner:", players[0].name)

if __name__ == "__main__":
    main()