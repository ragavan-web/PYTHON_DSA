"""
Find Triplets with Sum K
In this question, you are given a list of numbers and a target number.
Your task is to find three numbers from the list that add up to the target number. 
The list is sorted in increasing order. You need to print all unique sets of three numbers that add up to the target number. 
If there are no such sets, print -1.

input:
6 10 (n,k)
1 2 3 4 5 6
output:
1 3 6
1 4 5
2 3 5

"""
def triplet(arr,n,k):
    result=[]
    
    for i in range(n):
        if i>0 and arr[i]==arr[i-1]:
            continue
        
        left=i+1 
        right=n-1 
        
        while left<right:
            total=arr[i]+arr[left]+arr[right]
            if total==k:
                result.append((arr[i],arr[left],arr[right]))
                left+=1 
                right-=1
                
                while left<right and arr[left-1]==arr[left]:
                    left+=1 
                while left<right and arr[right]==arr[right+1]:
                    
                    right-=1 
                    
            elif total<k:
                left+=1 
            else:
                right-=1 
                
    if not result:
        print(-1)
    else:
        for i in result:
            print(*i)
                
    
    
n,k=list(map(int, input().split()))
arr=list(map(int, input().split()))
triplet(arr,n,k)