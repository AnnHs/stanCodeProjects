"""
File: class_reviews.py
Name: Ann
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
Exit = str(-1)

def main():
    """
    user input class name and score.
    shows maximum, minimum, average of each class.
    """
    cl = str(input('Which class? ')).upper()
    if cl == Exit:
        print('No class scores were entered')
    else:
        SC001 = False
        SC101 = False
        score = int(input('Score: '))
        if cl == 'SC001':
            SC001 = True
            count001 = 1
            total001 = score
            max001 = score
            min001 = score
            avg001 = float(total001/count001)
        elif cl == 'SC101':
            SC101 = True
            count101 = 1
            total101 = score
            max101 = score
            min101 = score
            avg101 = float(total101 / count101)
        while True:
            cl = str(input('Which class? ')).upper()
            if cl == Exit:
                break
            elif cl == 'SC001':
                score = int(input('Score: '))
                if SC001 :
                    count001 += 1
                    total001 += score
                    if score > max001:
                        max001 = score
                    if score < min001:
                        min001 = score
                    avg001 = float(total001/count001)
                else:
                    SC001 = True
                    count001 = 1
                    total001 = score
                    max001 = score
                    min001 = score
                    avg001 = float(total001 / count001)
            elif cl == 'SC101':
                score = int(input('Score: '))
                if SC101 :
                    count101 += 1
                    total101 += score
                    if score > max101:
                        max101 = score
                    if score < min101:
                        min101 = score
                    avg101 = float(total101 / count101)
                else:
                    SC101 = True
                    count101 = 1
                    total101 = score
                    max101 = score
                    min101 = score
                    avg101 = float(total101 / count101)
        print('=============SC001=============')
        if SC001:
            print('Max(001): '+str(max001))
            print('Min(001): '+str(min001))
            print('Avg(001): '+str(avg001))
        else:
            print('No score for 001')
        print('=============SC101=============')
        if SC101:
            print('Max(101): '+str(max101))
            print('Min(101): '+str(min101))
            print('Avg(101): '+str(avg101))
        else:
            print('No score for 101')






# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
