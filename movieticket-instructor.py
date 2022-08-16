from ast import While
from secrets import choice


child_tix_price = 7.25
adult_tix_price = 11.50
tax_rate = .075
print( 'Welcome to the movies!')

cont_choice = "y"

while cont_choice == "y":
    print('1- Star Wars')
    print('2- Top Gun Maverick')
    print('3- Megamind')


    movie_choice = int(input('Which Movie do you want to see?  '))
    adult_tix = int(input('How many adult tickets do you want to purchase?  '))
    child_tix = int(input('How many child tickets do you want to purchase?  '))


# total price = (adult tx * adult price + child tx * child price) * (1+tax_rate)
    total_price = ((adult_tix * adult_tix_price) + (child_tix * child_tix_price)) * (1 + tax_rate)
    form_total_price = "{:.2f}".format(total_price)


    print (f'Thanks for your purchase! Your total is ${form_total_price}')
    cont_choice = str(input('Do you want more tickets? type y or n   '))

print('Bye')