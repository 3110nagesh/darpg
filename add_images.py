# Open the visual

with open(file_img, 'rb') as fp: 
img = MIMEImage(fp.read()) 
img.add_header('Content-Disposition', 'attachment', filename=file_img) 
img.add_header('X-Attachment-Id', '0') 
img.add_header('Content-ID', '<0>') 
fp.close() 
msg.attach(img) 

# Open the header

with open(file_header, 'rb') as fp: 
img = MIMEImage(fp.read()) 
img.add_header('Content-Disposition', 'attachment', filename=file_header) 
img.add_header('X-Attachment-Id', '1') 
img.add_header('Content-ID', '<1>') 
fp.close() msg.attach(img)
