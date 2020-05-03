import smtplib

smtpUser ='tfroog@gmail.com'
smtpPass = 'hobosafeman33'

toAdd = 'tfroog@gmail.com'
fromAdd = smtpUser

print("Enter current weight of object")
weight = input()
print("Enter total weight of object")
totalWeight = input()
percentage = weight/ float (totalWeight) * 100


subject = 'Weight Notification'
header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + "Subject: " + subject

if (percentage== 0):
    body = 'Object is empty. Needs to be refilled'
else:
    body = 'Object is ' + str (percentage) + '% full'
    

print header + '\n' + body

s = smtplib.SMTP('smtp.gmail.com', 587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

s.quit()