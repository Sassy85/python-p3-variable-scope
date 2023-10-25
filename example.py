name = 'Haylee'

def greeting(name):
    print(f'Hello, {name}')

greeting(name)
greeting('Bella')

# JAVASCRIPT
# const evilMonster = 'Bowser'
# function princessPeachsCastle() {
#   console.log(`${evilMonster} is trying to kidnap Princess Peach!`)
# }

#PYTHON
evil_monster = 'Bowser'

def princess_peachs_castle():
    print(f'{evil_monster} is trying to kidnap Princess Peach!')

princess_peachs_castle()

#def practicing_function_scope():
#    im_trapped_in_the_function = "You can't access me outside this function!"

#print(im_trapped_in_the_function)



#change_the_world = 'change yourself'

#def change_yourself():
#    change_the_world = 'world changed'

#change_yourself()
#print(change_the_world)
#OUTPUT change yourself

change_the_world = 'change yourself'

def change_yourself():
    global change_the_world
    change_the_world = 'world changed'

change_yourself()
print(change_the_world)