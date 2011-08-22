# github.com/lastkarrde
# 22.8.11

import sys

from PySide.QtCore import QUrl
from PySide.QtGui import QApplication, QGridLayout, QWidget
from PySide.QtWebKit import QWebSettings, QWebView

class Settings(QWidget):

    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)

        self.setWindowTitle('Settings, Debugger Application')

        url = QUrl('http://www.bitcoin.org/')

        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.DeveloperExtrasEnabled, True)

        # more settings
        # http://pyside.org/docs/pyside/PySide/QtWebKit/QWebSettings.html#detailed-description

        self.webView = QWebView()
        self.webView.setUrl(url)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.webView)

        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    s = Settings()
    s.show()
    
    sys.exit(app.exec_())
