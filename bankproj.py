import json
from pathlib import Path
import random
import string

class Bank:

    data = []

    __database = "data.json"
     
    try:
        if Path(__database).exists():
            with open(__database) as fs:
                data = json.loads(fs.read())
    except Exception as err:
        print(f"An error occured as {err}")
    

    @classmethod
    def __updatedata(cls):
        with open(cls.__database, "w") as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def __Generate_account_number(cls):
        alpha = random.choices(string.ascii_letters,k=5) 
        numbers = random.choices(string.digits,k=5)
        id = alpha + numbers
        random.shuffle(id)
        return "".join(id)       

    def createaccount(self):
        info = {
            "name":input("Tell your name :- "),
            "age":int(input("Tell your age :- ")),
            "gender":input("Tell your gender :- "),
            "email":input("Tell your email :- "),
            "phone":int(input("Tell your phone number :- ")),
            "AccountNo.":Bank.__Generate_account_number(),
            "pin":int(input("Tell your pin :- ")),
            "balance":0
        }
        if info['age'] < 18:
            print("sorry you cannot create the account")
        
        elif not len(str(info["phone"])) == 10:
            print("Invalid phone number")
        
        elif not len(str(info["pin"])) == 4:
            print("Invalid pin")
        
        else:
            Bank.data.append(info)
            Bank.__updatedata()
            

    def depositeMoney(self):
        account_no = input("tell your account")
        pin = int(input("tell you pin:- "))
        # for i in Bank.data:
        #     if i["AccountNo."] == account_no and i['pin'] == pin:
        #         userdata = i
        #         break
        #     else:
        #         print("no such user found.")
        #     print(user.data)
        user_data = [i for i in Bank.data if i["AccountNo."] == account_no and i['pin'] == pin]
        
        if user_data == False:
            print("no such user found")
        else:
            amount = int(input("how much you want to deposit"))
            if amount < 0:
                print("Invalid deposit amount")
            elif amount > 20000:
                print("sorry you cannot deposit more than 20,000rs")
            else:
                user_data[0]['balance'] += amount
                Bank.__updatedata()
                print("amount deposited successfully")

    def withdrawMoney(self):
        account_no = input("tell your account")
        pin = int(input("tell you pin:- "))

        user_data = [i for i in Bank.data if i["AccountNo."] == account_no and i['pin'] == pin]

        if user_data == False:
            print("no such user found")
        else:
            amount = int(input("how much you want to withdraw"))
            if amount > 20000:
                print("sorry you cannot withdraw more than 20000rs")
            elif amount > user_data[0]["balance"]:
                print("insufficient balance")
            else:
                user_data[0]["balance"] -= amount
                Bank.__updatedata()
                print("amount withdrawn successfully")

    def accountDetails(self):
        account_no = input("tell your account")
        pin = int(input("tell you pin:- "))

        user_data = [i for i in Bank.data if i["AccountNo."] == account_no and i['pin'] == pin]

        if user_data == False:
            print("no such user found")
        else:
            for i in user_data[0]:
                print(f"{i} : {user_data[0][i]}")

    def updateAccount(self):
        account_no = input("tell your account")
        pin = int(input("tell you pin:- "))

        user_data = [i for i in Bank.data if i["AccountNo."] == account_no and i['pin'] == pin]

        if user_data == False:
            print("no such user found")
        else:
            print("you cannot change your account number")
            print("now update your details enter to skip")
            newdata = {
                "name":input("tell your name:- "),
                "age":input("tell your age "),
                "email":input("tell your email"),
                "phone":input("tell your phone number"),
                "pin": input("tell your pin "),
            }
            if newdata['age'] == "":
                newdata['age'] = user_data[0]['age']
            if newdata['name'] == "":
                newdata['name'] = user_data[0]['name']
            if newdata['email'] == "":
                newdata['email'] = user_data[0]['email']
            if newdata['phone'] == "":
                newdata['phone'] = user_data[0]['phone']
            if newdata['pin'] == "":
                newdata['pin'] = user_data[0]['pin']

            newdata["AccountNo."] = user_data[0]["AccoutnNo."]
            newdata["balance"] = user_data[0]["balance"]

            for i in user_data[0]:
                if user_data[0][i] == newdata[i]:
                    continue
                else:
                    if newdata[i].isnumeric():
                        user_data[0][i] = int(newdata[i])
                    else:
                        user_data[0][i] = newdata[i]

            Bank.__updatedata()
            print("updated successfully")
            
    def deleteAccount(self):
        account_no = input("tell your account")
        pin = int(input("tell you pin:- "))

        user_data = [i for i in Bank.data if i["AccountNo."] == account_no and i['pin'] == pin]

        Bank.data.remove(user_data[0])
        Bank.__updatedata()
        print("deleted successfully.")


print("""Press the following for your task:- 
         Press 1 for creating the bank account. 
         Press 2 for depositing money in your bank account. 
         Press 3 for withdrawing the money from your account.
         press 4 for account details. 
         press 5 for updating your details. 
         press 6 for deleting the account. 
         press 0 to exit.""")


user = Bank()
check = input("Tell your response :- ")

if check == "1":
    user.createaccount()
elif check =="2":
    user.depositeMoney()
elif check == "3":
    user.withdrawMoney()
elif check == "4":
    user.accountDetails()
elif check == "5":
    user.updateAccount()
elif check == "6":
    user.deleteAccount()