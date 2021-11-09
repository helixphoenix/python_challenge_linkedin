import smtplib, ssl

smtp_server= "smtp.gmail.com"
port=587
sender="fitifiti@gmail.com"
password=input("Type your pw and press enter:")


context= ssl.create_default_context()

def email(receiver_address, subject, message):
    
    mail_format=f"Subject:{subject}\n\n{message}"
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender,password)
        server.sendmail(sender,receiver_address,mail_format)
    except Exception as e:
        print(f"Mail could not be sent due to {e}")
    finally:
        server.quit()    
        
            
    
email("fitiifi@gmail.com","fitifiti","Hayat sevince Guzell Sevince farkli gunler bir gulu yasamayi bir cicegi sevin yeter")