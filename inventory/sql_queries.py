from django.db import connection, transaction

'''
    Because Django does not support prepared statements, it does so in another form to protect against
    SQL Injection in the form of 
'''