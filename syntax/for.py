# for
myList = ["a", "b", "c", "d", "e", "f", "g"]
myTuple = ("a", "b", "c", "d", "e", "f", "g")
mySet = {"a", "b", "c", "d", "e", "f", "g"}

# for x in myList:
#     if x == "b":
#         continue  # b만 건너뛰고 출력
#     print(x)


# range (start, end, step)
# for x in range(3, 10, 2):
#     print(x)
# else:
#     print("Done!")


for i in range(2, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i * j)
    print("-" * 10)
