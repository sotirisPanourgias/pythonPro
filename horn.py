def forward_chaining(file_path, query):
    with open(file_path, 'r') as file:
        rules = file.readlines()


    facts = set()
    r = []


    for rule in rules:
        rule = rule.strip()
        if '->' in rule:
            premise, conclusion = rule.split('->')
            premises = premise.split('^')
            r.append((premises, conclusion.strip()))
        else:
            facts.add(rule)
    newc = True
    while newc:
        newc = False
        for conditions, conclusion in r:

            if all(cond in facts for cond in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    newc = True



    if query in facts:
        return True
    else:
        return False