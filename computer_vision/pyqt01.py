import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt 기초 예제')

        # 1. 메인 뮌도우(창)의 위치와 크기 설정
        # setGeometry(x, y, width, height)
        # - x = 300: 모니터 화면 좌측 상단(0,0)을 기준, 오른쪽으로 300px 떨어진 위치
        # - y = 300: 모니터 화면 좌측 상단(0,0)을 기준, 아래쪽으로 300px 떨어진 위치
        # - width = 300: 창의 가로 길이 (300px)
        # - height = 200: 창의 세로 길이 (200px)
        
        self.setGeometry(300, 300, 300, 200)    

        # 2. 버튼 위젯 생성 및 위치/크기 설정
        btn = QPushButton('클릭하세요', self)

        # - x = 100: 메인 원도우 내부 좌측 상단을 기준, 오른쪽으로 100px 떨어진 위츠
        # - y = 80: 메인 뮌도우 내부 좌측 상단을 기준, 아래쪽으로 80px 떨어진 위치
        # - width = 100: 버튼의 가로 너비 (100px)
        # - height = 40: 버튼의 세로 높이 (40px)
        btn.setGeometry(100, 80, 100, 40)

        # 3. Signal과 slot 연결 (이벤트 모델)
        # 'clicked' 시그널이 발생하면 'btn_clicked' 슬롯 메서드가 실행됨
        btn.clicked.connect(self.btn_clicked)

    # Slot 메서드 정의
    def btn_clicked(self):
        QMessageBox.information(self, '알림', '버튼이 클릭되었습니다!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())