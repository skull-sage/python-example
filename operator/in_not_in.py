
def checkExist(*args):
    print(f"{args[0]} in {args[1]}? {args[0] in args[1]}")

checkExist((1, 2), (1, 2, 3, 4))
checkExist({1, 2}, {1, 4, 3, 2})
checkExist((1, 2), [1, 4, 3, 2])
