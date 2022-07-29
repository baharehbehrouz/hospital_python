def main():
    Username=givUserPass()
    # s=creatIllFile()
    # print(readPatientFile())
    # Patient("Reception","add")

def readPatientIndex():
    file = open("ill.txt")
    lines=file.readlines()
    if len(lines)<=9:
        WriteIllFile('0')
        lines=["0"]

    return lines
def WriteIllFile(lines):
        file = open("ill.txt", "w")
        file.writelines(lines)
        file.close()
def ReadPeitent():
    file = open("ill.txt")
    lines = file.readlines()
    return lines
def SearchPaitent(Index,Linecounter,Dep):
    clear = False
    lines = ReadPeitent()
    lnNumber = 0

    for item in lines:
        str1r = item.split()
        if str1r[0] == "Index" and str1r[1] == Index:
            Full_Name = lines[lnNumber -4].split()
            Age = lines[lnNumber -3].split()
            National_code = lines[lnNumber -2].split()
            Status = lines[lnNumber -1].split()
            Financial = lines[lnNumber + 1].split()
            Discharge = lines[lnNumber + 2].split()
            Description = lines[lnNumber +3].split()
            Cost = lines[lnNumber +4].split()
            Paid = lines[lnNumber +5].split()
            if len(Full_Name)==1:
                Full_Name.append(" ")
            if len(Age)==1:
                Age.append(" ")
            if len(National_code) == 1:
                National_code.append(" ")
            if len(Status) == 1:
                Status.append(" ")
            if len(Financial) == 1:
                Financial.append(" ")
            if len(Discharge) == 1:
                Discharge.append(" ")
            if len(Description) == 1:
                Description.append(" ")
            if len(Cost) == 1:
                Cost.append(" ")
            if len(Paid) == 1:
                Paid.append(" ")

            print(Full_Name[0], "                 ", Full_Name[1])
            print(Age[0], "                       ", Age[1])
            print(National_code[0], "             ", National_code[1])
            print(Status[0], "                    ", Status[1])
            print("Index                      ", Index)
            print(Financial[0], "                    ", Financial[1])
            print(Discharge[0], "                    ", Discharge[1])
            print(Description[0], "                    ", Description[1])
            print(Cost[0], "                    ", Cost[1])
            print(Paid[0], "                    ", Paid[1])


            break
        if lnNumber +1 < len(lines):
            lnNumber += 1
    print("Doctor ! please select 1 or 2...you can enter \"back\" to back menue")
    print("1-Add financial row")
    print("2-Discharge the patient")
    userSelected=input(">")
    if userSelected=="1":
        FinancRow=input("PLease Enter patient financial: ")
        line = "Financial            " + FinancRow+"\n"
        ln1=lines[0:lnNumber+1]
        # print(ln1)
        # print(ln1)
        ln2=lines[lnNumber+2:]
        # print(ln2)
        if lnNumber+5>len(lines):
            ln1.append("\n")
        ln1.append(line)
        for i in ln2:
            ln1.append(i)
        # print(ln1)
        # lines=ln1.append(ln2)

        WriteIllFile(ln1)
        print("Finantial added...")
        Doctor_TreatmentPannell(Linecounter,2)
    if userSelected.lower()=="2":
        ClOrno = input("Is this paitent cleared?:y/n ")
        if ClOrno.lower()=="y":
            Discharge = "clearance"
            Status = "cured"
            LnDischarge="Discharge            " + Discharge+"\n"
            LnStatus="Status               " + Status+"\n"
            LnDischarge1 = lines[0:lnNumber + 2]
            LnDischarge2 =lines[lnNumber + 3:]
            if lnNumber + 4 > len(lines):
                # LnStatus1.append("\n")
                LnDischarge1.append("\n")
            LnDischarge1.append(LnDischarge)
            for i in LnDischarge2:
                LnDischarge1.append(i)
            LnStatus1 = LnDischarge1[0:lnNumber - 1]
            LnStatus2 = LnDischarge1[lnNumber:]
            if lnNumber + 6 > len(lines):
                # LnStatus1.append("\n")
                LnStatus1.append("\n")
            LnStatus1.append(LnStatus)
            for j in LnStatus2:
                LnStatus1.append(j)
            WriteIllFile(LnStatus1)
            clear=True

            # WriteIllFile(LnDischarge1)
            print("patient cleared....")
            Doctor_TreatmentPannell(Linecounter,2)
        if ClOrno.lower()=="n":
            pass
    if userSelected=="back":
        Acceptance_and_clearance(Linecounter,Dep)
    if clear==True:
        return True
