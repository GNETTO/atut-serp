
from serp import Serp

ent = ['houphouet boigny','laurent gbagbo']
attrs = ['date de naissance', 'nationalite']
serp = Serp(ent, attrs)
result = serp.start()

print(result)




