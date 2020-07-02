from collections import Counter

def find_dup_char(input) :
    WC = Counter(input)
    j = -1
    wckesys = list(WC.keys())
    # print(wckesys)
    for i in WC.values():
        j = j + 1
        if (i>1) :
            print(wckesys[j])

if __name__ == '__main__' :
    input = 'geeksforgeeks'
    find_dup_char(input)
