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
    def totscore(self):
        for b in self.books:
            self.totalscore=self.totalscore+b.score

    def __init__(self, books, signup, perday,ratio=0,score=0):
        self.books = books
        self.signup = signup
        self.perday = perday
        self.ratio=ratio
        self.totalscore=score
        self.totscore()
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
        libraries.append(Library(bl, _lib_info[1], _lib_info[2]))
    print(libraries)
    return libraries, books
def comparator(a):
    return a.ratio
    # return a.score>b.score

def rank(libraries):
    for lib in libraries:
        lib.ratio=(lib.signup+(lib.retbooks()/lib.perday))/lib.totalscore
    libraries.sort(key=comparator)
    return libraries

def main():
    libraries, books = parser('a_example.txt')
    libraries=rank(libraries)
    for lib in libraries:
        print(lib.ratio)

if __name__ == '__main__':
    main()
