class Solution:
    def simplifyPath(self, path: str) -> str:
        output = []
        for token in path.split("/"):
            if token == "" or token == ".":
                continue
            elif token == "..":
                if output:
                    output.pop()
            else:
                output.append(token)
        return "/" + "/".join(output)