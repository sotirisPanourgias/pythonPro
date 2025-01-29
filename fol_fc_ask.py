def read_kb_from_file(file_path):
    
    #Διαβάζει τη βάση γνώσης KB από αρχείο.

    kb = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Αφαίρεση κενών γραμμών και σχολίων
            line = line.strip()
            if line and not line.startswith('#'):
                # Διαχωρισμός προϋποθέσεων και συμπερασμάτων
                if '->' in line:
                    premises, conclusion = line.split('->')
                    premises = tuple(p.strip() for p in premises.split('^'))
                    conclusion = conclusion.strip()
                    kb.append((premises, conclusion))
                else:
                    # Προσθήκη ατομικών προτάσεων
                    kb.append(line)
    print (kb)
    return kb

file_path = 'knowledge_base.txt'  # Το αρχείο με την βάση γνώσης
KB = read_kb_from_file(file_path)

# Εκτέλεση της fol_fc_ask



def fol_fc_ask(KB, a):
    """
    Υλοποίηση Forward Chaining για κατηγορηματική λογική.

    :param KB: Λίστα με οριστικές προτάσεις κατηγορηματικής λογικής (βάση γνώσης).
    :param a: Ερώτηση (ατομικός τύπος κατηγορηματικής λογικής).
    :return: Ενοποιητής αν το συμπέρασμα ισχύει, αλλιώς "Failure".
    """
    inferred = set()  # Σύνολο για παρακολούθηση των ήδη εξαγόμενων συμπερασμάτων
    agenda = list(KB)  # Ενεργές προτάσεις προς επεξεργασία

    while agenda:
        clause = agenda.pop(0)
        if a in clause:
            return f"Unify: {a}"
        if clause not in inferred:
            inferred.add(clause)
            # Εξαγωγή νέων συμπερασμάτων με βάση την πρόταση Horn
            for rule in KB:
                if isinstance(rule, tuple):
                    premises, conclusion = rule
                    if all(p in inferred for p in premises):
                        if conclusion not in inferred:
                            agenda.append(conclusion)
    return "Failure"

a = "Criminal(West))"
result = fol_fc_ask(KB, a)
print("Αποτέλεσμα:", result)