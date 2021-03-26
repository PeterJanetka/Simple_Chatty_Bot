A = int(input())
B = int(input())
H = int(input())

# H >= A and H <= B: "Normal"
# H < A: “Deficiency”
# H > B: “Excess”
# Writing it down helps LOL


if H >= A:
    if H > B:
        print("Excess")
    else:
        print("Normal")
else:
    print("Deficiency")
