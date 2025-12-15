from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
class Pateint(BaseModel):
    #ideal schema define here
   name:str = Annotated[str, Field(max_length=50, description="Enter your full name", title="Name", examples=["john ", "robert"])]
   email:EmailStr
   linkedin_url:AnyUrl
   age:int = Field(gt=0, lt=120, strict=True)
   
   #constraint
   weight:float = Field(gt=0)
   married:Optional[bool] = None
   allergies:Optional[ List[str]] = None
   contact_details:Dict[str, str]





def insert_patient( pateint:Pateint):
   print(pateint.name)
   print(pateint.age)
   print(pateint.weight)
   print(pateint.married)
   print(pateint.allergies)
   print(pateint.contact_details)
   print(pateint.email)
   print(pateint.linkedin_url)



   print("inserted")



pateint_info = {"name":"nitish", "age":30,"email":"abc@gmail.com",  "weight":70, "married":True, "allergies":["poolen", "dust"], "contact_details":{"email":"nitish@gmail.com", "phone":"302342312"}, "linkedin_url":"http://linkedin.com/1322"}

patient1 = Pateint(**pateint_info)

insert_patient(patient1)



    