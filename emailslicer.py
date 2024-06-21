email = input("Enter your email ID :").strip()

username = email[:email.index("@")]
domain = email[email.index("@")+1:]
print("your username is :",username)
print("your domain is :",domain)