from sys import argv

script, file_name = argv

text = open(file_name)
print "Here is your file, %r" % file_name
print text.read()

print "Type the file_name again:"
file_again = raw_input("> ")
text_again = open(file_again)

print text_again.read()
