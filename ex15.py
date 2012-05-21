from sys import argv

script, filename = argv

print "here's your file %r: " % filename

with open(filename) as input1:
    print input1.read()
    
print "i'll also ask you type it again:"
file_again = raw_input(">")

txt_again = open(filename)

print txt_again.read()
print file_again

txt_again.close()

