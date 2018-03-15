from texttable import Texttable
from pip._vendor.distlib.compat import which


def intro():
    print "BETA VERSION\n"
    print "|<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>|"
    print "|<~~~~~~~ Sql Injection Tool ~~~~~~~>|"
    print "|<~~~~~~ Coded By: Mr.Crowley ~~~~~~>|"
    print "|<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>|\n"
    print "Instructions:"
    print "Find a vulnerable to sql-injection site"
    print "paste below the url and let the fun begin! =D"
    print "Example: http://www.somesite.com/articles.php?id=1'\n\n"


def print_data(total_data, columns, table_name):
    table = Texttable()
    c = []
    a = []
    l = len(columns)
    for index in columns:
        a.append(index)
    c.append(a)
    for i in range(0, len(total_data) / l):
        a = []
        for j in range(0, l):
            a.append(total_data[i * l + j].encode('utf_8'))
        c.append(a)
    table.add_rows(c)
    print table.draw()


def print_cols_tables(data, which):

    len_of_which = len(which)
    maxs = len_of_which

    for index in data:
        len_of_data = len(index)
        if maxs < len_of_data:
            maxs = len_of_data

    print '_' * (maxs + 2)

    if len_of_which % 2:
        left = ((maxs - 2) / 2 - len_of_which / 2 + 1)
        right = maxs - ((maxs - 2) / 2 + len_of_which / 2 + 2)

    else:
        left = ((maxs - 2) / 2 - len_of_which / 2)
        right = maxs - ((maxs - 2) / 2 + len_of_which / 2)

    print '|' + ' ' * left + which + ' ' * right + '|'
    print '-' * (maxs + 2)

    for index in data:
        print '|' + index + ' ' * (maxs - len(index)) + '|'

    print '-' * (maxs + 2)
