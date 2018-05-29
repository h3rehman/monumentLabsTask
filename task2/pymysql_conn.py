import pymysql
from intercom.client import Client

'''
Grab the data from the user_data table from monlab_db Database.
Insert each record as new users in Intercom using Intercom's API
'''

intercom = Client(personal_access_token='your_access_token')

try:
    
    conn = pymysql.connect(user="root", password="whateveritis", host="localhost", database="monlab_db")
    curs = conn.cursor()
    sql = 'select * from user_data;'
    rowCount= curs.execute(sql)
    data = curs.fetchall()

    credentials = {}
    bulk_User = []
    
    #getting each user data into a directory and appending that into the bulk_User list
    for row in data:
        credentials['user_id']= row[0]
        credentials['name']= str(row[1])
        credentials['email']= str(row[2])
        bulk_User.append(credentials)
        credentials = {}
    
    #doing a bulk insert/creation job
    intercom.users.submit_bulk_job(create_items=bulk_User)    
    #print (bulk_User)
    print('Data transmitted')

except:
    print('Something went wrong somewhere')
        

