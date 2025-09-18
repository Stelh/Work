import operator
# Exercices de merde j'ai tout test pour rien fallait pas mettre la student_list dans le submit

student_list = {
    "English": ['Tim', 'Carl', 'Dean', 'Jane', 'David'],
    "Maths": ['Jane', 'Mike', 'Ann', 'Kate', 'Nick', 'Jenny'],
    "Chemistry": ['Tim', 'Carl', 'Dean']
}

student_list_copy = {key: len(value) for key, value in student_list.items()}
print(max(dict(sorted(student_list_copy.items(), key=operator.itemgetter(1), reverse=True)).keys()))

##
# student_list_copy = dict((key, len(value)) for key, value in student_list.items())
# print(max(student_list_copy.items(), key=operator.itemgetter(1))[0])
##
##
#student_list_copy = {key: len(value) for key, value in student_list.items()}
###
# print(max(student_list_copy, key=student_list_copy.get))
###
# print(f"{max(student_list_copy.items(), key=operator.itemgetter(1))[0]}")
###
# student_list_sorted_by_value = dict(sorted(student_list_copy.items(), key=operator.itemgetter(1), reverse=True))
# print(f"{list(student_list_sorted_by_value.keys())[0]}")

