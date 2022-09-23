from classes.greetings import Greetings
from classes.wine import Wine
from classes.pair import Pair
from classes.recipe import Recipe
from simple_term_menu import TerminalMenu
import clearing
import cowsay



cabernet_sauvignon = Pair(
Wine('Cabernet sauvignon'),
Recipe(
'Roast beef',
'''
ROAST BEEF:

500g of beef 
100g of butter
Salt and Pepper to taste

METHOD: 
Put the beef on a tray, rub butter salt and pepper all over, 
put it in the oven at 180° for 1hour.

''',
'main'
),
Recipe(
'Gouda cheese',
'''
CHEESE BOARD: 

Gouda cheese 
Prosciutto 
Walnuts

''',
'cheese'
),
Recipe(
'Plums',
'''
DESSERT:

Plums
Honey
Cream

''',
'fruit'
)
)

# pinot_noir = Pair(
#                     'Pinot noir', 
#                     'Salmon', 
#                     'Gruyere cheese', 
#                     'Apples', 
#                     '''\n SALMON: \n 2 Slices of Salmon \n 100g of Butter \n 
#                     Salt and pepper to taste \n Italian herbs \n \n 
#                     METHOD: \n Season the fish with salt, pepper and herbs, 
#                     \n add butter to a frying pan, cook both sides of \n the 
#                     fish untill preferred level of doneness.\n''', 
#                     '\n CHEESE BOARD: \n Gruyere cheese \n Bacon \n Almonds \n', 
#                     '\n DESSERT: \n Apples \n Brown Sugar \n Cinammon \n'
#                     )

# shiraz = Pair(
#                 'Shiraz', 
#                 'Duck', 
#                 'Pecorino cheese', 
#                 'Apricot', 
#                 '''\n DUCK: \n 200g Duck Breasts \n 2tb of Olive Oil \n 1 Clove of garlic 
#                 \n Lemon Pepper, Salt, to taste \n \n METHOD: \n Preheat oven to 180°, season the breasts with salt, 
#                 \n Pepper and garlic, add Olive Oil to a frying pan, \n cook both sides untill brown, 
#                 finish cooking for another 20min in the oven.\n''', 
#                 '\n CHEESE BOARD: \n Pecorino cheese \n Ricotta \n Ham \n', 
#                 '\n DESSERT: \n Apricot \n Tahini \n Attar \n Pistachios \n'
#                 )

# merlot = Pair(
#                 'Merlot', 
#                 'Pork', 
#                 'Camembert cheese', 
#                 'Figs', 
#                 '''\n PORK: \n 1 Pork Leg \n Salt Pepper \n Aluminium Foil \n Oil \n \n 
#                 METHOD: \n Get a Tray, add the pork leg, rub salt and pepper, 
#                 \n add oil for the crackling, roll aluminium foil around \n 
#                 the tray, bake at 180° for 2 hours.\n''', 
#                 '\n CHEESE BOARD: \n Camembert cheese \n Cashew Nuts \n Olive Oil \n', 
#                 '\n DESSERT: \n Figs \n Brown Sugar \n Lemon Juice \n Zest \n Cream or Icecream \n'
#                 )

# sangiovese = Pair(
#                     'Sangiovese', 
#                     'Spaghetti Bolognese', 
#                     'Mozzarella cheese', 
#                     'Strawberry', 
#                     '''\n SPAGHETTI BOLOGNESE: \n 500g minced meat \n 1 can tomato sauce \n 500g Spaghetti 
#                     \n Parmesan cheese \n oil \n 1 onion \n 1 clove of Garlic \n salt pepper \n \n 
#                     METHOD: \n Cook spaghetti pasta in salty boiling water, \n fry oil with onion and garlic, 
#                     add seasoned minced meat, \n when meat is done add tomato sauce, cook for 20 minutes, \n 
#                     add water if needed, mix it with the pasta, add some parmesan, enjoy.\n''', 
#                     '\n CHEESE BOARD: \n Mozzarella cheese \n Jam \n Brazil Nuts \n', 
#                     '\n DESSERT: \n Strawberry \n Condensed Milk \n'
#                     )

# chianti = Pair(
#                 'Chianti', 
#                 'Pizza', 
#                 'Parmesan cheese', 
#                 'Apples', 
#                 '''\n PIZZA: \n 1 Sliced Pepperoni sausage \n mozzarella cheese \n tomato sauce \n pizza base 
#                 \n oregano \n \n METHOD: \n preheat oven to 180, get a tray, put the pizza base, \n 
#                 spread tomato sauce, add cheese, add sliced pepperoni, \n add oregano, bake for 10 to 20 minutes.\n''', 
#                 '\n CHEESE BOARD: \n Parmesan cheese \n Pepperoni \n Brown Sugar \n', 
#                 '\n DESSERT: \n Apples \n Brown Sugar \n Cinammon \n'
#                 )

