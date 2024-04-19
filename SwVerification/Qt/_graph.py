from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class GraphView(QWidget):
    def __init__(self, fig, title):
        super().__init__()
        self.fig = fig
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.toolbar)
        self.setLayout(self.layout)

        self.setWindowTitle(f' {title}')
        self.setWindowIcon(QIcon('./static/icons/graph-icon.png'))

    def __del__(self):
        print(".... GRAPH WINDOW CLOSE.....\n")

    def show_widget(self, main_geometry):
        self.move(main_geometry.center())
        self.show()
        self.activateWindow()