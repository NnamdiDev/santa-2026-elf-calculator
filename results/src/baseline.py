import pandas as pd, json

def solve(starts, targets):
    prog = [["/", 0, 0, 47]]            # reg 47 = 1
    have = set(starts) | {1}
    for t in targets:
        if t in have:
            continue
        first = True
        for bit in bin(t)[3:]:          # bits after the leading 1
            if first:
                prog.append(["+", 47, 47, 46]); first = False   # 2
            else:
                prog.append(["+", 46, 46, 46])                  # double
            if bit == "1":
                prog.append(["+", 46, 47, 46])                  # add 1
        have.add(t)
    return prog

def check(starts, targets, limit, prog):
    assert len(prog) <= 4096
    reg = dict(enumerate(starts))
    seen = set(starts)
    for op, i, j, d in prog:
        a, b = reg[i], reg[j]
        if op == "+": r = a + b
        elif op == "-": assert a > b; r = a - b
        elif op == "*": r = a * b
        else: assert a % b == 0; r = a // b
        assert 0 < r <= limit
        reg[d] = r; seen.add(r)
    assert all(t in seen for t in targets)
    return len(prog)

df = pd.read_csv("/kaggle/input/competitions/santa-2026/puzzles.csv")
rows, total = [], 0
for _, row in df.iterrows():
    s = json.loads(row.starting_values)
    t = json.loads(row.targets)
    p = solve(s, t)
    total += check(s, t, row.value_limit, p)
    rows.append({"id": row.id, "program": json.dumps(p)})

pd.DataFrame(rows).to_csv("/kaggle/working/submission.csv", index=False)
print("total instructions:", total)
