import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

now = QDate.currentDate()

class MyApp(QMainWindow):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      cpbtn = QPushButton('카드 결제', self)
      cpbtn.move(50, 50)
      cpbtn.resize(cpbtn.sizeHint())
      cpbtn.clicked.connect(QCoreApplication.instance().quit)

      ppbtn = QPushButton('현금 결제', self)
      ppbtn.move (150, 50)
      ppbtn.resize(ppbtn.sizeHint())
      ppbtn.clicked.connect(self.cash)

      dateL = QLabel(now.toString(), self)
      font1 = dateL.font()
      font1.setPointSize(20)

      self.statusBar().showMessage('준비됨')
      self.setWindowTitle('매점 결제기')
      self.setGeometry(500, 500, 500, 400)
      self.center()
      self.show()

  def cash(self):
      self.statusBar().showMessage('돈을 넣으십시오')
      self.setWindowTitle('매점 결제기')
      self.setGeometry(500, 500, 500, 400)
      self.center()
      self.show()

  def center(self):
      qr = self.frameGeometry()
      cp = QDesktopWidget().availableGeometry().center()
      qr.moveCenter(cp)
      self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())