def main():
    animals = ('bear', 'cat', 'dog', 'bunny')
    for pet in animals:
        if pet == 'dog':
            continue

        print(pet)
    # if you exit normally and transverse all the animals
    else:
        print("that is all of the animals")


main()
