hostname = 'localhost'
username = 'Hal5000'
password = '2001'
database = 'halogen'

import MySQLdb
# Simple routine to run a query on a database and print the results:

def createQuery( conn ) :
    cur = conn.cursor()
    
    try:
    	cur.execute( "Create table if not exists user (name varchar(40),nplate varchar(20) primary key,email varchar(40) not null,contact varchar(10) not null,address varchar(500))" )
    except:
    	print("Table exists!")

def insertQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "insert into user values('rakshit gupta','MH42H1434','rakshit@gmail.com','1245875920','Andheri East')" )
    cur.execute( "insert into user values('manas shukla','DL1CJ8153','99manas99@gmail.com','7845214852','Kharghar')" )


def doQuery(nplate) :
    conn = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    cur = conn.cursor()

    cur.execute( "SELECT * FROM user where nplate like '%"+ nplate +"%'" )

    row = cur.fetchall()
    print row
    try:
    	user = row[0]
    	print(user)
    	return user
    except:
    	print('No Records found')
    


#import MySQLdb
#myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
#createQuery( myConnection )

#insertQuery( myConnection )
#doQuery( 'DL1CJ8153')
#myConnection.close()
