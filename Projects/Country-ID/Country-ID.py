#country ID#
print('Enter your country of origin...')
country = str(input('Your Country: '))

#verification ID#
if country == 'I am from Japan' or country == 'Japan' or country == 'japan':
    print ('Chotto, Nihongo, Hajimemashite')

elif country == 'I am from United States' or country == 'United States' or country == 'united states':
    print ('Haha, American, Nice To Meet You! ')

elif country == 'I am from Italy' or country == 'Italy' or country == 'italy':
    print('Mama Mia, Italiano, piacere di conoscerti! ')

elif country == 'I am from German' or country == 'German' or country == 'german':
    print('Halloo, Deutsch, schon dich kennenzulernen! ')
    
else:
    print('Okay, I do not know your country. Sorry')
