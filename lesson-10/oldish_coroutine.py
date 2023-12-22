def grep(pattern):
    print("start grep for", pattern)
    while True:
        s = yield
        print(f'Got s=[{s}]')
        if pattern in s:
            print("found!", s)
        else:
            print("no %s in %s" % (pattern, s))

g = grep("python")
next(g)
g.send("data")
g.send("deep python")
