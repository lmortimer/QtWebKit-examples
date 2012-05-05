basic.py
--------
The most basic demonstration of a *QWebView*.

event.py
--------
Demonstrates how to listen for an event, specifically *QWebFrame.loadFinished()*.

useragent.py
------------
Defines a class which extends *QWebPage*, overrides *setUserAgentForUrl()* method, defines a custom user agent on all requests. 

settings.py
-----------
Shows how to enable and disable various settings including the Web Inspector/Debugger, Javascript, Local Storage and Plugins (Flash).

map/map.py
----------
Demonstrates passing data from Python into the Javascript context of the QWebView. Takes the location specified in the *QLineEdit* and passes it to the Google Map loaded in the HTML.
