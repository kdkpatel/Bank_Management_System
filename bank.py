#import mysql connector
import mysql.connector
from textblob import TextBlob

mydb = mysql.connector.connect(user='root', host='localhost', password='', database='bank_management')


def OpenAcc():
    n = input('Enter your name: ') 
    ac = input("Enter your Account Number: ")
    db = input("Enter DOB: ")
    add = input("Enter Address: ")
    cn = input("Enter Contact Number: ")
    ob = input("Enter the opening balance: ")
    data1 = (n, ac, db, add, cn, ob)
    data2 = (n, ac, ob)
    sql1 = 'insert into account values (%s,%s,%s,%s,%s,%s)'
    sql2 = 'insert into amount values( %s,%s,%s)'
    x = mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    mydb.commit()
    print("Data entered successfully!!!!")
    main()


def DespoAmo():
    amount = input("Enter the amount you wish to deposit: ")
    ac = input("Enter your Account Number: ")
    a = 'SELECT balance FROM amount WHERE AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0]+int(amount)
    sql = 'UPDATE amount SET balance=%s WHERE AccNo=%s'
    d = (t, ac)
    try:
        x.execute(sql, d)
        mydb.commit()
        print("Deposited")
    except Exception as e:
        print("Failed:", e)
    finally:
        x.close()
        main()

def WithdrawAmount():
    amount = input("Enter the amount you wish to withdraw: ")
    ac = input("Enter your Account Number: ")
    a = 'SELECT balance FROM amount WHERE AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0]-int(amount)
    sql = 'UPDATE amount SET balance=%s WHERE AccNo=%s'
    d = (t, ac)
    try:
        x.execute(sql, d)
        mydb.commit()
        print("Withdrawal successful.")
    except Exception as e:
        print("Withdrawal failed:", e)
    finally:
        x.close()
        main()



def BalEnq():
    ac = input("Enter your Account Number: ")
    a = 'select * from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    print("Balance for Account:" ,ac, "is" ,result[-1])
    main()

def DisDetails():
    ac = input("Enter your Account Number: ")
    a = 'select * from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()

def CloseAcc():
    ac = input("Enter your Account Number: ")
    sql1 = 'delete from account where AccNo=%s'
    sql2 = 'delete from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    mydb.commit()
    main()

def main():
    print('''
      1. OPEN ACCOUNT
      2. DEPOSIT AMOUNT
      3. WITHDRAW AMOUNT 
      4. BALANCE ENQUIRY       
      5. DISPLAY CUSTOMER DETAILS
      6. CLOSE AN ACCOUNT''')
    
    choice = input("CHOOSE ANY ONE OF THE OPTIONS MENTIONED BELOW : ")
    if (choice == '1'):
        OpenAcc()
    elif (choice == '2'):
        DespoAmo()
    elif (choice == '3'):
        WithdrawAmount()
    elif (choice == '4'):
        BalEnq()
    elif (choice == '5'):
        DisDetails()
    elif (choice == '6'):
        CloseAcc()
    else:
        print("Opps!!,Invalid Choice")

main()
