#ex1

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#1
print phonebook_dict['Elizabeth']

#2
phonebook_dict['Kareem'] = '938-345-2345'

#3
del phonebook_dict['Alice']

#4
phonebook_dict['Bob'] = '968-345-2345'

#5
print phonebook_dict[*]
