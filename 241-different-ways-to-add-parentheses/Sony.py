class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def add(a, b):
            return a + b
        def sub(a, b):
            return a - b
        def mul(a, b):
            return a * b
        def div(a, b):
            return a / b
        def findNextOp(input, start, end):
            for idx in xrange(start, end):
                try:
                    int(input[idx])
                except:
                    return idx
            return - 1
        def findSubResult(input, start, end, value_dict):
            if (start, end) not in value_dict:
                operator_idx_list = []
                next_sep = findNextOp(input, start + 1, end)
                if next_sep == -1:
                    value_dict[(start, end)] = [int(input[start + 1: end])]
                else:
                    sub_result_list = []
                    while next_sep != -1:
                        operator = input[next_sep]
                        if operator == '+':
                            op = add
                        elif operator == '-':
                            op = sub
                        elif operator == '*':
                            op = mul
                        else:
                            op = div
                        front_list = findSubResult(input, start, next_sep, value_dict)
                        back_list = findSubResult(input, next_sep, end, value_dict)
                        for i in front_list:
                            for j in back_list:
                                sub_result_list.append(op(i, j))
                        next_sep = findNextOp(input, next_sep + 1, end)
                    value_dict[(start, end)] = sub_result_list
            return value_dict[(start, end)]
        value_dict = dict()
        return findSubResult(input, -1, len(input), value_dict)
