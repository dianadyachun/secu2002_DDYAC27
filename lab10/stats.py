import csv
f = open ('../../secu2002_master/data/london_gang_attr.csv', 'r')
r = csv.DictReader (f,delimiter = ',')
age_str = []
arrests_str = []
convictions_str = []
prison_str = []
in_prison = 0


for row in r:
    age_str.append(int(row['Age']))
    arrests_str.append(int(row['Arrests']))
    convictions_str.append(int(row['Convictions']))
    prison_str.append(int(row['Prison']))


for item in age_str:
    av_age = sum(age_str)/len(age_str)
    min_age = min(age_str)
    max_age = max(age_str)
for item in arrests_str:
    total_arrests = sum(arrests_str)
for item in convictions_str:
    total_convictions = sum(convictions_str)
for item in prison_str:
    if item == 1:
        in_prison += 1


print '(1) The mean age is ' + str(av_age)
print '(2) The age range is from ' + str(min_age) + ' to ' + str(max_age)
print '(3) The total number of arrests across all gang members is ' + str(total_arrests)
print '(4) The total number of convictions is ' + str(total_convictions)
print '(5) The total number of members who have spent time in prison is ' + str(in_prison)

