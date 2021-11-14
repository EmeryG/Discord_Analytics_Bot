def verify_table_schema(conn):
    check_table(conn, { 
        "name": "stat_groupings",
        "cols": [
            { "name": "r_id", "def": "r_id int NOT NULL AUTO_INCREMENT" },
            { "name": "group_id", "def": "group_id int NOT NULL" },
            { "name": "role_id", "def": "role_id varchar(255) NOT NULL"},
            { "name": "label", "def": "label varchar(255) NOT NULL"}
        ]
    })
    
    check_table(conn, { 
        "name": "members",
        "cols": [
            { "name": "u_id", "def": "u_id bigint(255) NOT NULL" },
            { "name": "roles", "def": "roles varchar(255) NOT NULL" },
            { "name": "discord_name", "def": "discord_name varchar(255) NOT NULL"},
            { "name": "server_nick", "def": "server_nick varchar(255)"}
        ]
    })
    
    check_table(conn, { 
        "name": "leave_history",
        "cols": [
            { "name": "u_id", "def": "u_id bigint NOT NULL" },
            { "name": "roles", "def": "roles varchar(255) NOT NULL" },
            { "name": "discord_name", "def": "discord_name varchar(255) NOT NULL"},
            { "name": "server_nick", "def": "server_nick varchar(255)"},
            { "name": "leave_time", "def": "leave_time time(0) NOT NULL"},
            { "name": "rejoin", "def": "rejoin boolean NOT NULL DEFAULT false"}
        ]
    })


def check_table(conn, table):
    if check_table_exist(conn, table["name"]) == False:
        colDef = ""
        
        for i in range(0,len(table["cols"])):
            colDef += table["cols"][i]["def"] + ",\n"
        
        colDef += f"PRIMARY KEY ({table['cols'][0]['name']})"
            
        cursor = conn.cursor()
        cursor.execute(f"""
                CREATE TABLE {table["name"]} (
                    {colDef}
                )
                        """)    
        cursor.close()
    else:
        for col in table["cols"]:
            if check_column_exist(conn, table["name"], col["name"]) == False:
                cursor = conn.cursor()
                cursor.execute(f"""
                        ALTER TABLE {table["name"]},
                        ADD {col["def"]}
                                """) 
                cursor.close()
                

def check_column_exist(conn, tablename, columnname):
    cursor = conn.cursor()
    cursor.execute(f"""
            SELECT COUNT(*)
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE table_name = '{tablename}'
            AND column_name = '{columnname}'
                    """)  
    
    result = cursor.fetchone()[0]
    cursor.close()
    
    if result == 1:
        return True
    elif result == 0:
        return False
    else:
        raise SystemError(f"Amount of existent columns is not 0 or 1: Table {tablename} Column {columnname}")
    
# SQL from feathj at https://stackoverflow.com/questions/17044259/python-how-to-check-if-table-exists
def check_table_exist(conn, tablename):
    cursor = conn.cursor()
    cursor.execute(f"""
            SELECT COUNT(*)
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_NAME = '{tablename}'
                    """)    
    
    result = cursor.fetchone()[0]
    cursor.close()
    
    if result == 1:
        return True
    elif result == 0:
        return False
    else:
        raise SystemError("Amount of existent tables is not 0 or 1: Table " + tablename)

        