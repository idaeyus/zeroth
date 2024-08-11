import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import requests

def download_image_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return QPixmap()
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
        return None

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Colde")
        self.setGeometry(180, 50, 1000, 650)

        image_url = "https://pbs.twimg.com/media/GTVADSjXkAAML1R?format=jpg&name=small"
        print(f"Downloading image from: {image_url}")
        image_data = requests.get(image_url).content
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)
        
        if not pixmap.isNull():
            self.setWindowIcon(QIcon(pixmap))
        else:
            print("Failed to set window icon.")

        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("Your_Path_To_zeroth.html"))

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("background-color: black; color: black; border: 1px solid black;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
