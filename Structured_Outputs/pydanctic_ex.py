from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str = 'Aalok'
    age:Optional[int] = None
    email:EmailStr
    cgpa:float=Field(gt=0,le=10,default=5)

new_stud={'age':32,'email':'abc@gmail.com','cgpa':2}


stud=Student(**new_stud)

print(stud)
print(stud.name)