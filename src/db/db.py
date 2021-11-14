import mysql.connector
import tables

conn = mysql.connector.connect(
                            user='admin',
                            password='password',
                            host='host.docker.internal'
                                    )

tables.verify_table_schema(conn)

def get_roles():
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT role_id FROM stat_groupings")
    
    role_list = list(cursor.fetchall())
    
    return role_list
    
def get_groups():
    cursor = conn.cursor()
    groups = {}
    
    cursor.execute("SELECT * FROM stat_groupings")
    
    for row in cursor.fetchall():
        group_id = row.group_id
        if group_id in groups.keys():
            groups[group_id]['roles'].append({ "id": row.role_id, "label": row.label })
        else:
            groups[group_id] = [{ "id": row.role_id, "label": row.label }]
            
    cursor.close()
    return groups