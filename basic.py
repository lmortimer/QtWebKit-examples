# github.com/lastkarrde
# 21.8.11

import sys

from PySide.QtCore import QUrl
from PySide.QtGui import QApplication, QGridLayout, QWidget
from PySide.QtWebKit import QWebView


# declare our class which inherits from QWidget (this essentially makes it a window)
class Basic(QWidget):

    def __init__(self, parent=None):
        # call QWidget's __init__
        super(Basic, self).__init__(parent)

        self.setWindowTitle('Basic Application')

        url = QUrl('http://www.bitcoin.org/')

        # declare our QWebView and set the URL. The URL must be an instance of QUrl, not a string
        self.webView = QWebView()
        self.webView.setUrl(url)

        # set up our layout and add the instance of the QWebView
        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.webView)

        self.setLayout(self.mainLayout)

# if our program is being called directly..
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    # instantiate and draw our window
    basic = Basic()
    basic.show()
    
    sys.exit(app.exec_())
