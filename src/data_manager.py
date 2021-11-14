from discord import DEFAULT_GUILD
from db import db
import plot

def get_user_info():
    user_list = DEFAULT_GUILD.get_users()
    
    user_map = []
    
    for user in user_list:
        user_info = user['user']
        
        user_map.append({
                    'user_id': user_info['id'], 
                    'roles': user['roles'],
                    'username': user_info['username'], 
                    'nick': user['nick']
                        })
    
    return user_map

def get_role_names():
    role_list = DEFAULT_GUILD.get_roles()
    
    role_name_map = {}
    
    for role in role_list:
        role_name_map[role['id']] = role['name']
    
    return role_name_map

def send_group_counts():
    groups = db.get_groups()
    
    for group in groups.values():
        send_group_count(group)
    
def send_group_count(group):
    users = get_user_info()
    
    role_counts = {}
    
    for user in users:
        for role in group:
            if role['id'] in user['roles']:
                if role['label'] in role_counts.keys():
                    role_counts[role['label']] += 1
                else:
                    role_counts[role['label']] = 1
    
    plot.normalize_plot(role_counts, 'type_stats')
    
    DEFAULT_GUILD.send_image('type_stats')
    
    
    