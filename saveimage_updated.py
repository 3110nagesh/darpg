# save the image
import matplotlib.pyplot as plt
from darpg_DB1 import get_database

dbname = get_database()
collection_name = dbname["users"]

#number of users with complaints from MOLBR organization
molbr = collection_name.count_documents({"org_code" : "MOLBR"})
#number of users with complaints from EPFO organization
epfo = collection_name.count_documents({"org_code" : "ROTH1"})
#number of users with complaints from MORLY organization
morly = collection_name.count_documents({"org_code" : "MORLY"})
#number of users with complaints from DOTEL organization
dotel = collection_name.count_documents({"org_code" : "DOTEL"})

department=['DOTEL', 'MOLBR', 'MORLY', 'ROTH1']
number_of_grievances=[dotel, molbr, morly, epfo]

fig, ax = plt.subplots()
plt.bar(department, number_of_grievances)
plt.title('Grievances Per Day (Number/Department)', fontsize = 12)
plt.xlabel('Department', fontsize = 12)
plt.ylabel('Number of Grievances', fontsize = 12)
plt.grid(True)
#save the image file in the present working directory
fig.savefig('reports.png')
plt.close(fig)