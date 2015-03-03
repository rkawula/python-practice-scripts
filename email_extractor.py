import re

doc = open("docs/club_emails.txt")
email_regex = re.compile(".+@mills.edu")

for line in doc:
	if email_regex.match(line):
		print line
		
doc.flush()
doc.close()