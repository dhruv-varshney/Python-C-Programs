lowercase = "aaaaaaa"
digits = "0123456789"

correct_answer =[a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]
create = correct_answer[:50]
print(create)
