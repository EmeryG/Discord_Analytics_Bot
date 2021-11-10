from discord import DEFAULT_GUILD

def get_user_info():
    user_list = DEFAULT_GUILD.get_users()
    
    user_map = []
    
    for user in user_list:
        user_info = user['user']
        
        user_map.append({
            'user_id': user_info['id'], 
            'username': user_info['username'], 
            'nick': user['nick'],
            'roles': user['roles']})
    
    return user_map

def get_role_names():
    role_list = DEFAULT_GUILD.get_roles()
    
    role_name_map = []
    
    for role in role_list:
        role_name_map.append({
            'id': role['id'],
            'name': role['name'],
        })
    
    return role_name_map
