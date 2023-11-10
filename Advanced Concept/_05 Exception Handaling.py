try:
    L=[11,12,13]
    S='PYTHON'
    print(S+L)
except TypeError as smg:
        print(smg)
except IndexError as smg:
    print(smg)
except:
    print('Unknown Error')
        