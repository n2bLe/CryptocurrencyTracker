from msilib.schema import Error
import sys 
from googletrans import Translator
from PyQt6.QtWidgets import * 
from PyQt6 import uic   
import requests


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui',self)
        
        self.comboBox = self.findChild(QComboBox,'comboBox')
        self.comboBox.activated.connect(self.fetch_price)
        self.comboBox.removeItem(3)
        self.coinLabel = self.findChild(QLabel,'coinLabel')
        self.priceLabel = self.findChild(QLabel,'priceLabel')
        self.priceButton = self.findChild(QPushButton,'priceButton')
        self.priceButton.clicked.connect(self.fetch_price)
        self.priceButton.setText('Refresh')
        self.setWindowTitle('Cryptocurrency Price Tracker')
        
        
        

    def fetch_price(self):
        
            item = self.comboBox.currentText()
            headers = {
                'X-CMC_PRO_API_KEY': 'db940677-8bd5-4993-82a9-3b6bc9082a95',
                'Accepts' : 'application/json'
            }
            params = {
                'start' : '1',
                'limit' : '100',
                'convert' : 'USD',
            }
            url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        
            json = requests.get(url,params=params,headers=headers).json()
        
            coins = json['data']
            for i in coins:
                if i['symbol'] == f'{item}':
                    price = str(i['quote']['USD']['price'] )
                    self.priceLabel.setText(f'${price}')
                    self.coinLabel.setText(f'{item} Price : ')




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())