from functools import reduce
from .math_operations import *

def ALLSUBSETSUM(S,u):
    # print('S,u: ',S,u)
    
    n=len(S)
    
    if n==1:
        return np.array([[0    , 0 ],
                         [S[0] , 1 ]])
    elif n==0:
        return np.array([[0    , 0 ]])
    
    Ta=S[:int(n/2)]
    Tb=S[int(n/2):]
    
    return MincowskySum_2d(ALLSUBSETSUM(Ta,u),ALLSUBSETSUM(Tb,u),u)


def ALLSUBSETSUMS(S,u):
    
    def split_S_by_congruence(S,b):
        Ql=[[] for i in range(b)]
        for x in S:
            y,l=np.divmod(x,b)
            Ql[l].append(y)
        return Ql
    # print('S,u: \n',S,u)
    
    n=len(S)
        
    b=int(np.floor(np.sqrt(n*np.log(n))))
    # print('b: ',b)
    # print('u/b: ',int(u/b))
    
    Ql=split_S_by_congruence(S,b)
    # print('Ql: ',Ql)

    QSubsetSumUp2u_div_by_b=list(
        map(
            lambda ql : ALLSUBSETSUM(ql,int(u/b)),
            Ql
        )
    )
    # print('QSubsetSumUpTo_u_div_by_b:\n', QSubsetSumUp2u_div_by_b)
    
    Rl=[np.array([z*b+l*j for z,j in QSubsetSumUp2u_div_by_b[l]]) for l in range(len(QSubsetSumUp2u_div_by_b))]
    # print('Rl:\n',Rl)
    
    return reduce(
                  lambda R1,R2 : MincowskySum(R1,R2,u),
                  Rl
                  )
if __name__=='__main__':
    print(ALLSUBSETSUMS(np.array([1,4,6,7,9,10]),10))
