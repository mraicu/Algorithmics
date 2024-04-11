import heapq

def KthElement(arr, k):
    heap = []
    for el in arr:
        heapq.heappush(heap, el)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def getLargestBatchSizes(arr, k):
    res = []
    n = len(arr)
    crt_arr = arr[:(k-1)] + [0] * (n-k)
    k_elem =0
    for i in range(k, n):
        crt_arr[i-1] = arr[i-1]
        if arr[i-1] < k_elem and i > 0:
            res.append(k_elem)
        else:
            k_elem = KthElement(crt_arr, k)
            res.append(k_elem)
    print(res)

getLargestBatchSizes([4,2,1,3], 2)