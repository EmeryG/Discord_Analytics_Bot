import mysql.connector

connection = mysql.connector.connect(
                            user='admin',
                            password='password',
                            host='host.docker.internal'
                                    )