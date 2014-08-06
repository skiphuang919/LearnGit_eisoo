#!/usr/bin/env python
#encoding=utf-8
"""
this is a py which do sth on DB
"""

import os
from random import randrange as rrange
import MySQLdb


def connect(user_name,db_name,password):
    cxn=MySQLdb.connect(user=user_name,db=db_name,passwd=password)
    return cxn

def create(cur):
    cur.execute("CREATE TABLE mates(name VARCHAR(8),uid INTEGER)")
NAMES=(('a',21),('b',1),('c',22),('d',99))

def randname():
    pick=list(NAMES)
    while len(pick)>1:
        yield pick.pop(rrange(len(pick)))

def insert(cur):
    cur.executemany("INSERT INTO mates VALUES(%s,%s)",[(who,uid) for who,uid in randname()])

def dbdump(cur):
    cur.execute("SELECT * FROM mates")
    for info in cur.fetchall():
        print info

def drop_tables(cur):
    cur.execute("DROP TABLE mates")

def main():
    print '****connect to database***'
    cxn=connect('root','test','123456')
    if not cxn:
        print 'ERROR:connect failed'
        return
    cur=cxn.cursor()
 
    #print '***create mates table'
    #create(cur)

    print '***insert date****'
    insert(cur)

    print '***show tables****'
    dbdump(cur)


if __name__=='__main__':
    main() 
        
    
