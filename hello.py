import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

class HelloWorldApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        # Create a label widget
        label = QLabel('Hello, World!', self)
        
        # Add the label to the layout
        layout.addWidget(label)
        
        # Set the layout for the main window
        self.setLayout(layout)
        
        # Set the main window title
        self.setWindowTitle('PyQt5 Hello World')
        
        # Set the window size
        self.resize(300, 200)

if __name__ == '__main__':
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    
    # Create an instance of the application's main window
    ex = HelloWorldApp()
    
    # Show the main window
    ex.show()
    
    # Start the application's event loop
    sys.exit(app.exec_())
