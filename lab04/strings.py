#working with David and Jordan
# TASK 1

# #define function my_join
def my_join(mysep, mylist):
    #create a list where added values are stored
    join = ''
    #create a for loop for mylist
    for x in mylist:
        #adding values in mylist and mysep to join
        join += x + mysep
    #return a updated join
    return join

print my_join('*',['a','s','r'] )



#TASK 2

#defines a function that sorts the string alphabetically
def sort_string(my_string):
    #list command converts a string into a list
    mylist = list(my_string)
    #print mylist
    #sort command sorts the variables in the list alphabetically
    mylist.sort()
    #print mylist
    #creating an empty string
    s = ''
    #joining the variables in the list
    u = s.join(mylist)
    return u

#definig the my_string variable
my_string = 'pizza'
#printing the sorted string
print sort_string(my_string)


#TASK 3


# set up a mapping from bases to their complements (a <-> t, g <-> c)
# these need to be ordered in the same way in order to enable mapping
# could also try to do this with list of pairs
base_str = 'atgc'
comp_str = 'tacg'

dna1 = 'wedwed'
dna2 = 'dfsdfd'
dna3 = 'sdvdf'
dna4 = 'fgdfgdf'
dna5 = 'sgsfgwe'

# generate some strand of dna
dna = 'atgcaattgcaattcgtagc'

############
# REVERSE  #

def reverse_dna(dna):
    # store reverse as list to allow mutability, use dummy values initially
    reverse_list = ['0'] * len(dna)
    # now fill in dummy values by going through dna forwards and filling in
    # reverse_list backwards
    for i in range(1, len(dna) + 1):
        reverse_list[-i] = dna[i - 1]
    # now form list into string
    reverse_dna = ''.join(reverse_list)
    return reverse_dna


# use fancy syntax to check answer
print 'reverse should be\t', dna[::-1]
print 'reverse is\t\t', reverse_dna(dna)
print '------------'

print 'reverse should be\t', dna1[::-1]
print 'reverse is\t\t', reverse_dna(dna1)
print '------------'

print 'reverse should be\t', dna2[::-1]
print 'reverse is\t\t', reverse_dna(dna2)
print '------------'

print 'reverse should be\t', dna3[::-1]
print 'reverse is\t\t', reverse_dna(dna3)
print '------------'

print 'reverse should be\t', dna4[::-1]
print 'reverse is\t\t', reverse_dna(dna4)
print '------------'

print 'reverse should be\t', dna5[::-1]
print 'reverse is\t\t', reverse_dna(dna5)
print '------------'


###############
# COMPLEMENT  #
###############
def comp_dna(dna):
    comp_dna = ''
    for char in dna:
        # find the index of char in base_str
        i = base_str.index(char)
        # now find the associated char in the mapped string comp_str
        # (this is why we needed the same order)
        comp_dna += comp_str[i]
    return comp_dna


# hardcoded expected results obtained by doing it by hand
print 'complement should be\t', 'tacgttaacgttaagcatcg'
print 'complement is\t\t', comp_dna(dna)
print '------------'

print 'complement is\t\t', comp_dna(dna1)
print 'complement is\t\t', comp_dna(dna2)


#######################
# REVERSE COMPLEMENT  #
#######################

def reverse_comp_dna(dna):
    # store reverse as list to allow mutability, use dummy values initially
    reverse_list = ['0'] * len(dna)
    # now fill in dummy values by going through dna forwards and filling in
    # reverse_list backwards
    for i in range(1,len(dna)+1):
        char = dna[i-1]
        o = base_str.index(char)
        reverse_list[-i] = comp_str[o]
    reverse_comp_dna = ''.join(reverse_list)
    return reverse_comp_dna


# hardcoded expected results obtained from reverse-complement.com
print 'reverse complement should be\t', 'gctacgaattgcaattgcat'
print 'reverse complement is\t\t', reverse_comp_dna(dna)

