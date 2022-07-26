import sqlite3

conn = sqlite3.connect('flaskblog/site.db')
c = conn.cursor()

# tables = ['post', 'user']

# # delete all rows from table
# for table in tables:
#     c.execute(f'DELETE FROM {table};',);
#     print('We have deleted', c.rowcount, 'records from the table.')

c.execute('''create table comment (
id int,
text varchar(200),
date_posted datetime,
post_id int,                                   
author int,
);
''')
#commit the changes to db			
conn.commit()
#close the connection
conn.close()