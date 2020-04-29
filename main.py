while 1 :
    
    def F_P(i, n, P):
        return(P*pow(1+i, n))

    def P_F(i, n , F):
        return(F*pow(1+i, -n))

    def P_A(i, n , A):
         return(A*(((pow(1+i, n))-1)/i*(pow(1+i, n))))

    def A_P(i, n, P):
         return(P*(( i * (pow(1 + i, n)/((pow(1 + i, n)) - 1)))))

    def F_A(i, n, A):
        return(A*((pow(1+i, n)-1)/i))

    def A_F(i, n, F):
        return(F*(i/(pow(1+i, n)-1)))

    def F_G(i, n, G):
        return(G*((1/i)*(((pow(1+i, n)-1)/i)-n)))

    def A_G(i, n, G):
        return(G*((1/i)- (n/((pow(1+i, n))-1))))

    def P_G(i, n, G):
       return(G*((1/i)*(1-((1+n)/pow(1+i, n)))))

    #----------------------------End of the Functions-----------------------------------------------------------------------
    print('\nWlecome to the Financial Engineering factors measurer:\n ')

    print('\nThe program includes MIT license:\n ')

    print('This program is coded by Ashkan Safari\nElectrical student at Elecetrical and Computer engineering faculty, Tabriz university')

    print('| F/A   F/P   F/G |  | P/F   P/A   P/G |  | A/F   A/P   A/G |')

    Operation= input("Pleas write the name of each factor you wanna use:\n ")

    #-----------------------------End of the Primary display commands-------------------------------------------------------

    if Operation == 'F/P':
        i = float(input('i:\n'));
        n= float(input('n:\n'));
        P = float(input('P:\n'));
        print('F= ',F_P(i, n, P));

    if Operation == 'P/F':
        i = float(input('i:\n'));
        n= float(input('n:\n'));
        F = float(input('F:\n'));
        print('P= ',P_F(i, n, F));

    if Operation == 'P/A':
        i = float(input('i:\n'));
        n= float(input('n:\n'));
        A = float(input('P:\n'));
        print('P= ',P_A(i, n, A));

    if Operation == 'A/P':
        i = float(input('i:\n'));
        n= float(input('n:\n'));
        P = float(input('P:\n'));
        print('A= ',A_P(i, n, P));

    if Operation == 'F/A':
        i = float(input('i:\n'));
        n= float(input('n:\n'));
        A = float(input('A:\n'));
        print('F= ',F_A(i, n, A));

    if Operation == 'A/F':
        i = float(input('i:\n'));
        n= float(input('n:\n'));
        F = float(input('F:\n'));
        print('A= ',A_F(i, n, F));

    if Operation == 'F/G':
        i = float(input('i:\n'));
        n= float(input('n:\n'));
        G = float(input('G:\n'));
        print('F= ',F_G(i, n, G));

    if Operation == 'A/G':
        i = float(input('i:\n'));
        n= float(input('n:\n'));
        G = float(input('G:\n'));
        print('A= ',A_G(i, n, G));

    if Operation == 'P/G':
        i = float(input('i:\n'));
        n= float(input('n:\n'));
        G= float(input('G:\n'));
        print('P= ',P_G(i, n, G));

    counter= input('Do you wanna repeat it again: \n')

    if counter== 'Y':
        continue;
    elif counter == 'N':
        break;
        
    #---------------------------------------------End of the (if) structures------------------------------------------------



