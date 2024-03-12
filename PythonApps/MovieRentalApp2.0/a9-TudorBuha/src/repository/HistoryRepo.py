from src.domain.HistoryCommand import HistoryCommand


class HistoryRepository:
    def __init__(self):
        self._history = []
        self.history_index = -1

    def add_to_history(self, command: HistoryCommand):
        while len(self._history) > self.history_index + 1:
            self._history.pop()

        self._history.append(command)
        self.history_index += 1

    def get_command(self):
        return self._history[self.history_index]
