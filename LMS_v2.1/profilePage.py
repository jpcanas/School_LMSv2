from PyQt6.QtWidgets import QFrame, QPushButton, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

from PyQt6.uic import loadUi

from absPath import resource_path


class Profile(QFrame):
    def __init__(self):
        super(Profile, self).__init__()
        # Load the UI file
        loadUi(resource_path('ui\\profile.ui'), self)

        self.profileWidgets()

    def profileWidgets(self):
        self.profileDisplay = self.findChild(QFrame, "disProfFrame")
        self.sidebar = self.findChild(QFrame, "inputProfFrame")
        self.sideSpacer = self.findChild(QFrame, "sideFrame")
        self.hide_sideBtn = self.findChild(QPushButton, "hideSideBtn")
        self.show_sideBtn = self.findChild(QPushButton, "showSideBtn")

        self.hide_sideBtn.clicked.connect(lambda: self.show_hide_Sidebar())
        self.show_sideBtn.clicked.connect(lambda: self.show_hide_Sidebar())

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.profileDisplay.setGraphicsEffect(self.shadow)

        # keep tracks of hidden/show sidebar
        self.sidebarShow = True

        # Hide side spacer by default
        self.sideSpacer.hide()

    def show_hide_Sidebar(self):
        if self.sidebarShow:
            self.sidebar.hide()
            self.sideSpacer.show()
            self.sidebarShow = False
        else:
            self.sidebar.show()
            self.sideSpacer.hide()
            self.sidebarShow = True




