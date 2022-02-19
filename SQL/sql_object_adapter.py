from SQL.psql_operations import PSQLOperations
from SQL.sql_operations import SQLOperations


class SqlObjectAdapter:

    @staticmethod
    def return_sql():
        return PSQLOperations()
        #return SQLOperations()