# bordeaux = Pair(
#                 'Bordeaux', 
#                 'Lamb', 
#                 'Brie cheese', 
#                 'Pears', 
#                 '''\n LAMB: \n 1 leg of lamb \n rosemary \n thyme \n olive oil \n salt and pepper \n 7spices \n \n 
#                 METHOD: \n Preheat oven to 180, put the leg of lamb on a tray, add the 7 spices, \n salt and pepper, 
#                 olive oil and rub, bake for 2 hours.\n''', 
#                 '\n CHEESE BOARD: \n Brie cheese \n Truffles \n Peanuts \n', 
#                 '\n DESSERT: \n Pears \n Maple Syrup \n Macadamia Nuts \n'
#                 )

# tempranillo = Pair(
#                     'Tempranillo', 
#                     'Lasagna', 
#                     'Manchego cheese', 
#                     'Cherries', 
#                     '''\n LASAGNA: \n 500g minced meat \n 1can tomato sauce \n 500g Lasagna sheets \n Mozzarella cheese \n 
#                     oil \n 1 onion \n 1 clove of Garlic \n salt pepper \n \n METHOD: \n Fry oil with onion and garlic, 
#                     add seasoned minced meat, when meat \n is done add tomato sauce, cook for 20 minutes, add water if \n 
#                     needed, get a tray, add a layer of sauce, cheese and lasagna sheets, \n repeat untill you reach the 
#                     top of the tray, bake for 40min at 180°.\n''', 
#                     '\n CHEESE BOARD: \n Manchego cheese \n Jamon \n Toasted Sunflower Seeds \n', 
#                     '\n DESSERT: \n Cherries \n Cream \n Honey \n'
#                     )

# carmenere = Pair(
#                 'Carmenere', 
#                 'BBQ', 
#                 'Cheddar cheese', 
#                 'Plums', 
#                 '''\n BBQ: \n Beef \n sausages \n Charcoal \n Salt and pepper \n \n METHOD: \n light up the charcoal, 
#                 season the beef with salt and pepper, \n grill the meat and sausages.\n''', 
#                 '\n CHEESE BOARD: \n Cheddar cheese \n Smoked Almonds \n Barbecue Sauce \n', 
#                 '\n DESSERT: \n Plums \n Maple Syrup \n'
#                 )

# rose = Pair(
#             'Rose', 
#             'Seafood', 
#             'Feta cheese', 
#             'Watermelon', 
#             '''\n SEAFOOD: \n 500g of mixed seafood \n 1 lemon or lime \n 100g butter \n salt and pepper \n 2 cloves of garlic \n \n 
#             METHOD: \n Add butter and garlic to a frying pan, season seafood \n with salt and pepper, fry for 6 minutes.\n''', 
#             '\n CHEESE BOARD: \n Feta cheese \n Anchovies \n Tzatziki Sauce \n', 
#             '\n DESSERT: \n Watermelon \n does not need anything else \n'
#             )

wine_list = [
    cabernet_sauvignon,
    # pinot_noir,
    # shiraz,
    # merlot,
    # sangiovese,
    # chianti,
    # bordeaux,
    # tempranillo,
    # carmenere,
    # rose
]


# cabernet_sauvignon_pair = Pair('Cabernet sauvignon', 'Roast beef', 'Gouda cheese', 'Plums')
# pinot_noir_pair = Pair('Pinot noir', 'Salmon', 'Gruyere cheese', 'Apples')
# shiraz_pair = Pair('Shiraz', 'Duck', 'Pecorino cheese', 'Apricot')
# merlot_pair = Pair('Merlot', 'Pork', 'Camembert cheese', 'Figs')
# sangiovese_pair = Pair('Sangiovese', 'Spaghetti Bolognese', 'Mozzarella cheese', 'Strawberry')
# chianti_pair = Pair('Chianti', 'Pizza', 'Parmesan cheese', 'Apples')
# bordeaux_pair = Pair('Bordeaux', 'Lamb', 'Brie cheese', 'Pears')
# tempranillo_pair = Pair('Tempranillo', 'Lasagna', 'Manchego cheese', 'Cherries')
# carmenere_pair = Pair('Carmenere', 'BBQ', 'Cheddar cheese', 'Plums')
# rose_pair = Pair('Rose', 'Seafood', 'Feta cheese', 'Watermelon')

