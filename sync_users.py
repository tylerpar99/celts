from peewee import Model
from ldap3 import Server, Connection, ALL
from app.models.user import User

# TODO: Create mysql database connection
# Note: we don't need to create model because it's already defined in User model

def connect_to_server(user,password):
    server = Server ('berea.edu', port=389, use_ssl=False, get_info='ALL')
    conn   = Connection (server, user=user, password=password)
    if not conn.bind():
        print(conn.result)
        raise Exception("BindError")
    return conn

def fetch_users(connection):
    # TODO: learn more about .search
    search_base = "dc=berea, dc=edu"
    search_filter = ""
    # TODO: add email and phoneNumber to the attributes
    attributes = ['samaccountname', 'givenname', 'sn', 'employeeid']
    connection.search(search_base, search_filter, attributes=attributes)
    return connection.entries

def grab_key(entry, key):
    if key in entry:
        return entry[key]
    return None

def dump_to_database(entries):
    print("Inserting {0} new records into {1}".format(len(entries), database_path))
    for entry in entries:
        row = User.create(
            username= grab_key(entry,'samaccountname'),
            bnumber=grab_key(entry,'employeeid'),
            email=grab_key(entry, ''),
            phoneNumber=grab_key(entry, '')
            lastname= grab_key(entry,'sn'),
            firstname=grab_key(entry,'givenname'),
            )
        row.save()
