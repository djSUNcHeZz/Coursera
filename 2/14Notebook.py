a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if a1 > b1:
    (a1, b1) = (b1, a1)
    if b1 > c1:
        (b1, c1) = (c1, b1)
if c1 < b1:
    (b1, c1) = (c1, b1)
    if b1 < a1:
        (a1, b1) = (b1, a1)
if a1 > b1:
    (a1, b1) = (b1, a1)
if a2 > b2:
    (a2, b2) = (b2, a2)
    if b2 > c2:
        (b2, c2) = (c2, b2)
if c2 < b2:
    (b2, c2) = (c2, b2)
    if b2 < a2:
        (a2, b2) = (b2, a2)
if a2 > b2:
    (a2, b2) = (b2, a2)
k1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
k2 = (a1 // b2) * (b1 // a2) * (c1 // c2)
k3 = (a1 // c2) * (b1 // b2) * (c1 // a2)
k4 = (a1 // a2) * (b1 // c2) * (c1 // b2)
k5 = (a1 // b2) * (b1 // c2) * (c1 // a2)
k6 = (a1 // c2) * (b1 // a2) * (c1 // b2)
print(max(k1, k2, k3, k4, k5, k6))
