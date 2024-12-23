def checkReport(report):
    isIncreasing = False
    isDecreasing = False
    problemIndex = -1

    if len(report) <= 1:
        return problemIndex
    for j in range(len(report) - 1):

        diff = report[j + 1] - report[j]

        if abs(diff) < 1 or abs(diff) > 3: 
            problemIndex = j
            break
        if diff > 0:
            isIncreasing = True
        elif diff < 0:
            isDecreasing = True
        if isIncreasing == isDecreasing:
            problemIndex = j
            break

    return problemIndex

with open("aoc2402.txt") as file:

    count = 0
    for line in file:
        report = list(map(int, line.split(" ")))
        print(report)
        problemIndex = checkReport(report)

        print("Index:", problemIndex)
        if problemIndex < 0:
            count += 1
        else:
            for j in [problemIndex - 1, problemIndex, problemIndex + 1]:
                reportCopy = report.copy()
                reportCopy.pop(j)

                if checkReport(reportCopy) < 0:
                    count += 1
                    break


print(count)





