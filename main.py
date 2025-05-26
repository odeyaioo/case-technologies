import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QSpinBox, QDateEdit, QComboBox, QPushButton, \
    QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Передвижения на складе")
        materialLabel = QLabel("Материал:")
        self.materialEdit = QLineEdit()
        quantityLabel = QLabel("Количество:")
        self.quantitySpin = QSpinBox()
        self.quantitySpin.setRange(0, 1000000)
        dateLabel = QLabel("Дата:")
        self.dateEdit = QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        typeLabel = QLabel("Тип:")
        self.typeCombo = QComboBox()
        self.typeCombo.addItems(["Поступление", "Отгрузка"]
                                )
        addButton = QPushButton("Добавить")
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Материал", "Количество", "Дата", "Тип"]
                                             )
        inputLayout = QHBoxLayout()
        inputLayout.addWidget(materialLabel)
        inputLayout.addWidget(self.materialEdit)
        inputLayout.addWidget(quantityLabel)
        inputLayout.addWidget(self.quantitySpin)
        inputLayout.addWidget(dateLabel)
        inputLayout.addWidget(self.dateEdit)
        inputLayout.addWidget(typeLabel)
        inputLayout.addWidget(self.typeCombo)
        inputLayout.addWidget(addButton)
        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(inputLayout)
        mainLayout.addWidget(self.table)
        addButton.clicked.connect(self.add_record)

    def add_record(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(self.materialEdit.text()))
        self.table.setItem(row, 1, QTableWidgetItem(str(self.quantitySpin.value())))
        self.table.setItem(row, 2, QTableWidgetItem(
            self.dateEdit.date().toString("yyyy-MM-dd")))
        self.table.setItem(row, 3, QTableWidgetItem(
            self.typeCombo.currentText()))
        self.materialEdit.clear()
        self.quantitySpin.setValue(0)
        self.dateEdit.setDate(self.dateEdit.date())
        self.materialEdit.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
