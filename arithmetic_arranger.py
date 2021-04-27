def arithmetic_arranger(problems, answer = False):

    firstLine = []
    secondLine = []
    thirdLine = []
    fourthLine = []

    # check: too many problems

    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for problem in problems:

            # split terms
            term = problem.split(" ")
            num1 = term[0]
            op = term[1]
            num2 = term[2]

            # check: operand and operator

            if num1.isdigit() == False:
                return "Error: Numbers must only contain digits."
                quit()
            elif num2.isdigit() == False:
                return "Error: Numbers must only contain digits."
                quit()
            elif op == "/" and "*":
                return "Error: Operator must be '+' or '-'."
                quit()

            # determining the width of the problem 
            
            probWidth = max(len(num1) + 2, len(num2) + 2)
            
            # check: max 4 digits

            if probWidth > 6:
                return "Error: Numbers cannot be more than four digits."
                quit()
            
            # determining the amount of spaces on each line

            firstLineSpaces = []
            secondLineSpaces = []
            

            for space in range(probWidth - (len(num1) + 2)):
                firstLineSpaces.append(" ")
            
            firstLine.extend(["  "])
            firstLine.extend(firstLineSpaces)
            firstLine.extend([num1, "    "])

            for space in range(probWidth - (len(num2) + 2)):
                secondLineSpaces.append(" ")

            secondLine.extend([op, " "])
            secondLine.extend(secondLineSpaces)
            secondLine.extend([num2, "    "])

            for space in range(probWidth):
                thirdLine.append("-")

            thirdLine.extend(["    "])

            # check: answer is True

            if answer == True:
                if op == "+":
                    sum = int(num1) + int(num2)
                elif op == "-":
                    sum = int(num1) - int(num2)
                
                fourthLineSpaces = []
                for space in range(probWidth - len(str(sum))):
                    fourthLineSpaces.append(" ")

                fourthLine.extend(fourthLineSpaces)
                fourthLine.extend([str(sum)])
            
            fourthLine.extend(["    "])
        
        # creating final lines
        line1 = "".join(firstLine).rstrip(" ")
        line2 = "".join(secondLine).rstrip(" ")
        line3 = "".join(thirdLine).rstrip(" ")
        line4 = "".join(fourthLine).rstrip(" ")

        # Final results
    if answer == True:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
        #print(arranged_problems)
        return arranged_problems

    else:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3
        #print(arranged_problems)
        return arranged_problems