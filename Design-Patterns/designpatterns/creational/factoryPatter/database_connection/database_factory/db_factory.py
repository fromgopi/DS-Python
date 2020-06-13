# pylint: disable=no-self-use,too-few-public-methods
"""Main Factory handle."""


class DbFactory:
    """Factory Handle."""
    def get_database_connection(self, database_object):
        """
        Factory method which will decide which db object to returned.
        :param database_object:
        :return: db object of that type.
        """
        return database_object.connection()
