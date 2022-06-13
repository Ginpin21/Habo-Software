import pandas as pd
import matplotlib.pyplot as pl
import sys
import random
#In total 2 CSV files will be made automatically when the add_data() and user() functions are called.
#Softstocks.csv holds the software info like price , quantity,etc.
#Softsales.csv holds the sales info like the software bought, customer who bought it,etc.
#----------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------    
def key_gen():#generates the product activation key
    key=''
    try:
        data=pd.read_csv("Softsales.csv",header=None,index_col=0)
        dup=True
        while dup==True:
            for i in range(11):
                if i not in [3,7]:
                    r=random.randrange(9)
                    key+=str(r)   
                else:
                    key+="-"
            for row in data.itertuples():
                if row[2]==key:
                    dup=True
                    break
                else:
                    dup=False              
    except FileNotFoundError:
        for i in range(11):
            if i not in [3,7]:
                r=random.randrange(9)
                key+=str(r)
            else:
                key+="-"           
    return key
#----------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------    
def add_data():#adding data
    print("Adding data........")
    data_added=True
    try:
        while data_added==True:
            SId=int(input("Enter the SId of the software: "))
            a=search_data(SId)
            if a in [-1,0]:
                SName=input("Enter the name of the software: ")
                SPrice=int(input("Enter the price of the software: "))
                SQuantity=int(input("Enter the quantity of the software: "))
                Sold=0
                l1=[SId,SName,SPrice,SQuantity,Sold]
                df1=pd.DataFrame([l1])
                df1.to_csv("Softstocks.csv",mode="a",header=0,index=0)
                data_added=False
            else:
                print("SId already in use please use a different SId.")
                input("\n Press any key to go back to data addition menu.")
    except FileNotFoundError:
        print("File does not exist")
    input("\n Press any key to continue.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------  
def remove_data(Sremove):#removing specific data
    try:
        a=search_data(Sremove)
        if a==1:
            confirm= input("\n Are you sure you want to remove SId "+str(Sremove)+" from the database? \n").lower()
            if confirm in ["yes","y"]:
                df=pd.read_csv("Softstocks.csv",header=None)
                for row in df.itertuples():
                    if row[1] == Sremove:
                        df.drop(row[0],axis=0,inplace=True)
                        df.to_csv("Softstocks.csv",columns=None,index=False,header=False)
                        break
            else:
                print("SId",Sremove,"will not be removed.")
        else:
            print("The SId",Sremove,"does not exist in the database.")
    except FileNotFoundError:
        print("The file does not exist.")     
    input("\n Press any key to continue.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------    
def modify_data():#modifying specific data
    try:
        columns1=['SId','SName','SPrice','SQuantity','Sold']
        df=pd.read_csv("Softstocks.csv",header=None,index_col=0)
        print("MODIFICATION MENU")
        print("1. Change name")
        print("2. Add stocks")
        print("3. Change price")
        ch=int(input("Enter your choice: "))
        loop=True
        while loop == True:
            if ch == 1:
                change_id=int(input("Enter the SId of the software whose name should be changed: "))
                a=search_data(change_id)
                name=input("Enter the new name: ")
                df.at[change_id,1]=name
                df.to_csv("Softstocks.csv",header=False,columns=None)
                loop=False
                break
            elif ch==2:
                stock_id=int(input("Enter the SId of the software whose quantity should be increased: "))
                b=search_data(stock_id)
                new_stocks=int(input("Enter the amount of stocks to be added: "))
                df.at[stock_id,3]+=new_stocks
                df.to_csv("Softstocks.csv",header=False,columns=None)
                loop=False
                break
            elif ch==3:
               price_id=int(input("Enter the SId of the software whose price should be changed: "))
               c=search_data(price_id)
               new_price=int(input("Enter the new price: "))
               df.at[price_id,2]=new_price
               df.to_csv("Softstocks.csv",header=False,columns=None)
               loop=False
               break
            else:
                break
    except FileNotFoundError:
        print("The file doesnt exist.")
    input("\n Press any key to continue.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------- 
def search_data(Ssearch):#finds a specific data and displays it
    val=0
    try:
        columns1=['SId','SName','SPrice','SQuantity','Sold']
        data=pd.read_csv("Softstocks.csv",index_col="SId",names=columns1)
        for row in data.itertuples():
            if row[0]==Ssearch:
                print("SID \t\t SName \t\t  SPrice \t\t  SQuantity \t\t    Sold")
                print("____________________________________________________________________________________________")
                print(row[0],row[1],row[2],"  ",row[3],row[4],sep="\t\t")
                val=1
                break
        else:
            val=-1                  
    except FileNotFoundError:
        print("File does not exist.....")
    return val
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def search_prod(SKey):#Find the customer and software name by product key
    try:
        col_names=["Customer Name","SName","SKey"]
        data=pd.read_csv("Softsales.csv",index_col=0,names=col_names)
        for row in data.itertuples():
            if row[2]==SKey:
                print("\n Matching key found")
                print("Customer Name \t\t SName \t\t\t SKey")
                print("__________________________________________________________________")
                print(row[0],row[1],row[2],sep="\t\t")
                break
        else:
            print("Such a key does not exist or has not been generated yet.")      
    except FileNotFoundError:
        print("The file does not exist.")
    input("\n Press any key to continue.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------- -----------------------------------------------------------------------------   
def search_cus(cusname):#Find the purchases made by a customer
    try:
        col_names=["Customer Name","SName","SKey"]
        data=pd.read_csv("Softsales.csv",index_col=0,names=col_names)
        print("Customer Name \t\t SName \t\t\t SKey")
        print("__________________________________________________________________")
        for row in data.itertuples():
            if row[0]==cusname:
                print(row[0],row[1],row[2],sep="\t\t")
     
    except FileNotFoundError:
        print("The file does not exist.")
    input("\n Press any key to continue.")  
#----------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------- -----------------------------------------------------------------------------   
def traverse_data():#displays all the data
    print("Reading all records.........")
    try:
        columns1=['SId','SName','SPrice','SQuantity','Sold']
        data=pd.read_csv("Softstocks.csv",index_col="SId",names=columns1)
        data.sort_values("SId",inplace=True)
        print(data)
    except FileNotFoundError:
        print("The file does not exist.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------- 
def traverse_sales():#displays all the sales made
    try:
        col_names=["Customer Name","SName","SKey"]
        data=pd.read_csv("Softsales.csv",index_col=0,names=col_names)
        print(data)
    except FileNotFoundError:
        print("The file does not exist.")
    input("\n Press any key to continue.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------       
def visualize_data(graphby):#graph data based on SPrice,SQuantity or Sold
    try:
        columns1=['SId','SName','SPrice','SQuantity','Sold']
        data_stocks=pd.read_csv("Softstocks.csv",index_col="SId",names=columns1)           
        i=columns1.index(graphby)
        if graphby not in ["SId","SName"]:
            data_stocks.sort_values(graphby,inplace=True)
            x_axis=data_stocks["SName"]
            y_axis=data_stocks[graphby]
            pl.bar(x_axis,y_axis,color="g",width=0.3)
            pl.xlabel("Software Name")
            if graphby == "SPrice":
                pl.ylabel(graphby+" in AED")
            else:
                pl.ylabel(graphby)
            pl.title("HABO SOFTWARES")
            pl.show()   
        else:
            print("The given data cannot be graphed.")
    except FileNotFoundError:
        print("The file does not exist.")
    input("\n Press any key to continue.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------     
def user():#user menu to buy software
    try:
      while True:
        print("_______________________________________________________________________________________")
        print("WELCOME USER")
        print("1. Buy software")
        print("2. View all available softwares")
        print("3. View price chart")
        print("4. Back to main menu")
        choice=int(input("Press the number corresponding to your choice: "))
        if choice==1:
            traverse_data()
            df_stocks=pd.read_csv("Softstocks.csv",header=None,index_col=0)
            buy_id=int(input("Enter the SId of the software you want to buy: "))
            search=search_data(buy_id)
            if search==1:
                if df_stocks.at[buy_id,3] > 0:
                    cus_name=input("Enter your name: ")
                    soft_name=df_stocks.at[buy_id,1]
                    df_stocks.at[buy_id,3]-=1
                    df_stocks.at[buy_id,4]+=1
                    Skey=key_gen()
                    l_sales=[cus_name,soft_name,Skey]
                    df_sales=pd.DataFrame([l_sales])
                    print("\n You have bought 1 copy of",soft_name+".")
                    print("The product activation key for your copy of",soft_name,"is:",Skey)
                    print("Thank You for your purchase.")
                    df_stocks.to_csv("Softstocks.csv",header=False,columns=None)
                    df_sales.to_csv("Softsales.csv",mode="a",header=0,index=0)
                else:
                    print("Sorry for the inconvenience but the software is currently out of stock ... ")
            else:
                print("Sorry for the inconvenience but such a SId has not been registered to the database yet...")
            input("\n Press any key to continue.")
        elif choice==2:
            traverse_data()
            input("\n Press any key to continue.")
        elif choice==3:
            visualize_data("SPrice")
        else:
            break
  
    except FileNotFoundError:
        print("Sorry for the inconvenience no database has been set as of now...")
    input("\n Press any key to continue.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------     
def admin():#admin menu
 loop=True
 while loop==True:
        print("_______________________________________________________________________________________")
        print("WELCOME ADMINISTRATOR")
        print("1. Add new software")
        print("2. Remove software")
        print("3. Modify software data")
        print("4. Display all softwares available/ sales history")
        print("5. Find specific software")
        print("6. Search for a software by key")
        print("7. Search for customer")
        print("8. Graph data")
        print("9. Back to main menu")
        ch= int(input("Enter your choice: "))
        if ch == 1:
            add_data()
        elif ch == 2:
            remove=int(input("Enter the software ID to be removed from the database: "))
            remove_data(remove)
        elif ch == 3:
            modify_data()
        elif ch == 4:
            print("What do you want to traverse")
            print("1.Softwares")
            print("2.Sales")
            choice=int(input("Enter you option: "))
            if choice == 1:
                traverse_data()
                input("\n Press any key to continue.")
            elif choice == 2:
                traverse_sales()
            else:
                print("Invalid choice.")
        elif ch == 5:
            search=int(input("Enter the software ID to be searched for: "))
            print("Searching for",search,"in the database....")
            s=search_data(search)
            if s== -1:
                print("Such a software does not exist in the database.")
            input("\n Press any key to continue.")
        elif ch == 6:
            key=input("Enter the software key to be searched for: ")
            print("Searching the database for a matching key......")
            search_prod(key)
        elif ch == 7:
            cusname=input("Enter the name of the customer to be searched for: ")
            search_cus(cusname)
        elif ch == 8:
            graphby=input("What do you want to graph? \n SPrice \n SQuantity \n Sold\n")
            visualize_data(graphby)
        elif ch == 9:
            loop= False
        else:
            print("Invalid")
            break
#----------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------                
def menu():#mainmenu
 while True:
    print("_______________________________________________________________________________________")
    print("WELCOME TO HABO SOFTWARES")
    print("1. Login as User")
    print("2. Login as Admin")
    print("3. Exit")
    ch=int(input("Press the number corresponding to your desired choice: "))
    if ch == 1:
        user()
    elif ch == 2:
        password="admin"
        a=input("Please enter the password: ")
        if a==password:
            admin()
        else:
            print("Invalid password.")
    elif ch == 3:
        sys.exit()
    else:
        print("Invalid option")
#----------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------    
menu()
  
