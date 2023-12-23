Outcomes = []
p1 = 1
p2 = 1
p3 = 1
p4 = 1
p5 = 1
p6 = 1
    
while True:
    number = int(input("input number"))
    Outcomes.append(number)
    total = len(Outcomes)
    n1 = Outcomes.count(1)
    n2 = Outcomes.count(2)
    n3 = Outcomes.count(3)
    n4 = Outcomes.count(4)
    n5 = Outcomes.count(5)
    n6 = Outcomes.count(6)

    p1 = (total - n1) / total
    p2 = (total - n2) / total
    p3 = (total - n3) / total
    p4 = (total - n4) / total
    p5 = (total - n5) / total
    p6 = (total - n6) / total

    print("Probability of 1:", round(p1, 2))
    print("Probability of 2", round(p2, 2))
    print("Probability of 3", round(p3, 2))
    print("Probability of 4", round(p4, 2))
    print("Probability of 5", round(p5, 2))
    print("Probability of 6", round(p6, 2))


    max_p= max(p1, p2, p3, p4, p5, p6)
    max_pNum = [p1, p2, p3, p4, p5, p6].index(max_p) + 1
    print("==============================\nhighest is", max_pNum)
    print("======================================")

# (((total outcomes) - (totoal number of times n occured)) out of total outcomes) = given as a decimal