def Patient(user,operation,Linecounter,Dep):
    l= readPatientIndex()
    lines=ReadPeitent()
    l=str(int(l[0])+1)+"\n"
    lines[0]=l
    WriteIllFile(lines)
    if user=="Reception" and operation=="add":
        file = open("ill.txt", "+a")
        FName=input("enter patinent Full Name You can enter space betwen characters... ")
        S=FName.split()
        if len(S)>1:
            while True:
                FName = input("enter patinent Full Name You can enter space betwen characters... ")
                S = FName.split()
                if len(S)==1:
                    # file.writelines(FName)
                    break
        Age = input("enter patinent Age if patient age is under 1 year you can enter a float betwen 0-1 and your limit is 0-200... ")
        if float(Age)<0 or float(Age)>200:
            while True:
                Age = input("enter patinent Age if patient age is under 1 year you can enter a float betwen 0-1 and your limit is 0-200... ")
                if float(Age)>0 or float(Age)<200:
                    # file.writelines(Age)
                    break
        NCode = input("enter patinent National Code... You should enter a number with 15 len ...")
        if len(NCode)<15 or not NCode.isdigit():
            while True:
                NCode = input("enter patinent National Code... You should enter a number with 15 len ...")
                if len(NCode) > 15 or NCode.isdigit():
                    break
        FName="Full-Name            "+FName+"\n"
        Age=  "Age                  "+str(Age)+"\n"
        NCode="National_code        "+NCode+"\n"
        status="Status               "+"sick"+"\n"
        Index1 = "Index                " + str((int(lines[0])+1)-1)+"\n"
        Financial="Financial\n"
        Discharge = "Discharge\n"
        Description="Description\n"
        Cost="Cost\n"
        Paid="Paid\n"

        lines.append(FName)
        lines.append(Age)
        lines.append(NCode)
        lines.append(status)
        lines.append(Index1)
        lines.append(Financial)
        lines.append(Discharge)
        lines.append(Description)
        lines.append(Cost)
        lines.append(Paid)

        WriteIllFile(lines)
        print("New patinet added...")
    file.close()
    Acceptance_and_clearance(Linecounter,Dep)

    if user=="Clearance":
        pass
def Recruitment(LineCounter,str1):
    d=""
    lines=readFile()
    name=input("Enter new Employee Full Name...")
    if name=="" or name==" ":
        while True:
            name = input("Enter new Employee Full Name...")
            if name != "" or name != " ":
                break
    uname=input("Enter new Employee User Name...")
    s=uname.split()
    if len(s)>1 or uname=="" or uname==" ":
        while True:
            uname = input("Enter new Employee User Name...")
            sp=uname.split()
            if len(sp)==1 and uname != "" and uname != " ":
               break

    pasw=input("Enter new Employee Password...")
    s = pasw.split()
    if len(s) > 1 or pasw=="" or pasw==" ":
        while True:
            pasw = input("Enter new Employee Password...")
            sp = pasw.split()
            if len(sp) == 1 and  pasw != "" and pasw != " ":
                break

    age=input("Enter new Employee Age...")
    s = age.split()
    if int(age)<=0 or int(age)>200 or age=="" or age==" " or not age.isdigit() or len(s)>1:
        while True:
            age = input("Enter new Employee Age...")
            s = age.split()
            if age != "" and age != " " and int(age)>0 and int(age)<200 and age.isdigit() and len(s)==1:
                break
    ncode=input("Enter new Employee National_code...")
    s = ncode.split()
    if ncode=="" or ncode==" " or not len(ncode)>=15 or not ncode.isdigit() or len(s)>1:
        while True:
            ncode = input("Enter new Employee National_code...")
            s = ncode.split()
            if ncode != "" and ncode != " " and len(ncode)==15  and ncode.isdigit() and len(s)>1:
                break
    dep=input(f"{name} is in witch part?You can select 1 for Acceptance and clearance 2 for Treatmen 3 for Accounting ")
    if dep=="" or dep==" " or not dep.isdigit():
        while True:
            dep = input(">>")
            if dep != "" and  dep != " " and dep.isdigit():
                    break
    if dep=="1":
         d="Acceptanceandclearance"
    elif dep=="2":
         d="Treatment"
    elif dep=="3":
         d="Accounting"

    EmpName="Full_Name           " +name + "\n"
    EmpUserName = "Username            " + uname + "\n"
    EmpPassword="Password            " +  pasw+ "\n"
    EmpAge ="Age                 " + age + "\n"
    EmpNcode = "National_code       "  + ncode + "\n"
    EmpDep = "department          " +d + "\n"
    newEmp=[EmpUserName,EmpPassword,EmpName,EmpAge,EmpNcode,EmpDep]

    file = open("file.txt", "a")
    file.writelines(newEmp )
    print("New Emploee Added!!!")
    file.close()
    ManagersubPanel("admin",str1)
