# Message Object
msg = MIMEMultipart()
msg['Subject'] = 'Grievance Report for {}'.format()
msg['From'] = from_mail
msg['To'] = ', '.join([from_mail, to_mail])

# Attach the HTML code

msg.attach(MIMEText(html_string, 'html', 'utf-8')) 

# Send the email via SMTP 

serverserver = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.ehlo()
server.login(from_mail, from_password) 
server.sendmail(from_mail, [from_mail, to_mail], msg.as_string())
server.quit()
