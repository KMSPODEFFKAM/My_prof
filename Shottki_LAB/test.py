import calculation
import formul

num_tr = 5
f = 3
teta = 120
u = 28
p = 30


res = calculation.main(num_tr=num_tr, f=f, teta=teta, u=u, p=p)

a1 = formul.a1(teta)

for key, var in res.items():
    print(f'{key} = {var}')

