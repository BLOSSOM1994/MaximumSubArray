#Create By Fatemeh Jokar #__# Autumn 1397

def crossingsubarray(A, low, mid, high):
    negetiveinfinity = -1000
    summ = 0
    for i in range(mid, low - 1, -1):
        summ = summ + A[i]
        if summ > negetiveinfinity:
            negetiveinfinity = summ
            leftindex = i
    left = negetiveinfinity
    negetiveinfinity = -1000
    summ = 0
    for j in range(mid+1, high+1):
        summ = summ + A[j]
        if summ > negetiveinfinity:
            negetiveinfinity = summ
            rightindex = j
    right = negetiveinfinity
    return leftindex, rightindex, left + right
#             *_*                 *_*                *_*
def findmaxarray(arrlist, low, high):

    if high == low:
        return low, high, arrlist[low]

    else:

        mid = (low+high)//2

        leftlow, lefthigh, leftsum = findmaxarray(arrlist, low, mid)
        rightlow, righthigh, rightsum = findmaxarray(arrlist, mid + 1, high)    
        crosslow, crosshigh, crosssum = crossingsubarray(arrlist, low, mid, high)         

        if leftsum >= rightsum and leftsum >= crosssum:
            return leftlow, lefthigh, leftsum
        elif rightsum >= leftsum and rightsum >= crosssum:
            return rightlow, righthigh, rightsum
        else:
            return crosslow, crosshigh, crosssum
#             *_*                 *_*                *_*
y='y'
while y=='y' or y=='Y':
    lenArr =int(input("لطفا طول ليست  خود را وارد کنيد :"))
    B=[]
    for i in range(0,lenArr):
        b=int(input(" لطفا عدد خود را وارد کنيد :"))
        B.append(b)
    num_Arr=len(B)-1
    L,H,maxi = findmaxarray(B, 0, num_Arr)
    print("\nLOW: "+str(L))
    print("HIGH: "+str(H))
    print("SUM: "+str(maxi))
    y=input("\n\n\t     اگر قصد ادامه برنامه را داريد\n\t\t\t Y يا y  \n\tو اگر قصد خروج از برنامه را داريد کليد \n\t\t\t N يا n \n\t\t      :را انتخاب نماييد \n\n\t\t\t   ")
print("\n\n\tشما با موفقيت از برنامه خارج شده ايد \n\t    @___@   موفق و پيروز باشيد   \n\n")
