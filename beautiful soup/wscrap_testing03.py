#this code ref form : https://www.youtube.com/watch?v=FSH77vnOGqU
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request

print(sys.argv) # ['wscrap_testing03.py']

class Client(QWebPage):
    def __init__(self,url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source,'lxml')
js_test = soup.find('p',class_='jstest')
print(js_test.text)

'''
โดยปกติหากไม่ใช้ web browser จะเห็นคนว่า y u bad to แต่หากเป็น web browser จะได้คำว่า Look at you shinin! แทน
นี่เป็นวิธีที่จะทำให้ scraper มองเห็นเหมือน web browser
Ex.
<p> Javascript (dynamic data) test: </p>
<p class='jstest' id='yesnojs'>y u bad to ? </P>
<script>
    document.getElementById('yesnojs').innerHTML = 'Look at you shinin!';
</script>
'''