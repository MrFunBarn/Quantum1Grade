# Brandon
# Spring 2016
#
# Dependancies:
#     Matplotlib
#
# Usageness:
#     Replace the values in the YOur Scores section with ( drum roll ), 
# Your scors for the various sectons of the quantum grade and run. A nice
# pretty plot should pop up. It is very possible that my maths are wrong
# for calculating the grades so, take it as you will.

import matplotlib.pyplot as plt

# Your Scores ####################################################################
# Scores are set to the class averages now.
# Your score the first and second midterms as percent 0-100.
t1 = 75.48
t2 = 75.48

# your homework average as decimal percent 0-1.
hw = 0.8559

# Your participation as percent 0-1.
particp = 0.8901

# Your extra credit as percent 0-1.
extracred = 0.7317

##################################################################################

# Initialze lists for final and grades.
final =[]
grade = []
gradenoextra = []

# Calculate Your Final Grade with and without extracredit for final
# exam scores from 0 to 100 % in stpes of 1 percent. Final Grade 
# with EC is calculated with,
#
# Grade = [65 - (extra_credit)*6.5) ] * (weighted ave exam score) 
#       + (extra_credit)*6.5 + 30*(homework) 
#       + 5*(participation)

for i in range(0,101,1):
    # Adds entry to final exam grades list.
    final.append(i)
    # Find midterm weighted average % 0->1.
    testavg = (.20*t1 + .20*t2 + .25*i) / 65
    # Test with extra credit.
    tests = (65 - (extracred*6.5)) * (testavg) 
    # Homework with extra credit.
    hws = extracred*6.5 + 30*hw
    # Participation as percent of total.
    participation = 5*particp
    # Final Grade with extra credit.
    grade.append( tests + hws + participation )
    # Final grade without extra credit.
    gradenoextra.append( 65*testavg + 30*hw + participation)


# Make the plot.
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

ax.plot( grade,final, 'b', lw=2)

ax.plot( gradenoextra,final,'b--', alpha=0.8)
ax.text(gradenoextra[50], 50,"No EC",ha='right',color='b', alpha=0.8)

LetterGrades = [89, 78, 66, 55 ]
#ax.vlines( LetterGrades, 0, 100)
plt.fill([89,100,100,89], [0,0,100,100], 'g', alpha=0.2)#, edgecolor='r')
plt.fill([78,89,89,78], [0,0,100,100], 'b', alpha=0.2)#, edgecolor='r'))#
plt.fill([66,78,78,66], [0,0,100,100], 'y', alpha=0.2)#, edgecolor='r')
plt.fill([55,66,66,55], [0,0,100,100], 'r', alpha=0.2)#, edgecolor='r')
plt.fill([0,55,55,0], [0,0,100,100], 'r', alpha=0.4)#, edgecolor='r')

ax.text(94, 10,"A's")
ax.text(83, 10,"B's")
ax.text(72, 10,"C's")
ax.text(60, 10,"D's")
ax.text(50, 10,"Fucked")

ax.vlines( (t1+t2)/2, 0, 100, color='r', alpha=0.8)
ax.text((t1+t2)/2, 95,"Midterm Average",ha='center',color='r', alpha=0.8)

ax.vlines( 100*hw, 0, 100, color='g')
ax.text(100*hw, 90,"H.W. Average",ha='center',color='g')

plt.xlabel('Final Grade (with extra credit)')
plt.ylabel('Grade on Final (%)')
plt.title('Quantum Final Grade')

ax.set_xlim( grade[0]-10, 100)
plt.show()
