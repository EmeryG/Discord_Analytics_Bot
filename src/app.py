import json, schema, mysql.connector

connection = mysql.connector.connect(
                            user='admin',
                            password='password',
                            host='host.docker.internal'
                                    )
print(schema.get_role_names())