DEBUG = False


class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score


class Library:
    def __init__(self, books, signup, perday):
        self.books = books
        self.signup = signup
        self.perday = perday


def get_int_list(data):
    return list(map(lambda x: int(x), data.split(' ')))


def get_book_list(data_list, book_db):
    ret = []
    for data in data_list:
        ret.append(book_db[data])
    return ret


def parser(input_file='a_example.txt'):
    fp = open(input_file)
    data = list(map(lambda x: get_int_list(x), fp.read().splitlines()))
    pro_info = data[0]
    book_count = pro_info[0]
    library_count = pro_info[1]
    total_days = pro_info[2]

    book_data = data[1]
    books = []
    for i in range(len(book_data)):
        books.append(Book(i, book_data[i]))

    libraries = []
    for i in range(library_count):
        lindex = (i + 1) * 2
        _lib_info = data[lindex]
        _lib_books = data[lindex + 1]
        bl = get_book_list(_lib_books, books)
        if DEBUG:
            print()
            for b in bl:
                print(b.id, b.score)
        libraries.append(Library(bl, _lib_info[1], _lib_info[2]))
    return libraries, books


def main():
    libraries, books = parser('a_example.txt')


if __name__ == '__main__':
    main()
