''' this module provide a database connection'''


from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase , QSqlQuery



def _create_contacts_table():
    ''' create the contacts table in database'''
    create_table_query = QSqlQuery()
    return create_table_query.exec(
    '''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )
    ''')



def create_connection(database_name):
    ''' create and open database '''

    connection = QSqlDatabase.addDatabase('QSQLITE')
    connection.setDatabaseName(database_name)

    if not connection.open():
        QMessageBox.warning(
            None,
            'Contact',
            f'Database Error : {connection.lastError().text()}'
        )
        return False
    _create_contacts_table()
    return True