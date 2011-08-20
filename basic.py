# github.com/lastkarrde
# 21.8.11

import sys

from PySide.QtCore import QUrl
from PySide.QtGui import QApplication, QGridLayout, QWidget
from PySide.QtWebKit import QWebView

class Basic(QWidget):

    def __init__(self, parent=None):
        super(Basic, self).__init__(parent)

        self.setWindowTitle('Basic Application')

        url = QUrl('http://www.bitcoin.org/')

        self.webView = QWebView()
        self.webView.setUrl(url)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.webView)

        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    basic = Basic()
    basic.show()
    
    sys.exit(app.exec_())
