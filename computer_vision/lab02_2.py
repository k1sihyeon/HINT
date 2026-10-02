import sys
from pathlib import Path

import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton


class ImageWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("이미지 처리 실습")
        self.setGeometry(300, 300, 640, 540)

        image_path = Path(__file__).parent / "data" / "lenna.png"
        self.image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
        if self.image is None:
            raise FileNotFoundError(f"이미지를 읽을 수 없습니다: {image_path}")

        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 10, 620, 450)
        self.image_label.setScaledContents(True)
        self.image_label.setPixmap(self._to_pixmap(self.image))

        grayscale_button = QPushButton("흑백 이미지", self)
        grayscale_button.setGeometry(90, 475, 130, 35)
        grayscale_button.clicked.connect(self.convert_to_grayscale)

        edge_button = QPushButton("엣지 검출", self)
        edge_button.setGeometry(255, 475, 130, 35)
        edge_button.clicked.connect(self.detect_edges)

        original_button = QPushButton("원본 복원", self)
        original_button.setGeometry(420, 475, 130, 35)
        original_button.clicked.connect(self.restore_original)

    @staticmethod
    def _to_pixmap(image: np.ndarray) -> QPixmap:
        if image.ndim == 2:
            height, width = image.shape
            qimage = QImage(
                image.data, width, height, image.strides[0], QImage.Format_Grayscale8
            )
        else:
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, _ = rgb_image.shape
            qimage = QImage(
                rgb_image.data, width, height, rgb_image.strides[0], QImage.Format_RGB888
            )
        return QPixmap.fromImage(qimage.copy())

    def convert_to_grayscale(self) -> None:
        grayscale = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image_label.setPixmap(self._to_pixmap(grayscale))

    def detect_edges(self) -> None:
        grayscale = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(grayscale, 100, 200)
        self.image_label.setPixmap(self._to_pixmap(edges))

    def restore_original(self) -> None:
        self.image_label.setPixmap(self._to_pixmap(self.image))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageWindow()
    window.show()
    sys.exit(app.exec_())