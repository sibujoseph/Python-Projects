#sys is a module. 
#To	 list all modules running on your python.
import sys as s
print(sorted(s.modules.keys())) 


#sys lets to access comand line arguments which gets stored in sys.argv
#example 
if len(sys.argv) < 2:
    print("Error! Please supply input or configuration.")
    exit(1)
    
# To access environment variable (when adding new env variables, reboot the system)
import os, sys
import platform
PYTHON_PROJECT_PATH=os.environ['PYTHON_PROJECT_PATH']
print(PYTHON_PROJECT_PATH)

#To access PATH variable
print(os.environ.get('PATH', os.defpath))

#To read a file
mypath=PYTHON_PROJECT_PATH+"\\"+"a.py"
exec(open(mypath).read())
#To get dir name of a file
here = os.path.dirname(os.path.abspath(mypath))
print(here)

# """To import a .py file in jupyter"""
print(sys.path)
WorkingFolder = PYTHON_PROJECT_PATH+"\Email Analytics"
print(WorkingFolder)
sys.path.insert(0, WorkingFolder)
print(sys.path)


##To reload a python module after it changes
import importlib
import login #import the module here, so that it can be reloaded.
importlib.reload(login)


##To setup virtual environments (mainly to test new releases/versions of python/libraries for existing code)
##Using Anconda
conda create --name <name of env> <base package of python that you want the new env>
##eg. conda create --name NewEnvNumPy numpy    #since version of python is not mentioned, default version will be used
##    activiate NewEnvNumPy

##eg. conda create --name NewEnvPyVer python=3.5 anaconda #downloads python 3.5 with all libraries from anaconda
##eg. conda create --name NewEnvPyVer python=3.5 numpy #downloads python 3.5 with numpy module only
##    activiate NewEnvPyVer

##To list all virtual envs
conda info --envs

##To substitute variables with values in a string, use format
"Hello {}, your room number is {}".format(name,room_number)
"Hello {n}, your room number is {r}. The room {r} is located here: {loc}. Welcome again, {n} !".format(n=name,r=room_number,loc=location)


##Use set to remove duplicates
print(set{1,2,3,4,5,5,3,4,2,1,8,9})
1,2,3,4,5,8,9

print({1,2,3,4,5,5,3,4,2,1,8,9})
1,2,3,4,5,8,9


##List comprehenison
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)

    #Above can be rewritten with list comprehension
    print([num**2 for num in x])


##Tuple unpacking
t = ([1,2],[3,4],[5,6])  #--> tuples with lists
for a,b in t:       #--> a,b is tuple unpacking
    print(a)
    print(b)

##Mapping list of values as input to a lambda function 
print(list(map((lambda x:x*3), [a*b for a,b in t])))
#=[6, 36, 90]




