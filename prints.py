from texttable import Texttable


def intro():
    print("BETA VERSION\n")
    print("|<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>|")
    print("|<~~~~~~~ Sql Injection Tool ~~~~~~~>|")
    print("|<~~~~~~ Coded By: Mr.Crowley ~~~~~~>|")
    print("|<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>|\n")
    print("Instructions:")
    print("Find a vulnerable to sql-injection site")
    print("paste below the url and let the fun begin! =D")
    print("Example: http://www.somesite.com/articles.php?id=1'\n\n")


def print_data(total_data, columns):
    table = Texttable()
    c = []
    a = []
    length = len(columns)
    for index in columns:
        a.append(index)
    c.append(a)
    k = int(len(total_data) / length)
    for i in range(0, k):
        a = []
        for j in range(0, length):
            a.append(total_data[i * length + j].encode('utf_8'))
        c.append(a)
    table.add_rows(c)
    print(table.draw())
