import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('kanderovd@gmail.com', 'just123kidding')
mail_list = ["el.piankova@gmail.com"]
message = "Test text from Dmytro kanderov"
smtpObj.sendmail("kanderovd@gmail.com", mail_list, message)
smtpObj.quit()
