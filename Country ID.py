#country ID#
print('Enter your country of origin...')
ct = input('Your Country: ')

#verification ID#
if ct == 'I am from Japan' or ct == 'Japan' or ct == 'japan':
    print ('Chotto, Nihongo, Hajimemashite')
elif ct == 'I am from United States' or ct == 'United States' or ct == 'united states':
    print ('Haha, American, Nice To Meet You! ')
elif ct == 'I am from Italy' or ct == 'Italy' or ct == 'italy':
    print('Mama Mia, Italiano, piacere di conoscerti! ')
elif ct == 'I am from German' or ct == 'German' or ct == 'german':
    print('Halloo, Deutsch, schon dich kennenzulernen! ')
else:
    print('Okay, I do not know your country. Sorry')