# pair_list = [
#     cabernet_sauvignon_pair,
#     pinot_noir_pair,
#     shiraz_pair,
#     merlot_pair,
#     sangiovese_pair,
#     chianti_pair,
#     bordeaux_pair,
#     tempranillo_pair,
#     carmenere_pair,
#     rose_pair
# ]

# cabernet_sauvignon_recipe = Recipe('Cabernet sauvignon', '\n ROAST BEEF: \n 500g of beef \n 100g of butter \n Salt and Pepper to taste \n \n METHOD: \n Put the beef on a tray, rub butter salt and pepper all over, \n put it in the oven at 180° for 1hour.\n', '\n CHEESE BOARD: \n Gouda cheese \n Prosciutto \n Walnuts \n ', '\n DESSERT: \n Plums \n Honey \n Cream \n')
# pinot_noir_recipe = Recipe('Pinot noir', '\n SALMON: \n 2 Slices of Salmon \n 100g of Butter \n Salt and pepper to taste \n Italian herbs \n \n METHOD: \n Season the fish with salt, pepper and herbs, \n add butter to a frying pan, cook both sides of \n the fish untill preferred level of doneness.\n', '\n CHEESE BOARD: \n Gruyere cheese \n Bacon \n Almonds \n', '\n DESSERT: \n Apples \n Brown Sugar \n Cinammon \n')
# shiraz_recipe = Recipe('Shiraz', '\n DUCK: \n 200g Duck Breasts \n 2tb of Olive Oil \n 1 Clove of garlic \n Lemon Pepper, Salt, to taste \n \n METHOD: \n Preheat oven to 180°, season the breasts with salt, \n Pepper and garlic, add Olive Oil to a frying pan, \n cook both sides untill brown, finish cooking for another 20min in the oven.\n', '\n CHEESE BOARD: \n Pecorino cheese \n Ricotta \n Ham \n', '\n DESSERT: \n Apricot \n Tahini \n Attar \n Pistachios \n')
# merlot_recipe = Recipe('Merlot', '\n PORK: \n 1 Pork Leg \n Salt Pepper \n Aluminium Foil \n Oil \n \n METHOD: \n Get a Tray, add the pork leg, rub salt and pepper, \nadd oil for the crackling, roll aluminium foil around \n the tray, bake at 180° for 2 hours.\n', '\n CHEESE BOARD: \n Camembert cheese \n Cashew Nuts \n Olive Oil \n', '\n DESSERT: \n Figs \n Brown Sugar \n Lemon Juice \n Zest \n Cream or Icecream \n')
# sangiovese_recipe = Recipe('Sangiovese', '\n SPAGHETTI BOLOGNESE: \n 500g minced meat \n 1 can tomato sauce \n 500g Spaghetti \n Parmesan cheese \n oil \n 1 onion \n 1 clove of Garlic \n salt pepper \n \n METHOD: \n Cook spaghetti pasta in salty boiling water, \n fry oil with onion and garlic, add seasoned minced meat, \n when meat is done add tomato sauce, cook for 20 minutes, \n add water if needed, mix it with the pasta, add some parmesan, enjoy.\n', '\n CHEESE BOARD: \n Mozzarella cheese \n Jam \n Brazil Nuts \n', '\n DESSERT: \n Strawberry \n Condensed Milk \n')
# chianti_recipe = Recipe('Chianti', '\n PIZZA: \n 1 Sliced Pepperoni sausage \n mozzarella cheese \n tomato sauce \n pizza base \n oregano \n \n METHOD: \n preheat oven to 180, get a tray, put the pizza base, \n spread tomato sauce, add cheese, add sliced pepperoni, \n add oregano, bake for 10 to 20 minutes.\n', '\n CHEESE BOARD: \n Parmesan cheese \n Pepperoni \n Brown Sugar \n', '\n DESSERT: \n Apples \n Brown Sugar \n Cinammon \n')
# bordeaux_recipe = Recipe('Bordeaux', '\n LAMB: \n 1 leg of lamb \n rosemary \n thyme \n olive oil \n salt and pepper \n 7spices \n \n METHOD: \n Preheat oven to 180, put the leg of lamb on a tray, add the 7 spices, \n salt and pepper, olive oil and rub, bake for 2 hours.\n', '\n CHEESE BOARD: \n Brie cheese \n Truffles \n Peanuts \n', '\n DESSERT: \n Pears \n Maple Syrup \n Macadamia Nuts \n')
# tempranillo_recipe = Recipe('Tempranillo', '\n LASAGNA: \n 500g minced meat \n 1can tomato sauce \n 500g Lasagna sheets \n Mozzarella cheese \n oil \n 1 onion \n 1 clove of Garlic \n salt pepper \n \n METHOD: \n Fry oil with onion and garlic, add seasoned minced meat, when meat \n is done add tomato sauce, cook for 20 minutes, add water if \n needed, get a tray, add a layer of sauce, cheese and lasagna sheets, \n repeat untill you reach the top of the tray, bake for 40min at 180°.\n', '\n CHEESE BOARD: \n Manchego cheese \n Jamon \n Toasted Sunflower Seeds \n', '\n DESSERT: \n Cherries \n Cream \n Honey \n')
# carmenere_recipe = Recipe('Carmenere', '\n BBQ: \n Beef \n sausages \n Charcoal \n Salt and pepper \n \n METHOD: \n light up the charcoal, season the beef with salt and pepper, \n grill the meat and sausages.\n', '\n CHEESE BOARD: \n Cheddar cheese \n Smoked Almonds \n Barbecue Sauce \n', '\n DESSERT: \n Plums \n Maple Syrup \n')
# rose_recipe = Recipe('Rose', '\n SEAFOOD: \n 500g of mixed seafood \n 1 lemon or lime \n 100g butter \n salt and pepper \n 2 cloves of garlic \n \n METHOD: \n Add butter and garlic to a frying pan, season seafood \n with salt and pepper, fry for 6 minutes.\n', '\n CHEESE BOARD: \n Feta cheese \n Anchovies \n Tzatziki Sauce \n', '\n DESSERT: \n Watermelon \n does not need anything else \n')