def write_file(lines):
    file = open("file.txt", "w")
    file.writelines(lines)
    file.close()
def Show_employees(LineCounter, str1):
    st1=[]
    lines=readFile()
    for item in lines:
        st = ""
        str1r=item.split()
        # print(str1r)
        ln=len(str1r)
        if ln>2:
            # st1=str1r[0:2]
            st1=str1r[1:]
            # print(st1)
            for it in st1:
                st+=" "+it
            print(str1r[0],(20-len(str1r[0]))*" ",st)
        elif ln<=2:
            st=str1r[1]
            print(str1r[0],(21-len(str1r[0]))*" ",st)
        if str1r[0]=="department":
            print()
    ManagersubPanel(LineCounter, str1)
def Employee_search(LineCounter, str1):
    IsNC=False
    lines=readFile()
    SearchFname=input("Name and Family(Full Name): ").lower()
    SearchNcode=input("National Code: ").lower()
    lnNumber=0
    for item in lines:
        st=""
        s = ""
        s1=""
        s2=""
        s3=""
        s4=""
        s5=0
        str1r = item.split()
        # amirpedram
        # 7890653891
        # print(userName)
        # print(password)
        #
        n = lines[lnNumber + 2].split()
        ln = len(n)
        if ln > 2:
            st1 = str1r[1:]
            # print(st1)
            for it in st1:
                st += " " + it
        if ln<=2:
            st=n[1]

        if n[0]=="National_code" and st==SearchNcode:
            IsNC=True
        #     print("yess")
        if str1r[0]=="Full_Name" and str1r[1]==SearchFname and IsNC :
            userName = lines[lnNumber-2].split()
            l = len(userName)
            if l > 2:
                u1 = userName[1:]
                for iu in u1:
                    s += " " + iu
            elif ln <= 2:
                s = userName[1]

            password = lines[lnNumber - 1].split()
            l = len(password)
            if l > 2:
                u1 = password[1:]
                for iu in u1:
                    s1 += " " + iu
            elif ln <= 2:
                s1 = password[1]
            Fname = lines[lnNumber ].split()
            l = len(Fname)
            if l > 2:
                u1 = Fname[1:]
                for iu in u1:
                    s2 += " " + iu
            elif ln <= 2:
                s2 = Fname[1]
            age = lines[lnNumber + 1].split()
            l = len(age)
            if l > 2:
                u1 = age[1:]
                for iu in u1:
                    s3 += " " + iu
            elif ln <= 2:
                s3 = age[1]
            nCode = lines[lnNumber + 2].split()
            l = len(nCode)
            if l > 2:
                u1 = nCode[1:]
                for iu in u1:
                    s4 += " " + iu
            elif ln <= 2:
                s4 = nCode[1]
            Dep=lines[lnNumber + 3].split()
            l = len(Dep)
            if l > 2:
                u1 = Dep[1:]
                for iu in u1:
                    s5 += " " + iu
            elif ln <= 2:
                s5 = Dep[1]
            print(userName[0],"                ",s)
            print(password[0],"                 ", s1)
            print(Fname[0],"                " , s2)
            print(age[0], "                     ", s3)
            print(nCode[0],"            ", s4)
            print(Dep[0], "               ", s5)

        if lnNumber+7<len(lines):
            lnNumber += 1

    ManagersubPanel(LineCounter, str1)
def SubTretment_pannel(linecounter,Dep):
    Index=input("Please Enter paitent Index Number To Search: ")
    SearchPaitent(Index,linecounter,Dep)
def TretmentRequest(LineCounter,Dep):
    lines = ReadPeitent()
    print("1-Find paitent")
    userInput = input(">").lower()
    if userInput == "change password":
        pass
    elif userInput=="sign out":
        main()
    elif userInput == "1" and Dep == 2:
        SubTretment_pannel(LineCounter,Dep)
