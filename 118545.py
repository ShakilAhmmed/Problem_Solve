while True:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        a_square = a * a
        b_square = b * b
        c_square = c * c

        if ((a_square+b_square)==c_square) or ((a_square+c_square)==b_square) or ((c_square+b_square)==a_square):
            print("right") 
        else:
            print("wrong")