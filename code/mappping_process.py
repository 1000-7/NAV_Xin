f1 = open("mapping_train.txt", "w")
f2 = open("mapping_valid.txt", "w")
f3 = open("mapping_test.txt", "w")

for i in range(0, 2200000):
    if i % 100 == 0:
        f2.write(str(i) + "\n")
    elif i % 100 == 1:
        f3.write(str(i) + "\n")
    else:
        f1.write(str(i) + "\n")
