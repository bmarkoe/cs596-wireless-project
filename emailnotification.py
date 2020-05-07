#library we are going to use to send our email
import smtplib

#This is the credential of the email address that will be sending the 
#the users emails, ideally this would be the companies email address
smtpUser ='tfroog@gmail.com'
smtpPass = 'hobosafeman33'

#this is the the email address of the user who will receive the notifications
toAdd = 'rmjunk11@gmail.com'
#from address, the same as the email credentials 
fromAdd = smtpUser

#We take in an input for the current weight of what we are weight, this would
#have retrieved from the scale 
print("Enter current weight of object")
weight = input()
#We take another input of the total weight of the objext. This is fine as a user
#because in a real world application the user would type in the total weight
print("Enter total weight of object")
totalWeight = input()
#calculate the perecentage
percentage = float(weight) / float (totalWeight) * 100

#draft of the parts of the email subject, header, and body
subject = 'Weight Notification'
header = 'To: ' + toAdd + '\n' + 'From: Smart Scale' + '\n' + "Subject: " + subject

#body of the message will change dependent on the calculation from the scale
if (percentage== 0):
    body = 'Milk is empty. Needs to be refilled'
else:
    body = 'Milk is ' + str (percentage) + '% full'
    

#print to log on our end
print(header + '\n' + body)

#use smtp lib to connect to email server
s = smtplib.SMTP('smtp.gmail.com', 587)

#encrypt email and ensure a secure transmission
s.ehlo()
s.starttls()
s.ehlo()

#log in to companies email that is sending (i.e Smart Scale)
s.login(smtpUser, smtpPass)

#send email
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

#quit
s.quit()