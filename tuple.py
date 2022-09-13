from typing import Tuple


Names = ("Joy", "Grace", "Ruth", "Kisel", "Godsave")
Name = list(Names)
Name[2] = ("Nipsy")
Name.append('Job')
Names =tuple(Name)
# print(Names)

Tuple1 = ("Grace", "Nipsy", "Kisel", "Godsave", "Job")
Tuple2 = ("Faith", "Comfort", "John", "Clement", "Lois")
Tuple3 = Tuple1 + Tuple2
print(Tuple3)
