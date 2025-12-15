from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, computed_field
from typing import List, Dict, Optional, Annotated


class Pateint(BaseModel):
    #ideal schema define here
   name:str 
   email:EmailStr
   linkedin_url:AnyUrl
   age:int #m
   height:float #mt
   #constraint
   weight:float #kg
   married:Optional[bool] = None
   allergies:Optional[ List[str]] = None
   contact_details:Dict[str, str]

   @computed_field
   @property
   def bmi_calculate(self)->float:
      bmi = round( self.weight/(self.height**2),2)
      return bmi
   





def insert_patient( pateint:Pateint):
   print(pateint.name)
   print(pateint.age)
   print(pateint.weight)
   print(pateint.married)
   print(pateint.allergies)
   print(pateint.contact_details)
   print(pateint.email)
   print(pateint.linkedin_url)
   print(pateint.height)
   print("BMI", pateint.bmi_calculate)





   print("inserted")


pateint_info = {"name":"nitish","height":1.72,  "age":65,"email":"abc@gmail.com",  "weight":70, "married":True, "allergies":["poolen", "dust"], "contact_details":{ "phone":"302342312", "emergency":"1234444"}, "linkedin_url":"http://linkedin.com/1322"}

patient1 = Pateint(**pateint_info)

insert_patient(patient1)