# recipe_list = [
#     cabernet_sauvignon_recipe,
#     pinot_noir_recipe,
#     shiraz_recipe,
#     merlot_recipe,
#     sangiovese_recipe,
#     chianti_recipe,
#     bordeaux_recipe,
#     tempranillo_recipe,
#     carmenere_recipe,
#     rose_recipe
# ]


Greetings.welcome()


def init():
    clearing.clear()
    input_message = input("What type of red wine do you have in mind (Please enter full item name)? ").capitalize()
    user_wine = Wine(input_message)
    is_wine_valid = user_wine.is_valid_wine()
    wine_validation(is_wine_valid, input_message)


def build_menu(options, return_string = True):
    menu = TerminalMenu(options)
    menu_entry_index = menu.show()
    if return_string:
        return options[menu_entry_index]
    else:
        return menu_entry_index

def reset_state():
    input_message = None
    is_wine_valid = None

def wine_validation(is_wine_valid, input_message):
    if is_wine_valid:
        clearing.clear()
        print(f"{input_message} goes well with the foods bellow, choose one for Recipe! (Use Arrow Keys ↑ ↓)")
        pair_list_iteration(input_message)
    else:
        print(f"{input_message} it is not a valid wine!")
        app_options()

def app_options():
    options = ["I want to try another wine (Use Arrow Keys ↑ ↓)", "I want to exit the app (Use Arrow Keys ↑ ↓)"]
    index = build_menu(options, False)
    if index == 0:
        init()
    else:
        Greetings.end()

def cowsay_items(cowsay_check):
    if cowsay_check == 'Pork':
        cowsay.pig('Merlot and Pork are best friends!')
    elif cowsay_check == 'Roast beef':
        cowsay.cow('You cant go wrong with Roast Beef and Cabernet!')
    elif cowsay_check == 'Duck':
        cowsay.turkey('Shiraz goes with any Poultry!')
    else:
        cowsay.trex('No wine is old enough to Pair with a T-Rex!')

def pair_list_iteration(input_message):
    for pair in wine_list:
        if input_message == pair.wine.name if pair and pair.wine else None:
            menu_options = [
                pair.main_dish.name if pair and pair.main_dish else None,
                pair.cheese.name if pair and pair.cheese else None,
                pair.fruit.name if pair and pair.fruit else None
            ]
            menu_selected = build_menu(menu_options)

            if pair.main_dish.name == menu_selected:
                print(pair.main_dish.description)
                cowsay_check = pair.main_dish.name
                cowsay_items(cowsay_check)
            elif pair.cheese.name == menu_selected:
                print(pair.cheese.description)
                cowsay.cheese('Cheese goes well with any wine!')
            else:
                print(pair.fruit.description)

            app_options()


init()














