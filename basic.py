import sys

from PySide import QtCore, QtGui, QtWebKit


class Basic(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Basic, self).__init__(parent)

        self.setWindowTitle('Basic Application')

        url = QtCore.QUrl('http://www.bitcoin.org/')

        self.webView = QtWebKit.QWebView()
        self.webView.setUrl(url)

        self.mainLayout = QtGui.QGridLayout()
        self.mainLayout.addWidget(self.webView)

        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)

    basic = Basic()
    basic.show()
    
    sys.exit(app.exec_())
