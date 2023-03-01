"""
Program that reads messages from an SQS queue and writes them to a PostgreSQL database.    
"""

from SQSClass import SQSClass
from PostgresClass import PostgresClass
from mask_responses import mask_responses as mask

sqs_queue = SQSClass()
sqs_queue.connect()

psdb = PostgresClass()
psdb.connect()


while True:
    messages = sqs_queue.receive_message()
    if messages:
        # for message in messages:
        #     print(message)

        masked_messages = mask(messages)

        # add masked messages to database
        for message in masked_messages:
            psdb.add_message(message)

    else:
        print('No more messages')
        break


# close connection
sqs_queue.sqs.close()
psdb.conn.close()
