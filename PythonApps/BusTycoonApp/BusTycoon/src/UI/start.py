from src.UI.ui import BusAppUI
from src.repository.busrepo import BusRepository
from src.service.busservice import BusService


if __name__ == "__main__":
    repository = BusRepository()
    service = BusService(repository)

    app_ui = BusAppUI(repository, service)
    app_ui.run()