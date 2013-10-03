import sys

if len(sys.argv[1:])<3:
    print "the program takes a list of three or more words from command line"

else:
    raw_input = sys.argv[1:]
    raw_input = sorted(raw_input)
    print ', '.join(raw_input[:-1]) +', and '+raw_input[-1] + '.'
    sentence = ', '.join(raw_input[:-1])
    sentence = sentence.capitalize()
    print sentence + ', and '+raw_input[-1] + '.'
