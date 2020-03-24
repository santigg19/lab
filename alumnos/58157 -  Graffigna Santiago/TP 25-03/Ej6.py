def sort_list(s):
    copy = s.copy()
    #ask = input("Le gustaria ordenar de manera descendente? (y/n) ")
    ask = "y"

    if ask == "y":
        s.sort(reverse=True)
        print("\nLa lista origginal es: ", copy, "\n")
        print("Lista ordenada de manera descendente ", s, "\n")
    else:
        s.sort()
        print("Lista ordenada de manera ascendente ", s)

sort_list([ 5, 77, 8, 33, 6, 45, 38 ])