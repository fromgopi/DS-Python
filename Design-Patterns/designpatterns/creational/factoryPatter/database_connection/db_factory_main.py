from designpatterns.creational.factoryPatter.database_connection.database_factory import DbFactory
from designpatterns.creational.factoryPatter.database_connection.mysql_db import MysqlServer
from designpatterns.creational.factoryPatter.database_connection.oracle_db import OracleServer

if __name__ == '__main__':
    db_factory = DbFactory()
    print(db_factory.get_database_connection(MysqlServer()))
    print(db_factory.get_database_connection(OracleServer()))