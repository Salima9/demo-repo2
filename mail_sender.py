import smtplib

def sendEmail(subject, message, receiver):
    print("Sending Email to: " + str(receiver) + "...")
    # creates SMTP session
    host = 'smtp.gmail.com'
    port = 587
    s = smtplib.SMTP(host, port)
    user = "omurbekova359@gmail.com" # You're gmail id here
    password = "neyoagsvsghcyxnm" # You'r gmail app password here, not actual gmail password
    '''
   
    '''
    # start TLS for security
    s.ehlo()
    s.starttls()
    
    # Authentication (username, password)
    s.login(user, password)
    
    # message to be sent
    from_mail = "omurbekova359@gmail.com" # Your gmail id here. Most of the time should be same as your username.
    message = 'From: {}\nSubject: {}\n\n{}'.format(from_mail, subject, message)
    # print(message)
    # sending the mail
    s.sendmail(from_mail, receiver, message)
    
    # terminating the session
    s.quit()

def sendEmailVerification(code, receiver):
    sendEmail("Verification Code", "Your verification code is: " + str(code) + "\n\nApp Team", str(receiver).strip())