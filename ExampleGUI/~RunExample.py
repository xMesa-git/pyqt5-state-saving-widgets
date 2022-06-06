from PyQt5.QtWidgets import QApplication, QDialog
from WindowGUI import Ui_example_dialog
import sys


class ExampleSavingGuiElements(QDialog, Ui_example_dialog):
    def __init__(self):
        super(ExampleSavingGuiElements, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    win = QApplication(sys.argv)
    app = ExampleSavingGuiElements()
    app.exec_()
