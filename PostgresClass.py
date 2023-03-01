"""
PostgresClass that handles connection to the PostgreSQL server
"""

import psycopg2
import psycopg2.extras
from datetime import datetime


class PostgresClass:
    def __init__(self):
        self.user = 'postgres'
        self.password = 'postgres'
        self.host = 'localhost'
        self.port = '5432'
        self.dbname = 'postgres'
        self.conn = None

    def connect(self):

        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)

        except psycopg2.Error as e:
            print("Unable to connect to the database")
            print('The error is: ', e)

    def add_message(self, message):
        curr = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        curr.execute(""" CREATE TABLE IF NOT EXISTS user_logins(
                                user_id varchar(128),
                                device_type varchar(32),
                                masked_ip varchar(256),
                                masked_device_id varchar(256),
                                locale varchar(32),
                                app_version integer,
                                create_date date
                                ); """)

        insert_query = ('INSERT INTO user_logins(user_id, \
                                            device_type, \
                                            masked_ip, \
                                            masked_device_id, \
                                            locale, \
                                            app_version, \
                                            create_date) \
                    VALUES (%s, %s, %s, %s, %s, %s, TO_DATE(%s,\'YYYYMMDD\'));')

        try:
            curr.execute(insert_query, (message['user_id'],
                                        message['device_type'],
                                        message['masked_ip'],
                                        message['masked_device_id'],
                                        message['locale'],
                                        str(message['app_version']),
                                        datetime.now().strftime("%Y-%m-%d")))
        except psycopg2.Error as e:
            print('The error is: ', e)
        self.conn.commit()
