class Solution:
    def intersection(self, nums1, nums2):
        return [x for x in set(nums1) if x in set(nums2)]
        # Facebook follow up, nums1 and nums2 are sorted, solve in O(1) space
        # nums1.sort()
        # nums2.sort()
        # ans = []
        # p1 = 0
        # p2 = 0
        # while p1<len(nums1) and p2<len(nums2):
        #     curr1 = nums1[p1]
        #     curr2 = nums2[p2]
        #     if curr1 == curr2:
        #         ans.append(curr1)
        #         while p1<len(nums1) and nums1[p1]==curr1:
        #             p1+=1
        #         while p2<len(nums2) and nums2[p2]==curr2:
        #             p2+=1
        #     elif curr1 > curr2:
        #         while p2<len(nums2) and curr2==nums2[p2]:
        #             p2+=1
        #     else:
        #         while p1<len(nums1) and curr1==nums1[p1]:
        #             p1+=1
        # return ans

obj = Solution()
print(obj.intersection([1,2,2,1],[2,2]))