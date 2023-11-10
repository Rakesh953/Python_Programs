#Class Member
class py_Spiders:
    c_name='Python FullStack development'
    b_name='Marthahalli'
p1=py_Spiders()
p2=py_Spiders()
p3=py_Spiders()

# Note:- Changing class member with the help of class reference 

py_Spiders.c_name='java fullstack Development' 
print(py_Spiders.c_name)
print(p1.c_name,p1.b_name)
print(p2.b_name)
print(p3.c_name)

# Note:- Changing class member with the help of object reference