def Doctor_TreatmentPannell(LineCounter,Dep):
    Items = ["Find patien"]
    print("-------[Treatment panel-------")
    print(f"You can enter\"change password\", \"sign out\" 1 ")
    TretmentRequest(LineCounter,Dep)
def changePass(LineCounter,Username,str1=""):
    lines=readFile()
    oldpass = input("Enter old password: ")
    if oldpass == str1[1]:
        newPass = input("Enter new password: ")
        confNewPass = input("Confirm new password: ")
        if newPass == confNewPass:
            str1 = "Password            " + newPass + "\n"
            # if Username=="admin":
            #     LineCounter+=1
            lines[LineCounter] = str1
            # Recruitment()
            write_file(lines)
            ManagersubPanel(LineCounter,str1)
            # ManagerRequest( LineCounter, str1)
def Acceptance_and_clearance(Linecounter,Dep):
    print("------------Acceptance and clearance--------------")
    parts = ["Reception", "Clearance", "Show patients", "Find patient"]
    print(f"You can enter \"back\" or chooce from 1 to {len(parts)}")
    i = 1
    for item in parts:
        print(f"{i}-{item}")
        i += 1
    AcceptanceRequest(Linecounter, Dep)
    # adminRequest(str1)
def AccountingPannel(Linecounter, Dep):
    print("------------Accounting Pannel--------------")
    parts = ["Reception", "Clearance", "Show patients", "Find patient"]
    print("you can enter 1.")
    print("1-Checkout")
    userRequest=input(">")
    if userRequest=="1":
        checkout(Linecounter, Dep)
def clearance(Linecounter,Dep):
    Index = input("Enter a paitent Index to search and clearance...")
    lines = ReadPeitent()
    lnNumber = 0
    for item in lines:
        str1r = item.split()
        # amirpedram
        # 7890653891
        # print(userName)
        # print(password)
        # isIndecinlines=F
        if str1r[0] == "Index" and str1r[1] == Index:
            Full_Name = lines[lnNumber + 1].split()
            Age = lines[lnNumber + 2].split()
            National_code = lines[lnNumber + 3].split()
            Status = lines[lnNumber + 4].split()
            Index = lines[lnNumber + 5].split()
            Financial = lines[lnNumber + 6].split()
            Discharge = lines[lnNumber + 7].split()
            Description = lines[lnNumber + 8].split()
            Cost = lines[lnNumber + 9].split()
            Paid = lines[lnNumber + 10].split()
            if len(Full_Name) == 1:
                Full_Name.append(" ")
            if len(Age) == 1:
                Age.append(" ")
            if len(National_code) == 1:
                National_code.append(" ")
            if len(Status) == 1:
                Status.append(" ")
            if len(Financial) == 1:
                Financial.append(" ")
            if len(Discharge) == 1:
                Discharge.append(" ")
            if len(Description) == 1:
                Description.append(" ")
            if len(Cost) == 1:
                Cost.append(" ")
            if len(Paid) == 1:
                Paid.append(" ")

            print(Full_Name[0], "                 ", Full_Name[1])
            print(Age[0], "                       ", Age[1])
            print(National_code[0], "             ", National_code[1])
            print(Status[0], "                    ", Status[1])
            print(Index[0], "                     ", Index[1])
            print(Financial[0], "                 ", Financial[1])
            print(Discharge[0], "                 ", Discharge[1])
            print(Description[0], "                    ", Description[1])
            print(Cost[0], "                    ", Cost[1])
            print(Paid[0], "                    ", Paid[1])

            break
    if lnNumber + 1 < len(lines):
        lnNumber += 1
    whantCheckout = input(f"Do you what clearance {Full_Name[1]} account ? y/n")
    if whantCheckout.lower()=="y" :
        line1 = lines[0:lnNumber]
        line2 = lines[lnNumber + 10:]
        for i in line2:
            line1.append(i)
        print(len(line1))
        if len(line1)==1:
            line1[0]=" "
    WriteIllFile(line1)
    print("paitent cleared..")
    Acceptance_and_clearance(Linecounter,Dep)
