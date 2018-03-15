from main import inject_database


def what_to_do(what):
    a = inject_database("www", ";")
    if what:
        a.option1()
    else:
        a.option2()

    return 1
