import imaplib
import email as em
M = imaplib.IMAP4_SSL("imap.gmail.com")
email = "132548t@gmail.com"
password = "zvwajhuygbgcpzab"
M.login(email, password)
M.select("inbox")
result, ids = M.search(None, "FROM 132548t@gmail.com")

my_str = ids[0].decode("utf-8") # bytes to string
my_email_list = my_str.split(" ")
rest, content = M.fetch(my_email_list[-1], "(RFC822)")
print(content)
raw_content = content[0][1] # relative information of email
email_content = raw_content.decode("utf-8") # bytes to string
email_message = em.message_from_string(email_content)
    
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode = True) # string to bytes
        print(body)
        with open("email_content.txt", "wb") as f:
            f.write(body)