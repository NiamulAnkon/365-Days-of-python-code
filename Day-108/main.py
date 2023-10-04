import smtplib as sb

ob = sb.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('niamulankon966@gmail.com', 'wsxokn963258poklrtfg678500hbd2012')
subject = "Testing mail"
body = "Walkers Join"
message = "subject:{}\n\n{}".format(subject, body)
list_add = ["aanonto643@gmail.com"]

ob.sendmail('niamulankon966@gmail.com', list_add, message)
print("send mail to")
ob.quit()
