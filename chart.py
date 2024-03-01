import pymongo
import matplotlib.pyplot as plt

from darpg_DB import get_database
dbname = get_database()
collection_name = dbname["users"]

DOTEL1 = collection_name.find({"org_code":"DOTEL"}).count();
MOLBR1 = collection_name.find({"org_code":"MOLBR"}).count();
MORLY1 = collection_name.find({"org_code":"MORLY"}).count();
MEAPD1 = collection_name.find({"org_code":"MEAPD"}).count();
DORLD1 = collection_name.find({"org_code":"DORLD"}).count();
DPLNG1 = collection_name.find({"org_code":"DPLNG"}).count();
CBODT1 = collection_name.find({"org_code":"CBODT"}).count();

department=['DOTEL', 'MOLBR', 'MORLY', 'MEAPD','DORLD','DPLNG','CBODT']
number_of_grievances=['DOTEL1', 'MOLBR1', 'MORLY1', 'MEAPD1','DORLD1','DPLNG1','CBODT1']

plt.bar(department, number_of_grievances)
plt.title('Grievances Per Day (Number/Department)', fontsize = 12)
plt.xlabel('Department', fontsize = 12)
plt.ylabel('Number of Grievances', fontsize = 12)
plt.grid(True)
plt.show()
