class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        if (len(expression) == 0):
            return False

        dic = {"t": True, "f": False}
        opp = {True: "t", False: "f"}
        ops = ["!", "|", "&"]

        def helper(operation, bools):
            array = bools.split(",")
            val = dic[array[0]]
            if (operation == "!"):
                return not val
            for i in range(1, len(array)):
                if (operation == "&"):
                    val = val and dic[array[i]]
                elif (operation == "|"):
                    val = val or dic[array[i]]
            return val

        def solve_operation(exp):
            arr = exp.split("(")
            x = arr[-1].replace(")", "")
            val = dic[x.split(",")[0]]
            for i in range(len(arr) - 2, -1, -1):
                val = helper(arr[i], x)
                x = opp[val]
            return opp[val]

        parsed = expression
        while (len(parsed) != 1):
            right_index = len(parsed) - 1
            for i in range(len(parsed) - 1, -1, -1):
                if (parsed[i] == ')'):
                    right_index = i
                if parsed[i] in ops:
                    val = solve_operation(parsed[i:right_index + 1])
                    repl = parsed[i:right_index + 1]
                    parsed = parsed.replace(repl, val)
                    break
        return dic[parsed]
