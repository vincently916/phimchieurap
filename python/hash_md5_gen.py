import md5

password = raw_input("Enter a password to hash: ")

m = md5.new(password).hexdigest()

print m
