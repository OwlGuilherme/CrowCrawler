import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_CrowCrawler


class CrowCrawler(QMainWindow):
    def __init__(self):
        super().__init__()

        # Instância da classe da interface
        self.ui = Ui_CrowCrawler()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CrowCrawler()
    window.show()
    sys.exit(app.exec_())
