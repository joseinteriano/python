
        else:
            print "use %d times" % i
            return mid
    return -1

if __name__ == "__main__":
    l=[1,4,5,6,7,8,9,44,333,2233]
    print l
    print BinarySearch(l,4)
    print BinarySearch(l,44)
    print BinarySearch(l,8)
    print BinarySearch(l,2233)
    print BinarySearch(l,77)
    
