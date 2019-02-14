import numpy as np


def horner(P, a):
    if len(P) >= 2:
        result = P[0]*a+P[1]
        # polynom degree = len(P)-1
        for i in range(2, len(P)):
            result = result*a+P[i]
        return result
    elif len(P) == 1:
        return P[0]
    else:
        print('error : polynom contains nothing')

# Test___________________________________________


P1 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 7189730]
a1 = 5.6

P2 = [2, 1, 1, 8, 99, 3576, 87, 0.1, 0, 123, 9876534517]
a2 = 3

P3 = [0, 1, 12567, 98, 89, 76381, 0, 0, 176, 0, 1987]
a3 = 0.12

P4 = [0, 1]
a4 = 36

Polynoms_to_test = [P1, P2, P3, P4]
floats_to_test = [a1, a2, a3, a4]

print("============================================================")
print("Calculs de polynomes en un reel")
print("============================================================")
for i in range(len(Polynoms_to_test)):
    horner_eval = horner(Polynoms_to_test[i], floats_to_test[i])
    np_eval = np.polyval(Polynoms_to_test[i], floats_to_test[i])
    print("------------------------------------------------------------")
    print("Coeffs : {}".format(Polynoms_to_test[i]))
    print("Float : {}".format(floats_to_test[i]))
    print("Horner : {}".format(horner_eval))
    print("Numpy : {}".format(np_eval))
    print(horner_eval == np_eval)


# End of Test_____________________________________
