''' this module provide views to manage the contacts table'''



from PySide6.QtCore import Qt

from PySide6.QtWidgets import (QAbstractItemView ,QHBoxLayout , QMainWindow , QWidget , QPushButton , QTableView , QVBoxLayout 
                               ,QDialog , QDialogButtonBox,QFormLayout , QLineEdit , QMessageBox,)

from .model import ContactModel


class Window(QMainWindow):
    ''' Main Window '''

    def __init__(self , parent = None):
        super().__init__(parent)
        
        self.setWindowTitle('Contacts')
        self.resize(550 , 250 )
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.contact_model = ContactModel()
        self.setup_ui()


    def setup_ui(self):
        self.table = QTableView()
        self.table.setModel(self.contact_model.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        # Create Button
        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.open_add_dialog)
        self.delete_button = QPushButton('Delete')
        self.delete_button.clicked.connect(self.delete_contact)
        self.clear_all_button = QPushButton('Clear All')
        self.clear_all_button.clicked.connect(self.clear_contacts)

        layout = QVBoxLayout()

        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addStretch()
        layout.addWidget(self.clear_all_button)
        
        self.layout.addWidget(self.table)

        self.layout.addLayout(layout)

    
    def open_add_dialog(self):
        dialog =  AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contact_model.add_contact(dialog.data)
            self.table.resizeColumnsToContents()

    def delete_contact(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return

        message_box = QMessageBox.warning(
            self,
            'Warning!!',
            'do you want to remove the selected contact ?',
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if message_box == QMessageBox.Ok:
            self.contact_model.delete_contact(row)

    def clear_contacts(self):

        message_box = QMessageBox.warning(
            self,
            'Warning!!',
            'do you want to remove all contacts ?',
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if message_box == QMessageBox.Ok:
            self.contact_model.clear_contacts()





class AddDialog(QDialog):
    ''' add contact dialog '''

    def __init__(self , parent = None):
        super().__init__(parent = parent)
        self.setWindowTitle('Add Contact')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        self.setup_ui()

    

    def setup_ui(self):
        ''' setup the add contact dialog '''

        self.name_field = QLineEdit()
        self.name_field.setObjectName('Name')
        self.job_field = QLineEdit()
        self.job_field.setObjectName('Job')
        self.email_field = QLineEdit()
        self.email_field.setObjectName('Email')

        layout = QFormLayout()

        layout.addRow('Name:' , self.name_field)
        layout.addRow('Job:' , self.job_field)
        layout.addRow('Email:' , self.email_field)
        self.layout.addLayout(layout)

        self.button_box = QDialogButtonBox(self)
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(
            QDialogButtonBox.Ok| QDialogButtonBox.Cancel
        )
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)


    def accept(self):
        ''' accept the data provided in dialog '''
        self.data = []
        for field in (self.name_field , self.job_field , self.email_field):
            if not field.text():
                QMessageBox.critical(
                    self,
                    'Error',
                    f'You Must Prodive The Contact {field.objectName()}',
                )
                self.data = None
                return
            

            self.data.append(field.text())

        super().accept()

        
            


       



