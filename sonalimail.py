import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
sender='sonali.18bcs@cmr.edu.in'
receiver='sonaliranjan.bnc@gmail.com'
msg="hiii"
s.login(sender,'bcs95784')
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()
