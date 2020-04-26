#coding:utf-8
import base64

while(1):
    database_password = raw_input("Password= ")
    if database_password == "quit":
        exit()
    else:
        a = base64.b64decode(database_password)
        s=""
        for i in a:
                s+= chr(ord(i) -1 )
        print "明文密码= " + s + "\n"
