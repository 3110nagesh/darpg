import pymongo
import matplotlib.pyplot as plt

from darpg_DB import get_database
dbname = get_database()
collection_name = dbname["users"]

#number of users with complaints from MOLBR organization
molbr = collection_name.count_documents({"org_code" : "MOLBR"})
print("the number of epfo complaints:", molbr)

#number of users with complaints from EPFO organization
epfo = collection_name.count_documents({"org_code" : "ROTH1"})
print("the number of epfo complaints:", epfo)

#number of users with complaints from MORLY organization
morly = collection_name.count_documents({"org_code" : "MORLY"})
print("the number of morly complaints:", morly)

#number of users with complaints from DOTEL organization
dotel = collection_name.count_documents({"org_code" : "DOTEL"})
print("the number of dotel complaints:", dotel)

department=['DOTEL', 'MOLBR', 'MORLY', 'ROTH1']
number_of_grievances=[dotel, molbr, morly, epfo]

plt.bar(department, number_of_grievances)
plt.title('Grievances Per Day (Number/Department)', fontsize = 12)
plt.xlabel('Department', fontsize = 12)
plt.ylabel('Number of Grievances', fontsize = 12)
plt.grid(True)
plt.show()
