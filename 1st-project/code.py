# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
# Concatenate both the strings
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

# Append the list
new_class=class_1 + class_2
# Print updated list
print(new_class)
new_class.append('Peter Warden')
print(new_class)
# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses={'math':65,'English':70,'History':80,'French':70,'Science':60}
values=courses.values()

# Slice the dict and stores  the all subjects marks in variable
total = sum(values)
print(total)
# Store the all the subject in one variable `Total`

# Print the total

# Insert percentage formula
percentage=(total/500)*100
# Print the percentage
print(percentage)



# Create the Dictionary
mathematics={'Geoffrey Hinton':'78',
 'Andrew Ng':'95',
 'Sebastian Raschka':'65',
 'Yoshua Benjio':'50',
'Hilary Mason':	'70',
'Corinna Cortes':'66',
'Peter Warden':'75' }

# Given string

topper= max(mathematics,key = mathematics.get)
print(topper)
# Create variable first_name 
first_name=topper[0:6]

# Create variable Last_name and store last two element in the list
Last_name=topper[7:9]
print(first_name)
print(Last_name)
full_name=topper.split()
print(full_name)
# Concatenate the string
full_name= Last_name+" "+first_name
# print the= full_name
print(full_name)
# print the name in upper case
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here


