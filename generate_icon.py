import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import (QPainter, QColor, QIcon, QPixmap, QFont, 
                          QLinearGradient, QBrush, QPainterPath, QPen)
from PySide6.QtCore import Qt, QRectF, QPointF

def create_icon():
    app = QApplication(sys.argv)
    
    # Create a 512x512 pixmap for high quality
    pixmap = QPixmap(512, 512)
    pixmap.fill(Qt.transparent)
    
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    
    # Create background gradient
    gradient = QLinearGradient(0, 0, 512, 512)
    gradient.setColorAt(0.0, QColor("#1a237e"))   # Dark blue
    gradient.setColorAt(1.0, QColor("#0d47a1"))   # Deep blue
    
    # Draw rounded rectangle background
    painter.setBrush(QBrush(gradient))
    painter.setPen(Qt.NoPen)
    painter.drawRoundedRect(QRectF(20, 20, 472, 472), 60, 60)
    
    # Draw a dumbbell/fitness icon in white
    painter.setPen(QPen(QColor("#ffffff"), 24))
    painter.setBrush(Qt.NoBrush)
    
    # Dumbbell bar (horizontal)
    painter.drawLine(QPointF(136, 256), QPointF(376, 256))
    
    # Dumbbell weights (left)
    painter.setBrush(QColor("#ffffff"))
    painter.drawRoundedRect(QRectF(86, 216, 60, 80), 15, 15)
    painter.drawRoundedRect(QRectF(56, 186, 50, 140), 15, 15)
    
    # Dumbbell weights (right)
    painter.drawRoundedRect(QRectF(366, 216, 60, 80), 15, 15)
    painter.drawRoundedRect(QRectF(406, 186, 50, 140), 15, 15)
    
    # Draw a heart pulse line (EKG line) on top of the dumbbell
    painter.setPen(QPen(QColor("#4fc3f7"), 10))
    painter.setBrush(Qt.NoBrush)
    
    # EKG line path
    points = [
        QPointF(136, 220), QPointF(200, 220), QPointF(220, 190),
        QPointF(240, 270), QPointF(260, 230), QPointF(280, 230),
        QPointF(300, 260), QPointF(320, 200), QPointF(340, 220),
        QPointF(376, 220)
    ]
    painter.drawPolyline(points)
    
    # Draw "KN" text at the bottom
    font = QFont("Arial", 72)
    font.setBold(True)
    painter.setFont(font)
    painter.setPen(QColor("#ffffff"))
    painter.drawText(QRectF(0, 340, 512, 100), Qt.AlignCenter, "KN")
    
    painter.end()
    
    # Save as ICO file (for Windows desktop icon)
    pixmap.save("kn_fitness_pro.ico", "ICO")
    
    # Save as PNG
    pixmap.save("kn_fitness_pro.png", "PNG")
    
    # Save as ICNS (for macOS)
    pixmap.save("kn_fitness_pro.icns", "ICNS")
    
    print("Icon created successfully!")
    print("Files saved: kn_fitness_pro.ico, kn_fitness_pro.png, kn_fitness_pro.icns")
    
    return QIcon(pixmap)

if __name__ == "__main__":
    icon = create_icon()
    app = QApplication.instance()
    if app:
        app.exit()
    sys.exit(0)