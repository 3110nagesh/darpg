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
  "organization" : "sbi",
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
  "age" : "44",
  "sex" : "M",
  "email" : "ravi@gmail.com",
  "mobile" : "2222222222",
  "address" : "34 Sarad Nivas",
  "dist_name" : "Kanpur",
  "state" : "Uttar Pradesh",
  "pincode" : "208001",
  "country" : "India",
}


user_3 = {
  "_id" : "0001236",
  "date" : "01-01-2024",
  "name" : "Raj",
  "description" : "improper railway crossing",
  "org_code" : "MORLY",
  "organization" : "railways",
  "age" : "62",
  "sex" : "M",
  "email" : "raj@gmail.com",
  "mobile" : "3333333333",
  "address" : "3 Sham Nivas",
  "dist_name" : "Chennai",
  "state" : "Tamil Nadu",
  "pincode" : "600001",
  "country" : "India",
}


user_4 = {
  "_id" : "0001237",
  "date" : "01-01-2024",
  "name" : "Rahul",
  "description" : "delay in receiving provident fund",
  "org_code" : "ROTH1",
  "organization" : "EPFO",
  "age" : "58",
  "sex" : "M",
  "email" : "rahul@gmail.com",
  "mobile" : "4444444444",
  "address" : "4 Sapna Nilaya",
  "dist_name" : "Bhopal",
  "state" : "Madhya Pradesh",
  "pincode" : "462001",
  "country" : "India",
}


user_5 = {
  "_id" : "0001238",
  "date" : "01-01-2024",
  "name" : "Ram",
  "description" : "non-connectivity of internet",
  "org_code" : "DOTEL",
  "organization" : "jio",
  "age" : "35",
  "sex" : "M",
  "email" : "ram@gmail.com",
  "mobile" : "5555555555",
  "address" : "7 Sita Nivas",
  "dist_name" : "Kannur",
  "state" : "Kerala",
  "pincode" : "670001",
  "country" : "India",
}


user_6 = {
  "_id" : "0001239",
  "date" : "01-01-2024",
  "name" : "Ranu",
  "description" : "delay in receiving provident fund",
  "org_code" : "ROTH1",
  "organization" : "EPFO",
  "age" : "55",
  "sex" : "F",
  "email" : "ranu@gmail.com",
  "mobile" : "6666666666",
  "address" : "#14 Diksha Apartments",
  "dist_name" : "Deoghar",
  "state" : "Jharkhand",
  "pincode" : "814112",
  "country" : "India",
}


user_7 = {
  "_id" : "0001231",
  "date" : "01-01-2024",
  "name" : "Rinku",
  "description" : "non-sanctioning of house loan",
  "org_code" : "MOLBR",
  "organization" : "sbi",
  "age" : "46",
  "sex" : "M",
  "email" : "rinku@gmail.com",
  "mobile" : "7777777777",
  "address" : "3 Sindhu Mahal",
  "dist_name" : "Kolkata",
  "state" : "West Bengal",
  "pincode" : "700001",
  "country" : "India",
}


user_8 = {
  "_id" : "0001232",
  "date" : "01-01-2024",
  "name" : "Raja",
  "description" : "improper railway crossing",
  "org_code" : "MORLY",
  "organization" : "railways",
  "age" : "28",
  "sex" : "M",
  "email" : "Raja@gmail.com",
  "mobile" : "8888888888",
  "address" : "4 Raja Nivas",
  "dist_name" : "Haridwar",
  "state" : "Uttarakhand",
  "pincode" : "249401",
  "country" : "India",
}


user_9 = {
  "_id" : "0001233",
  "date" : "01-01-2024",
  "name" : "Ramu",
  "description" : "non-sanctioning of house loan",
  "org_code" : "MOLBR",
  "organization" : "sbi",
  "age" : "31",
  "sex" : "M",
  "email" : "Ramu@gmail.com",
  "mobile" : "99999999999",
  "address" : "8 Lal Mansion",
  "dist_name" : "Anantapur",
  "state" : "Andhra Pradesh",
  "pincode" : "515134",
  "country" : "India",
}


user_10 = {
  "_id" : "0001230",
  "date" : "01-01-2024",
  "name" : "Rohit",
  "description" : "non-connectivity of internet",
  "org_code" : "DOTEL",
  "organization" : "jio",
  "age" : "39",
  "sex" : "M",
  "email" : "Rohit@gmail.com",
  "mobile" : "1234567890",
  "address" : "4 Sahyadri Nivas",
  "dist_name" : "Mumbai",
  "state" : "Maharashtra",
  "pincode" : "400001",
  "country" : "India",
}

collection_name.insert_many([user_1,user_2,user_3,user_4,user_5,user_6,user_7,user_8,user_9,user_10])
