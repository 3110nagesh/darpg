# import the necessary components

import smtplib 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
message = MIMEMultipart()
sender_email = "3110nagesh@gmail.com"
password = "duubkxurs" 
receiver_email = "3110nagesh@gmail.com"
message["Subject"] = "Grievance Report" 
message["From"] = sender_email 
message["To"] = receiver_email

# write the text/plain part 
text = "Hi, Kindly check the Grievance Report for January 1, 2024, feel free to let me know if there is any questions!" 

# write HTML part 
#the image files should be saved in a server path and accessed via a URL

html = """
<!Doctype html>
<head>
<title>Grievance Report</title>
<meta charset="UTF-8">
<meta name="description" content="">
<meta name="description" content="Department of Administrative Reforms and Public Grievance,  Centralised Public Grievance Redress and Monitoring System">
<meta name="keywords" content="Bharath, India, DARPG, Administration, Public, Grievance, CPGRAMS, Meripehchaan, Janparichay">
<meta name="author" content="DARPG_913, Nagesh">
<meta http-equiv="refresh" content="60">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style> footer {text-align: center;} </style>
<style> .header {padding: 10px; text-align: center;} </style>
</head>
<body style="text-align:center; border: 2px solid black">
<div class="header">
<!-- add image from the server path via URL to reflect the image in the email-->
<img src="darpg.png" alt = "darpg">
</div>
<h2> GRIEVANCE REPORT (January 1, 2024)</h2>
<img src="reports.png" alt = "report">
</body>
<footer> DARPG </footer>
</html>"""

# convert to MIMEText objects and add them to the MIMEMultipart message 
part1 = MIMEText(text, "plain") 
part2 = MIMEText(html, "html") 
message.attach(part1) 
message.attach(part2) 

# send email
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message.as_string()) 

print('sent')