def checkout(Linecounter,Dep):
    Index=input("Enter a paitent Index to search and clearance...")
    # if SearchPaitent(Index,Linecounter,Dep):
    lines = ReadPeitent()
    lnNumber = 0
    for item in lines:
       str1r = item.split()
    # amirpedram
    # 7890653891
    # print(userName)
    # print(password)
    # isIndecinlines=F
       if str1r[0] == "Index" and str1r[1] == Index and Dep==3:
          Full_Name = lines[lnNumber -4].split()
          Age = lines[lnNumber -3].split()
          National_code = lines[lnNumber -2].split()
          Status = lines[lnNumber -1].split()
          Index = lines[lnNumber ].split()
          Financial = lines[lnNumber+1 ].split()
          Discharge = lines[lnNumber + 2].split()
          Description = lines[lnNumber + 3].split()
          Cost = lines[lnNumber + 4].split()
          Paid = lines[lnNumber + 5].split()
          if len(Full_Name) == 1:
              Full_Name.append(" ")
          if len(Age) == 1:
              Age.append(" ")
          if len(National_code) == 1:
              National_code.append(" ")
          if len(Status) == 1:
              Status.append(" ")
          if len(Financial) == 1:
              Financial.append(" ")
          if len(Discharge) == 1:
              Discharge.append(" ")
          if len(Description) == 1:
              Description.append(" ")
          if len(Cost) == 1:
              Cost.append(" ")
          if len(Paid) == 1:
              Paid.append(" ")

          print(Full_Name[0], "                 ", Full_Name[1])
          print(Age[0], "                       ", Age[1])
          print(National_code[0], "             ", National_code[1])
          print(Status[0], "                    ", Status[1])
          print(Index[0], "                     ", Index[1])
          print(Financial[0], "                 ", Financial[1])
          print(Discharge[0], "                 ", Discharge[1])
          print(Description[0], "                    ", Description[1])
          print(Cost[0], "                    ", Cost[1])
          print(Paid[0], "                    ", Paid[1])

       if lnNumber + 1 < len(lines):
           lnNumber += 1
       # break


    # break
    # whantCheckout = input(f"Do you what check out {Full_Name[1]} account ? y/n")
    cost1 = input("Input Cost...")
    paid1 = input("Did paied cost?y/n")
    if paid1=="y":
        paid1="paid"
    if paid1=="n":
        paid1="not paid"
    description1 = input("enter a description ...")
    Description = "Description          " + description1 + "\n"
    Description1= lines[0:lnNumber-2 ]
    Description2 = lines[lnNumber -1:]
    Description1.append(Description)
    for i in Description2:
            Description1.append(i)
    Cost = "Cost                 " + cost1 + "\n"
    Cost1 = Description1[0:lnNumber -1]
    Cost2 = Description1[lnNumber :]
    Cost1.append(Cost)
    for j in Cost2:
        Cost1.append(j)
    Paid = "Paid                 " + paid1 + "\n"
    Paid1 = Cost1[0:lnNumber ]
    Paid2 = Description1[lnNumber +1:]
    Paid1.append(Paid)
    for z in Paid2:
        Paid1.append(z)
    WriteIllFile(Paid1)
    print("Accounting added...")
    AccountingPannel(Linecounter, Dep)
def showPaitent(Linecounter,Dep):
    lines = ReadPeitent()
    for item in lines:
        st = ""
        str1r = item.split()
        # print(str1r)
        ln = len(str1r)
        if ln > 2:
            # st1=str1r[0:2]
            st1 = str1r[1:]
            # print(st1)
            for it in st1:
                st += " " + it
            print(str1r[0], (19 - len(str1r[0])) * " ", st)
        # elif ln <= 2:
        #     st = str1r[1]
        #     print(str1r[0], (21 - len(str1r[0])) * " ", st)

        # str1r = item.split()
        if len(str1r)==2:
            print(str1r[0], (20 - len(str1r[0])) * " ", str1r[1])
        if len(str1r)==1:
            print(str1r[0])

        if str1r[0] == "Paid":
            print()
    Acceptance_and_clearance(Linecounter,Dep)
def AcceptanceRequest(Linecounter,Dep):
    lines = readFile()
    userInput = input(">").lower()
    if userInput == "back":
       main()
       # changePass(str1,LineCounter,Username)
    elif userInput == "1" and Dep==1:
        Patient("Reception","add",Linecounter,Dep)
    elif userInput == "2":
        clearance(Linecounter,Dep)
    elif userInput == "3":
        showPaitent(Linecounter,Dep)
    elif userInput == "4":
        inp=input("please enter paitent index...")
        y=SearchPaitent(inp,Linecounter,Dep)
