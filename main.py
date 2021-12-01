import smtplib
from requests import get

import conf

print("***************************************************************")
recorded_ip = open("recorded_ip.txt", 'r', encoding="utf-8") #aktif IP görüntülenmesi
ip_recorded = open("recorded_ip.txt").readline().rstrip()
ip = get('https://api.ipify.org').content.decode('utf8')
print("Görülen IP adresiniz:", ip_recorded)

print("***************************************************************")
if ip_recorded != ip: #Kaydedilen ve anlık IP karşılaştırılması
    #smtp ile mail gönderim işlemi
    to = conf.receiver_mail
    user = conf.sender_mail
    pwd = conf.sender_password
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(user, pwd)
    header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:' + conf.subject
    print(header)
    msg = header + '\n\n' + conf.warning_message + ip + "\n" + conf.warning_message_cont + ip_recorded + '\n\n' #mail de gönderilecek
    smtpserver.sendmail(user, to, msg)                                                                          #mesaj
    print('Mail gönderildi!')
    smtpserver.quit()
    print("Güncel IP adresiniz: " + ip)
    recorded_ip = open('recorded_ip.txt', 'w+')  # kullanılan ip'nin kaydedilmesi
    recorded_ip.write(ip)
    recorded_ip.close()
else:
    print("IP adresinde herhangi bir değişikliğe rastlanmadı.")
    print("Güncel IP adresiniz: " + ip)
print("***************************************************************")


