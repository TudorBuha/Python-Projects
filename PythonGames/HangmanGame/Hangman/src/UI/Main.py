from src.Repository.SentenceRepo import SentenceRepository
from src.Service.HangmanService import HangmanService
from src.UI.UI import HangmanConsoleUI

def main():
    repo = SentenceRepository('sentences.txt')
    service = HangmanService(repo)
    ui = HangmanConsoleUI(service)
    ui.start()

if __name__ == '__main__':
    main()
