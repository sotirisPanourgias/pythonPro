from horn import forward_chaining
file_path = 'pl.txt'
query = 'Q'
result = forward_chaining(file_path, query)

if result:
    print(f"Ο τυπος {query} αποδειχθηκε.")
else:
    print(f"ο τυπος {query} δεν αποδειχθηκε ")

