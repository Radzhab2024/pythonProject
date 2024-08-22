calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    list_ = [len(string), string.upper(), string.lower()]
    print(tuple(list_))
    count_calls()
def is_contains(string, list_to_search):
    string = str(string.upper())
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
    if string == list_to_search[i]:
        print(True)
    else:
        print(False)
    count_calls()
string_info('Radzhab')
string_info('Complicated')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['universal', 'pictures'])
print(calls)
#hjhj
