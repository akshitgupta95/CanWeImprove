def prefixAvg( arr):
        # code here
        runningSum=0
        for i,item in enumerate(arr):
            if i!=0:
                runningSum=arr[i-1]*(i)+item
                arr[i]=runningSum/(i+1)
        return arr

if __name__=="__main__":
    print(prefixAvg([1, 3, 4, 2, 6, 5, 8, 7]))