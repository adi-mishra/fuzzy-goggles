import logging

"""
Contract to be implemented by data store to add or retrieve data.
"""


class DataStore:
    """
    Check if data store has saved item that can be identified by data identifier.
    """

    def hasItem(self, dataIdentifier):
        logging.error("getItem method of DataStore class has not implemented")
        raise NotImplementedError("Unimplemeted method")
