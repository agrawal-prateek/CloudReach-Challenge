def solution(A, K, L):
    arr,k,l,n=A,K,L,len(A)
    if k+l>n:
        return -1
    
    ks,ke,kres=0,k-1,sum(arr[:k])
    ls,le,lres=0,l-1,sum(arr[:l])
    
    try:
        curr_sum = kres 
        for i in range(k, n):
            curr_sum += arr[i] - arr[i-k]
            if curr_sum > kres:
                kres=curr_sum
                ks=i-k+1
                ke=i
    except Exception as e:
        pass
    try:            
        curr_sum = lres 
        for i in range(l, ke):
            curr_sum += arr[i] - arr[i-l]
            if curr_sum > lres:
                lres=curr_sum
                ls=i-l+1
                le=i
    except Exception as e:
        pass

    nls,nle,nlres=ke+1,ke+l,sum(arr[ke+1:ke+1+l]) 
    curr_sum=nlres
    try:
        for i in range(ke+1, n):
            curr_sum += arr[i] - arr[i-l]
            if curr_sum > nlres:
                nlres=curr_sum
                nls=i-l+1
                nle=i
    except Exception as e:
        pass

    maxsum=max(nlres,lres)+kres

    ls,le,lres=0,l-1,sum(arr[:l])
    ks,ke,kres=0,k-1,sum(arr[:k])
    
    try:
        curr_sum = lres 
        for i in range(l, n):
            curr_sum += arr[i] - arr[i-l]
            if curr_sum > lres:
                lres=curr_sum
                ls=i-l+1
                le=i
    except Exception as e:
        pass
    try:            
        curr_sum = kres 
        for i in range(k, le):
            curr_sum += arr[i] - arr[i-k]
            if curr_sum > kres:
                kres=curr_sum
                ks=i-k+1
                ke=i
    except Exception as e:
        pass

    nks,nke,nkres=le+1,le+k,sum(arr[le+1:le+1+k]) 
    curr_sum=nkres
    try:
        for i in range(le+1, n):
            curr_sum += arr[i] - arr[i-k]
            if curr_sum > nkres:
                nkres=curr_sum
                nks=i-k+1
                nke=i
    except Exception as e:
        pass

    maxsum=max(max(nkres,kres)+lres,maxsum)
    
    return maxsum
