''' this module provide model to manage the contacts table '''

from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlTableModel



class ContactModel:

    def __init__(self):
        self.model = self._create_model()


    @staticmethod
    def _create_model():
        ''' create and setup model'''
        table_model = QSqlTableModel()
        table_model.setTable('contacts')
        table_model.setEditStrategy(QSqlTableModel.OnFieldChange)
        table_model.select()
        headers = ('ID' , 'Name' , 'Job' , 'Email')

        for column_index , header in enumerate(headers):
            table_model.setHeaderData(column_index , Qt.Horizontal , header)

        return table_model
    



    def add_contact(self, data):
        '''add contact to database '''

        rows = self.model.rowCount()
        self.model.insertRows(rows , 1)
        for column ,field in enumerate(data):
            self.model.setData(self.model.index(rows , column + 1) ,field)
        
        self.model.submitAll()
        self.model.select()


    def delete_contact(self,row):
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clear_contacts(self):
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0 , self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()