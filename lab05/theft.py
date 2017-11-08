# CREATE_ROW: used to create dict-style row for spreadsheet
# input:    columns (as list)
# output:   row (as dict)
def create_row(columns):
    # columns are: (0) start date,
    #              (1) start time,
    #              (2) end date,
    #              (3) end time,
    #              (4) free text
    d = {'start date': columns[0], 'start time': columns[1],
         'end date': columns[2], 'end time': columns[3],
         'text': columns[4]}
    return d

# read in contents of file, line by line
# this is hardcoded for my file system so will have to change!
prefix = '../data/'
f = open(prefix + 'church_metal_theft.csv', 'r')

print f

# parse lines into spreadsheet-type format, with each line as dict
spreadsheet = []
for line in f:
    # split line into columns
    columns = line.split(':::')
    row = create_row(columns)
    spreadsheet.append(row)

print spreadsheet

print spreadsheet[0]

def metal(text, metal_type):
    copper_list = []
    lead_list = []
    for x in range(len(text)):
        if metal_type[0] in text[x]:
            copper_list.append(x)
        if metal_type[1] in text[x]:
            lead_list.append(x)
    return copper_list,lead_list


coplist,llist=metal(spreadsheet,['copper','lead'])


print 'copper number of thefts is', len(coplist)
print 'lead number of thefts is', len(llist)

