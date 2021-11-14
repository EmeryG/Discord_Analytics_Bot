import mysql.connector
from db import tables

conn = mysql.connector.connect(
                            user='root',
                            password='password',
                            host='host.docker.internal',
                            database="db"
                                    )

tables.verify_table_schema(conn)

def insert_default_groups():
    cursor = conn.cursor()
    sql = """
        INSERT INTO stat_groupings (group_id, role_id, label)
        VALUES (%s, %s, %s)
        """
    values = [
        ( 1, '848352240481337364', "ILE"),
        ( 1, '848352377383288842', "SEI"),
        ( 1, '848352529384341504', "LII"),
        ( 1, '848362004028850176', "LIE"),
        ( 1, '848360647946141736', "ESE"),
        ( 1, '848361168342351883', "SLE"),
        ( 1, '848361273330368523', "IEI"),
        ( 1, '848360732319547413', "IEE"),
        ( 1, '848360926369677322', "LSE"),
        ( 1, '848361372550430731', "LSI"),
        ( 1, '848360831069454336', "SLI"),
        ( 1, '848361457866375210', "EIE"),
        ( 1, '848361019167735868', "EII"),
        ( 1, '848361536673939456', "SEE"),
        ( 1, '848361621239234571', "ILI"),
        ( 1, '848361883408269363', "ESI"),
        ( 2, '855964737019183104', "Alpha"),
        ( 2, '855965084341633034', "Beta"),
        ( 2, '855965669925060608', "Gamma"),
        ( 2, '855965327099428885', "Delta"),
        ( 3, '880588260429139978', "Dominant"),
        ( 3, '880588414339125278', "Creative"),
        ( 3, '880588532228423732', "Normalizing"),
        ( 3, '880588612528373800', "Harmonizing")
    ]
    
    cursor.executemany(sql, values)
    conn.commit()
    
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
        group_id = row[1]
        if group_id in groups.keys():
            groups[group_id].append({ "id": row[2], "label": row[3] })
        else:
            groups[group_id] = [{ "id": row[2], "label": row[3] }]
            
    cursor.close()
    return groups