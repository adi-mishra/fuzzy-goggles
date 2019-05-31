from .DataStore import DataStore
import boto3
import logging
from botocore.exceptions import ClientError
from errors.StoreError import StoreError

"""
Data store backed by dynamo db to save and retrieve blacklisted url.
"""


class DynamoDbUrlBlacklistDataStore(DataStore):
    def __init__(self):
        dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
        self._table = dynamodb.Table('UrlBlacklist')

    """
    Check if url is stored as a blacklisted url.
    
    Returns true/false is url is in blacklisted table.
    raises Store error in case of error.
    """

    def hasItem(self, url):
        try:
            response = self._table.get_item(Key={'url': url})
        except ClientError as e:
            logging.warning("Unexpected error occurred when accessing dynamoDB, reason: %s" % e.response)
            raise StoreError("ClientError was raised by dynamo db")
        else:
            logging.debug("GetItem succeeded , url: %s,response: %s" % (url, response))
            if 'Item' in response:
                return True
            else:
                return False

    """
    Add url as a blacklisted url.

    raises Store error in case of error.
    """

    def addItem(self, url):
        try:
            self._table.put_item(Item={'url': url})
        except ClientError as e:
            logging.warning("Unexpected error occurred when accessing dynamoDB, reason: %s" % e.response)
            raise StoreError("ClientError was raised by dynamo db")
