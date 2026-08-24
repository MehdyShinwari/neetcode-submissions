class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for op in operations:
            match op:
                case "+":
                    rec.append(sum(rec[-2:]))
                case "D":
                    rec.append(rec[-1]*2)
                case "C":
                    rec.remove(rec[-1])
                case _:
                    rec.append(int(op))
        return sum(rec)