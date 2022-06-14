import sys
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 오늘도 또 개발자 분들이 쉽게 만든 모듈을 써 볼게요~~~
import pyupbit

form_class = uic.loadUiType('ui/btcprice.ui')[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # "너네 식구 다 불러" (자소서 - 협동, 리더십 강조)
        self.setupUi(self)  # 이래야 form_class ui로 사용 ㄱㄴ

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.requestPrice) #이 코드로 하면 1000밀리초(1초)마다 자동으로 가격 호출.

        #self.price_button.clicked.connect(self.requestPrice) #이 코드로 하면 버튼 누를 때마다 가격 호출.

    def requestPrice(self):
        coinPrice = pyupbit.get_current_price("KRW-BTC")
        self.price_label.setText(f"{coinPrice:,.0f}원") # 잘 했는데도 왜 에러 나지? 싶으면 대부분 자료형 에러다.
        # f string은 정말 편하다! :,는 3자리마다 , 찍으라는 얘기고, .0f는 소수점 아래 자리를 없애라는 거다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
