"""This is Oracle Server."""
from designpatterns.creational.factoryPatter.database_connection.database_factory import Database


class OracleServer(Database):
    """This is Oracle Server"""

    def connection(self):
        """
        Returns Oracle Server.
        :return: Oracle Server object.
        """
        return "Oracle Server connected."

