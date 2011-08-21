# github.com/lastkarrde
# 21.8.11

import sys

from PySide.QtCore import QUrl
from PySide.QtGui import QApplication, QGridLayout, QWidget
from PySide.QtWebKit import QWebView

class Event(QWidget):

    def __init__(self, parent=None):
        super(Event, self).__init__(parent)

        self.setWindowTitle('loadFinished Event')


        url = QUrl('https://www.torproject.org/')

        self.webView = QWebView()
        self.webView.setUrl(url)

        page = self.webView.page()
        frame = page.mainFrame()

        frame.loadFinished.connect(self.load_finished)
    

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.webView)

        self.setLayout(self.mainLayout)


    def load_finished(self):
        print 'load has finished'

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    basic = Event()
    basic.show()
    
    sys.exit(app.exec_())

