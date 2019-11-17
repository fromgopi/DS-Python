from designpatterns.creational.factoryPatter.database_connection.database_factory import Database


class MysqlServer(Database):
    """Mysql Server."""

    def connection(self):
        """
        Method which returns Mysql Server connection object.
        :return: Mysql Connection object.
        """
        return "Mysql Server connected."
