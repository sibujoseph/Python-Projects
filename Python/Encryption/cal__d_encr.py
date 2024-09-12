import os, sys
import random #module

PYTHON_PROJECT_PATH=os.environ['PYTHON_PROJECT_PATH']

def fn_ser_EncrData (iv_str_UsrNm=''):
#Function Encrypts data using Randomization


    #Declaration
    #Get Date    
    v_int_Dt
    
    random.randint(1, v_int_Dt)
    


def fn_lst_GetLoginInfo(iv_str_LoginContext, iv_str_path=None):
#Function returns Login Credentials as List
    #Declaration
    v_lst_Credn = []
    #Read the credentials
    if iv_str_path is None:
        iv_str_path='PYTHON_PROJECT_PATH/Email Analytics' #os.getcwd()
    v_fl_LoginFile = open(iv_str_path+"\Login.protected", "r")
    for v_ln_EachLine in v_fl_LoginFile:
        if "#" not in v_ln_EachLine:      #Exclude lines with any comments in the file
          if v_ln_EachLine.strip().split(":")[0] == iv_str_LoginContext:
            v_lst_Credn = v_ln_EachLine.strip().split(":")[1]
    v_fl_LoginFile.close()

    return v_lst_Credn



def fn_lst_GetEmailFolders(iv_Email_Conn_Obj=None):
#To get the final list of all email folder names
    v_lst_FinalListOfEmailFolders = []
    v_lst_EmailFolderList = iv_Email_Conn_Obj.list()

    #Only if the connection succeeded
    if v_lst_EmailFolderList[0] == "OK":
        v_lst_ListOfEmailFolders =  v_lst_EmailFolderList[1]     #Get the byte folder list
        for v_bytstr_EachFolder in v_lst_ListOfEmailFolders:
            #Convert byte string to string
            v_str_DecodedFolder=(v_bytstr_EachFolder.decode("utf-8"))
            #Substring; Append to Final List (Upper Case)
            v_lst_FinalListOfEmailFolders.append(v_str_DecodedFolder[v_str_DecodedFolder.index('/')+2:].upper().strip())             
    else:
        print("GetEmailFolders() : Error in iv_Email_Conn_Obj")
            
    #iv_Email_Conn_Obj.close()
    #iv_Email_Conn_Obj.logout()
    return sorted(v_lst_FinalListOfEmailFolders)