import functools

def pythagorean_triplet():
        l = [(i, 1000-i-k, k) for i in range(1,999) for k in range(1,1000-i)]
        for elem in l:
            if (elem[0]**2) + (elem[1]**2) == (elem[2]**2):
                print (elem[0], elem[1], elem[2])
                print (elem[0] * elem[1] * elem[2])
                



        

        
pythagorean_triplet()