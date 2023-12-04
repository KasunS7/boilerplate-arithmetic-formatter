def arithmetic_arranger(problems,Solutions = False):
  if len(problems) > 5:
    return "Error: Too many problems"

  firstOperand = []
  secondOperand = []
  operator = []
  thirdline = []
  sol = []

  for i in problems:
    problem = i.split()
    firstOperand.append(problem[0])
    secondOperand.append(problem[2])
    operator.append(problem[1])

  if ("*" in operator) or ("/" in operator):
    return 'Error: Operator must be "+" or "-".'

  for i in range(len(firstOperand)):
    if not (firstOperand[i].isdigit() and secondOperand[i].isdigit()):
        return "Error: Numbers must only contain digits."

  for i in range(len(firstOperand)):
    if not (len(firstOperand[i])<5 and len(secondOperand[i])<5):
        return "Error: Numbers cannot be more than four digits"

  for i in range(len(firstOperand)):
    thirdline.append("-"*(max(len(firstOperand[i]),len(secondOperand[i]))+2))

  line1 = []
  line2 = []
  for i in range(len(firstOperand)):
    if len(firstOperand[i]) > len(secondOperand[i]):
      line1.append(" "*2 + firstOperand[i])
    else:
      line1.append(" "*(len(secondOperand[i]) - len(firstOperand[i]) + 2) + firstOperand[i])
  
  for i in range(len(secondOperand)):
        if len(secondOperand[i]) > len(firstOperand[i]):
            line2.append(operator[i] + " " + secondOperand[i])
        else:
            line2.append(operator[i] + " "*(len(firstOperand[i]) - len(secondOperand[i]) + 1) + secondOperand[i])

        
  if Solutions:
        for i in range(len(firstOperand)):
            if operator[i] == "+":
                ans = str(int(firstOperand[i]) + int(secondOperand[i]))
            else:
                ans = str(int(firstOperand[i]) - int(secondOperand[i]))

            if len(ans) > max(len(firstOperand[i]), len(secondOperand[i])):
                sol.append(" " + ans)
            else:
                sol.append(" "*(max(len(firstOperand[i]), len(secondOperand[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(thirdline) + "\n" + "    ".join(sol)
  else:
      arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(thirdline)
  return arranged_problems


    return arranged_problems
