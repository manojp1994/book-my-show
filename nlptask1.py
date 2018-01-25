
num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def number(Number):

    if (Number >= 1) and (Number < 19):
        return (num2words1[Number])
    elif (Number > 20) or (Number < 99):
        return (num2words2[Number])
    else:
        print("Number Out Of Range")
        caliculation()

def caliculation():
    num = eval(input("Please enter a number between 0 and 99: "))
    number(num)

caliculation()