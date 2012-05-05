# github.com/lastkarrde
# 21.8.11

import sys

from PySide.QtCore import QUrl
from PySide.QtGui import QApplication, QGridLayout, QLineEdit, QPushButton, QWidget
from PySide.QtWebKit import QWebView


# declare our class which inherits from QWidget (this essentially makes it a window)
class MapApp(QWidget):

    def __init__(self, parent=None):
        # call QWidget's __init__
        super(MapApp, self).__init__(parent)

        self.setWindowTitle('Map Application')

        f = open('map.html', 'r')
        html = f.read()
        f.close()
        
        # declare our QWebView and set the URL to the source of the map.html file.
        # we must also set a URL (which QtWebKit will use if we ask for the URL of the page)
        self.webView = QWebView()
        self.webView.setHtml(html, baseUrl=QUrl('http://local'))
        self.webView.show()
		
        self.location = QLineEdit()
        self.go = QPushButton('Find this location')
        
        self.go.clicked.connect(self.findLocation)

        # set up our layout and add the instance of the QWebView
        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.location)
        self.mainLayout.addWidget(self.go)
        self.mainLayout.addWidget(self.webView)

        self.setLayout(self.mainLayout)
        
      
    def findLocation(self):
        page = self.webView.page()
        frame = page.mainFrame()
        
        # the javascript code to be executed
        functionCall = 'codeAddress("' + self.location.text() + '")'
        
        # execute the javascript code in the webkit instance
        frame.evaluateJavaScript(functionCall)
        
# if our program is being called directly..
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    # instantiate and draw our window
    basic = MapApp()
    basic.show()
    
    sys.exit(app.exec_())
