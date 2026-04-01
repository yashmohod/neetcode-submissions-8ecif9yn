class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a,b = (nums1,nums2) if len(nums1) <= len(nums2) else (nums2,nums1)
        n = len(nums1) + len(nums2)
        l,r = 0,len(a)-1
        
        while True:
            i = (l+r)//2
            j = (n//2)-i-2
            
            al = a[i] if i >=0 else -float("inf")
            ar = a[i+1] if i <len(a)-1 else float("inf")
            bl = b[j] if j >=0 else -float("inf")
            br = b[j+1] if j < len(b)-1 else float("inf")
            
            if al<=br and bl <= ar:
                if n%2 ==0:
                    return (max(al,bl) + min(ar,br))/2
                else:
                    return min(ar,br)
            elif al > br :
                r = i -1
            else:
                l = i+1

