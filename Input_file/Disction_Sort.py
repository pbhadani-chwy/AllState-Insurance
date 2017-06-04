# def FindbiggestNumber():
#     dis = {1: [2,3], 5: [5,2], 3: [5,1], 7: [6,4]}
#     sd = sorted(dis.items(), key = lambda x: x[1])
#     for k,v in sd:
#         print(k,v)
#
# FindbiggestNumber()
def ArrangeBiggestNum():

    T = input()
    while (T !=0):
        disc = {}
        size = input()
        z = size.split()
        for i in range(len(z)):
            l = []
            for j in z[i]:
                l.append((j))

            disc[i] = l

        sd = sorted(disc.items(),key = lambda x: x[1])
        final = []
        for k,v in sd:
            print(v)
            final.insert(0,list(v))
            # for i in final:
            #     if len(i):


        print(final)
        result = sum(final,[])
        print(result)

        print("".join(result))



ArrangeBiggestNum()
