from sys import argv

script, filename = argv

print "we're going to erase %r." % filename
print "if you don't want that, hit ctrl-c,"
print "if you do want this, fit return"


raw_input("?")

print "opening the file...."
target = open(filename, 'w+')

#print "truncating the file. goodbye"
#target.truncate()  #erase whole data

print "now i'm going to ask you for three lines"

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "i'm going to write these to the file"

print >> target, '\n'.join([line1, line2, line3,'\n']) 
print "and finally, we close it"


target.close()


