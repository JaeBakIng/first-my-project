for dan in range(2,10) :
    print()
    print('%d단:' % dan , end="")
    for num in range(1,10) :
        print('%dX%d=%d ' % (dan,num,dan*num),end='')