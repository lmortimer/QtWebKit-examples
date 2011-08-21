# github.com/lastkarrde
# 21.8.11

import sys

from PySide.QtCore import QUrl
from PySide.QtGui import QApplication, QGridLayout, QWidget
from PySide.QtWebKit import QWebPage, QWebView

class CustomWebPage(QWebPage):

    def __init__(self, parent=None):
        super(CustomWebPage, self).__init__(parent)

    def userAgentForUrl(self, url):
        return "Stork[Gm]"

class UserAgentExample(QWidget):

    def __init__(self, parent=None):
        super(UserAgentExample, self).__init__(parent)

        self.setWindowTitle('Custom User Agent Example')

        url = QUrl('http://getmyuseragent.com')
        page = CustomWebPage()

        self.webView = QWebView()
        self.webView.setPage(page)
        self.webView.setUrl(url)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.webView)

        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    uae = UserAgentExample()
    uae.show()
    
    sys.exit(app.exec_())
