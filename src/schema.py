from discord import DEFAULT_GUILD

specified_roles = {
    '848352240481337364': 0,
    '848352377383288842': 0,
    '848352529384341504': 0,
    '848362004028850176': 0,
    '848360647946141736': 0,
    '848361168342351883': 0,
    '848361273330368523': 0,
    '848360732319547413': 0,
    '848360926369677322': 0,
    '848361372550430731': 0,
    '848360831069454336': 0,
    '848361457866375210': 0,
    '848361019167735868': 0,
    '848361536673939456': 0,
    '848361621239234571': 0,
    '848361883408269363': 0
}

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
    
    role_name_map = {}
    
    for role in role_list:
        role_name_map[role['id']] = role['name']
    
    return role_name_map

def send_role_count():
    users = get_user_info()
    role_list = get_role_names()
    
    for user in users:
        for role in specified_roles.keys():
            if role in user['roles']:
                specified_roles[role] += 1
    
    message = []
    
    for role in specified_roles.keys():
        message.append(f'{role_list[role]}: {specified_roles[role]}')
        
    DEFAULT_GUILD.post_message('\n'.join(message))
    
    
    