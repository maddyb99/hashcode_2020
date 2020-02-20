DEBUG = False


class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def __str__(self):
        return "(id: {}, score: {})".format(self.id, self.score)

    def __repr__(self):
        return str(self)


class Library:
    def __init__(self, id, books, signup, perday, ratio=0):
        self.id = id
        self.books = books
        self.signup = signup
        self.perday = perday
        self.ratio = ratio
        tval = 0
        for book in self.books:
            tval += book.score
        self.score = self.perday / tval

    def retbooks(self):
        return len(self.books)

    def get_smol_books(self):
        return self.books if DEBUG else ','.join([str(item) for item in self.books[0:2]]) + '...'

    def __str__(self):
        return "LIB > signup = {}, perday = {}, books = {} <".format(self.signup, self.perday, self.get_smol_books())

    def __repr__(self):
        return str(self)


def get_int_list(data):
    return list(map(lambda x: int(x), data.split(' ')))


def get_book_list(data_list, book_db):
    ret = []
    for data in data_list:
        ret.append(book_db[data])
    return ret


def parser(input_file='a_example.txt'):
    fp = open(input_file)
    n = fp.read().splitlines()
    while "" in n:
        n.remove("")
    # print(n)
    data = list(map(lambda x: get_int_list(x), n))
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
        libraries.append(Library(i, bl, _lib_info[1], _lib_info[2]))
    return libraries, books, total_days


def comp(x):
    return x.score


def proc_lib(lib, cur, total, uniq_books):
    _cur = cur
    tval = 0
    proc_book = []
    # idx = 0
    # lib.books.sort(key=comp)
    # while _cur < total:
    #     tval += lib.books[idx]
    lib.books.sort(key=comp, reverse=True)
    for i in range(len(lib.books)):
        if _cur > total:
            break
        if lib.books[i] in uniq_books:
            continue
        if i % lib.perday == 0:
            _cur += 1
        tval += lib.books[i].score
        proc_book.append(lib.books[i])
        uniq_books.append(lib.books[i])
    return tval, proc_book


def process_libraries(libraries, gantt, total):
    uniq_books = []
    cur = 0
    r1 = len(gantt)
    print(r1)
    for lib in gantt:
        cur += lib.signup
        value, books = proc_lib(lib, cur, total, uniq_books)
        if len(books) == 0:
            continue
        print(lib.id, len(books))
        for i in range(len(books)):
            print(books[i].id, end=' ')
        if lib != gantt[len(gantt) - 1]:
            print()


def main():
    libraries, books, total_days = parser('f_libraries_of_the_world.txt')
    libraries.sort(key=comp, reverse=True)
    libscores = [x.score for x in libraries]
    gantt = []
    cur = 0
    idx = 0
    while cur < total_days:
        if idx >= len(libraries):
            break
        if cur + libscores[idx] > total_days:
            idx += 1
            continue
        gantt.append(libraries[idx])
        cur += libscores[idx]
        idx += 1
    # for lib in libraries:
    #     print(lib, lib.score)
    process_libraries(libraries, gantt, total_days)


if __name__ == '__main__':
    main()
