import emails

message = emails.html(html="Hi {{ name }},<br>This is a test email.",subject='Test Email',mail_from=('Test Sender', 'test@test.com'))
r = message.send(to=("Alex Wang", "alex3763@gmail.com"), render={"name":"Alex"}, smtp={'host': 'aspmx.l.google.com', 'timeout': 5})
print r.status_code
