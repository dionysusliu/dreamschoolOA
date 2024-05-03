
def bracketMatch(src: str) -> str:
    n = len(src)
    res = [' '] * n
    stack = []
    # match
    for i, c in enumerate(src):
        if c == '(':
            stack.append(('(', i))
        elif c == ')':
            if len(stack) == 0 or stack[-1][0] != '(':
                stack.append((')', i))
            else:
                stack.pop()
    # mark
    while len(stack) > 0:
        e = stack.pop()
        if e[0] == '(':
            res[e[1]] = 'x'
        elif e[0] == ')':
            res[e[1]] = '?'
    
    return ''.join(res)


def main():
    tests = [
        "bge)))))))))",
        "((IIII))))))",
        "()()()()(uuu",
        "))))UUUU((()"
    ]
    for t in tests:
        print(f"{t}\n{bracketMatch(t)}")

if __name__ == '__main__':
    main()