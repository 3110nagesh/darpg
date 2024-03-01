# we create a set of users as a collection and add to the darpgDB database, this information is logged by a user from the pgportal website

from darpg_DB import get_database
dbname = get_database()
collection_name = dbname["users"]

user_1 = {
  "_id" : "0001234",
  "date" : "01-01-2024",
  "name" : "Amit",
  "description" : "non-sanctioning of house loan",
  "org_code" : "MOLBR",
  "organization" : "state bank of india",
  "age" : "34",
  "sex" : "M",
  "email" : "amit@gmail.com",
  "mobile" : "1111111111",
  "address" : "1 RP Bhawan MG Road",
  "dist_name" : "Belgaum",
  "state" : "Karnataka",
  "pincode" : "590001",
  "country" : "India",
}

user_2 = {
  "_id" : "0001235",
  "date" : "01-01-2024",
  "name" : "Ravi",
  "description" : "delay in receiving provident fund",
  "org_code" : "ROTH1",
  "organization" : "EPFO",
  "age" : "58",
  "sex" : "M",
  "email" : "ravi@gmail.com",
  "mobile" : "2222222222",
  "address" : "34 Sarad Nivas",
  "dist_name" : "Kanpur",
  "state" : "Uttar Pradesh",
  "pincode" : "208001",
  "country" : "India",
}

collection_name.insert_many([user_1,user_2])
