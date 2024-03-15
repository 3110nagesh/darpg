import pymongo

from darpg_DB import get_database

dbname = get_database()
collection_name = dbname["users"]

 #users with complaints from MOLBR organizationm
item_details = collection_name.find({"org_code" : "MOLBR"})
for item in item_details:
 print("user with molbr complaints:",item)

#users with complaints from EPFO organizationm
item_details = collection_name.find({"org_code" : "ROTH1"})
for item in item_details:
 print("user with epfo complaints:",item)

#users with complaints from MORLY organizationm
item_details = collection_name.find({"org_code" : "MORLY"})
for item in item_details:
 print("user with morly complaints:",item)

 #users with complaints from DOTEL organizationm
item_details = collection_name.find({"org_code" : "DOTEL"})
for item in item_details:
 print("user with dotel complaints:",item)

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
