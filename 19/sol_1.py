with open('19/input.txt') as f:
    workflows, parts = f.read().split('\n\n')

def build_lambda(rule):

    rule = rule.split(',')

    for i,r in enumerate(rule[:-1]):
        cond, return_value = r.split(':')
        if return_value in ['A', 'R']: 
            rule[i] = f"'{return_value}' if {cond} else "
        else:                           
            rule[i] = f"N['{return_value}'](x,m,a,s) if {cond} else "
    
    if rule[-1] in ['A', 'R']:  
        rule[-1] = f"'{rule[-1]}'"
    else:                       
        rule[-1] = f"N['{rule[-1]}'](x,m,a,s)"

    text = 'lambda x,m,a,s : ' + ''.join(rule)
    return eval(text)


N = dict()

for w in workflows.split('\n'):
    id, rule = w[:-1].split('{')
    N[id] = build_lambda(rule)

res = 0
for p in parts.split('\n'):
    x,m,a,s = list(map(lambda x: int(x), p.split(',')))
    if N['in'](x,m,a,s) == 'A':
        res += sum([x,m,a,s])

print('part1 :', res)