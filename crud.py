import getpass
m=1
print("Welcome to my {CRUD}")
dic={}
while True:
    work = input(">>>")
    if work == "help":
        print("1.Create account\n2.Login\n3.update\n4.delete\n5.EXIT\nDEV option")  
    elif work == "create account" or work=="1":
        while True:
            choo=input("\t\t\t\tSign up(y/n)-:")
            if choo=="y":
                name_info=input("your full name-:")
                ph_number=input("phone number-:")
                E_mail=input("E-mail>>")
                if "@" in E_mail and "." in E_mail:
                    passwd = input("password-:")
                    lic=["name","number","password","email"]
                    data=[name_info,ph_number,passwd,E_mail]
                    c={}
                    for i in range(len(lic)):
                        c.update({lic[i]:data[i]})
                    dic[m]=c
                    m+=1
                else:
                    print("invalid Email entered.")
            else:
                break
    elif work=="login" or work=="2":
        gmail=input("Enter E.mail>>")
        passwd=getpass.getpass(prompt="Password: ", stream=None) 
        c=[]
        for i,j in dic.items():
            for x,y in j.items():
                c.append(y)
        if gmail in c:
            if passwd in c:
                print("corret password...")
                print('''\t\t\tWELCOME dear user:
                    your account has been Hacked.
                    so dont login again.''',chr(128121))
            else:
                print("incorrect password...")
        else:
            print("incorrect password...")
    elif work=="update" or work=="3":
        a = input("E-mail-:")
        b = getpass.getpass(prompt="Password: ", stream=None) 
        c=[]
        for i,j in dic.items():
            for x,y in j.items():
                c.append(y)
        if a in c:
            if b in c:
                print("corret password...")
                while True:
                    mob=input("Wanna update(y/n)-:")
                    print(lic)
                    if mob=="y":
                        change=input("info change-:")
                        for i,j in dic.items():
                            for x,y in j.items():
                                if x==change:
                                    updated=input("new info-:")
                                    j[x]=updated
                                    print("CONGRATULATION:your value is updated.")
                    else:
                        break         
            else:
                print("incorrect password...")
        else:
            print("incorrect password...")
    elif work=="delete" or work=="4":
        a = input("E-mail-:")
        b = getpass.getpass(prompt="Password: ", stream=None) 
        c=[]
        for i,j in dic.items():
            for x,y in j.items():
                c.append(y)
        if a in c:
            if b in c:
                print("corret password...")
                dele=input('''
                           Are you sure you want to delete(y/n)-:''')
                if dele=="y":
                    dic.pop(i)
                    print("\nyour info is deleted\n")
            else:
                print("incorrect password...")
        else:
            print("incorrect password...")
    elif work=="exit" or work=="5":
        confo=input('''you want to exit.
your data will be deleted-:(y/n)''')
        if confo== "y":
            break
    elif work=="dev":
        b = getpass.getpass(prompt="Password: ", stream=None) 
        if b=="0987":
            print("Welcome BOSS",chr(129761))
            print(dic)
        else:
            print("worng passwd")
    else:
        print("command:not found.")
        