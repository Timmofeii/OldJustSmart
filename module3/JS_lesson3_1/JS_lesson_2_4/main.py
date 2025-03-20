def del_number(a,b):
    return " Del number %s to %s = %d"%(a,b,a/b)



def add_book():
    a = int(input("Кількість книг: "))
    books = []
    name='name'
    col='col'
    for i in range(a):
        name_book = input("Назва: ")
        col_b = int(input("Кількість: "))
        book = {
            name: name_book,
            col: col_b
        }
        books.append(book)
    return books


books = add_book()


def add_users():
    a = int(input("Кількість користовачів: "))
    users = []
    for i in range(a):
        name_u = input("ПІ: ")
        books = []
        user = {
            name: name_u,
            books: books
        }
        users.append(user)
    return user


users = add_users()
