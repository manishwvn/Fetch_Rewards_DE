"""
SQSClass creates a connection to the AWS SQS service and provides methods to send and receive messages.    
"""

import boto3
import json
from botocore import UNSIGNED
from botocore.client import Config


class SQSClass:
    def __init__(self):
        self.sqs = None
        self.queue_url = 'http://localhost:4566/000000000000/login-queue'
        self.region = 'us-east-1'

    def connect(self):
        self.sqs = boto3.client(
            'sqs',
            endpoint_url=self.queue_url,
            region_name=self.region,
            config=Config(signature_version=UNSIGNED))

    def receive_message(self):

        response = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            AttributeNames=['All'],
            MaxNumberOfMessages=1,
            WaitTimeSeconds=1
        )

        if 'Messages' not in response:
            return None

        messages = []

        for message in response['Messages']:
            messages.append(json.loads(message['Body']))
            self.sqs.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )

        return messages
