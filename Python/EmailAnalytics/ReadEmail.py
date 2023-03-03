import imaplib
import login

tmpVarList = (login.GetLoginInfo("GMAIL"))

mSrvr = imaplib.IMAP4_SSL('imap.gmail.com',993)

#print(IMAP4.error)

Usr = tmpVarList[0]
Pwd = tmpVarList[1]

mSrvr.login(Usr, Pwd)
mSrvr.select()

#typ, cnt = mSrvr.select("Inbox")

typ, data = mSrvr.search(None, 'ALL')

for num in data[0].split():
    #typ, data = mSrvr.fetch(num, '(UID BODY[TEXT])')
    typ, data = M.fetch(num, '(RFC822)')
    print('Message %s\n%s\n' % (num, data[0][1]))
#print(data[0][1])

mSrvr.close()
mSrvr.logout()