def Laying_off(LineCounter,str1):
    isNC=False
    lines=readFile()
    SearchFname=input("Name and Family(Full Name): ")
    SearchNcode=input("National Code: ")
    lnNumber=0
    for item in lines:
        str1r = item.split()
        s=lines[LineCounter].split()
        # if s[0]=="National_code" and s[1]==SearchNcode:
        #     isNC=True
        if str1r[0]=="Full_Name" and str1r[1]==SearchFname  :
            s1=lines[:lnNumber-2]
            s2=lines[lnNumber+4:]
            for i in s2:
                s1.append(i)
            break
        if lnNumber+2<len(lines):
            lnNumber += 1

    write_file(s1)
    print("Emploee Removed!!!")
    ManagersubPanel(LineCounter, str1)
def adminRequest(str1):
    # import os
    lines=readFile()
    # os.system('cls' or 'clear')
    #
    # class color:
    #     GREEN = '\033[92m'
    #     RED = '\033[91m'
    #     WHITE = '\033[0m'
    userInput = input(">").lower()
    if userInput == "1":
       Recruitment()
    if userInput == "3":
        Show_employees()
    if userInput == "2":
        Laying_off()
    if userInput == "4":
        Employee_search()
    if userInput == "sign out":
        MainPannel("admin")
        MainRequest(1, "admin")
    if userInput=="back":
        MainPannel("admin")
        MainRequest(1,"admin","Administration")
        # userRequest(str1, LineCounter, Username)
    if userInput=="change password":
        changePass(1,"admin",str1)
def readFile():
    with open("file.txt", "r") as f:
        lines = f.readlines()
        return lines
def ManagersubPanel(Linecounter,str1):
    # while True:
    #     try:
            Users = ["Recruitment", "Laying off", "Show employees", "Employee search"]
            print("-------[Administration panel-------")
            print(f"You can enter\"change password\", \"sign out\" , \"back\" or chooce from 1 to {len(Users)}")
            i=1
            for item in Users:
                print(f"{i}-{item}")
                i += 1
            ManagerRequest(Linecounter,str1)
        # except:
        #     ManagersubPanel(Linecounter,str1)
def ManagerPannel(LineCounter, str1):
    print("-------[Main panel]-------")
    adminPanell = ["Acceptance and clearance", "Treatment", "Accounting"]
    print(f"You can enter\"change password\", \"sign out\"  or chooce from 1 to {len(adminPanell)}")
    i = 1
    for item in adminPanell:
        print(f"{i}-{item}")
        i += 1
    ManagerRequest(LineCounter, str1)
def ManagerRequest(LineCounter, str1):
    lines = readFile()
    userInput = input(">").lower()
    if userInput == "change password":
        changePass(LineCounter,"admin",str1 )
    elif userInput == "sign out":
        main()
    elif userInput == "back":
        ManagersubPanel(LineCounter, str1)
    elif  userInput == "1":
        Recruitment(LineCounter,str1)
    elif userInput == "2" :
        Laying_off(LineCounter, str1)
    elif userInput == "3" :
        Show_employees(LineCounter,str1)
    elif userInput == "4" :
        Employee_search(LineCounter,str1)
def givUserPass():
     while True:

            IsPassword = False
            IsUserName = False
            Username = input("Username: ")
            Password = input("Password: ")
            lines=readFile()
            LineCounter = 0
            for line in lines:
                if line != "\n":
                        str1 = line.split()
                        if str1[0] == "Username" and str1[1] == Username:
                            IsUserName = True
                        Dep=0
                        if str1[0] == "Password" and str1[1] == Password and IsUserName:
                                IsPassword=True
                                D=lines[LineCounter+4].split()
                                if D[1]=="Acceptanceandclearance":
                                    Dep=1
                                if D[1] == "Treatment":
                                    Dep = 2
                                if D[1] == "Accounting":
                                    Dep = 3
                                break
                LineCounter+=1
            if Username=="admin" and IsPassword==True:
                ManagersubPanel(LineCounter,str1)
            if Username!="admin" and Dep==1 :
                Acceptance_and_clearance(LineCounter,Dep)
            if Username != "admin" and Dep == 2:
                Doctor_TreatmentPannell(LineCounter,Dep)
            if Username != "admin" and Dep == 3:
                AccountingPannel(LineCounter, Dep)

main()
