# -* encoding: utf-8 *-
from gui import mainwindow, randomdialog
import sys
from PySide import QtGui, QtCore


class MainWindow(QtGui.QMainWindow, mainwindow.Ui_MainWindow):
    counter_value = 0

    def __init__(self, parent=None, app=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.app = app

        # Create related Dialog to be opened in on_actionSettings_triggered
        self.randomDialog = RandomDialog(self)

    @QtCore.Slot()
    def on_increment_clicked(self):
        """This handles clicked() slot for "increment" button. It doesn't need
        any declaration in UI, everything is bound automatically"""
        self.counter_value += 1
        self.counter_label.setText(str(self.counter_value))

    @QtCore.Slot()
    def on_decrement_clicked(self):
        self.counter_value -= 1
        self.counter_label.setText(str(self.counter_value))

    @QtCore.Slot()
    def on_actionSettings_triggered(self):
        self.randomDialog.show()

    @QtCore.Slot()
    def on_actionExit_triggered(self):
        """This handles activation of "Exit" menu action"""
        self.app.exit()


class RandomDialog(QtGui.QDialog, randomdialog.Ui_Dialog):
    def __init__(self, parent=None):
        super(RandomDialog, self).__init__(parent)
        self.setupUi(self)

    @QtCore.Slot()
    def on_buttonBox_helpRequested(self):
        msgbox = QtGui.QMessageBox()
        msgbox.setWindowTitle('Example dialog')
        msgbox.setText('There is no help for you, my friend :^)')
        msgbox.exec_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow(app=app)
    window.show()
    sys.exit(app.exec_())
