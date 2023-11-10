try:
    L=[11,12,13]
    S='PYTHON'
    print(S+L)
except(TypeError,ValueError,IndexError)as smg:
    print(smg)
except:
    print('UnKnown Error')