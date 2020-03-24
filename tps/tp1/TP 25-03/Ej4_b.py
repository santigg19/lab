def histogram(items):
    print("\n")
    for i in items:
        graph = ''
        times = i
        while( times > 0 ):
            graph += '*'
            times = times - 1
        print(graph)