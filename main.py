from mainwindow import *


def main():
    app = QApplication(sys.argv)
    mw = mainwindow()
    mw.show()

    # adw = addWindow()
    # adw.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()