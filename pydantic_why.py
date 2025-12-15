def insert_patient(name:str, age:int):
    if(age<0):
        raise ValueError("age is not less than zero")
    else:
        if(name, str) and (age, int):
            print(name)
            print(age)
            print("data is inserted in to databse")
        else:
            raise TypeError("data type is not valid")  
insert_patient("abc", 10)    

