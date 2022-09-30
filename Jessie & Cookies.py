from heapq import heapify, heappop, heappush


def cookies(k, A):
    # # Write your code here
    heapify(A)
    count = 0

    while True:
        last = heappop(A)

        if last >= k:
            return count
        if A:
            bef_last = heappop(A)
            new = last + 2 * bef_last
            heappush(A, new)
            count += 1
        else:
            return -1



# poniższe nie przechodzą testów "time eff."

# def cookies(k, A):
#     # Write your code here
#     arr = sorted(A)
#     count = 0
#     cookie = arr[::-1]
#
#     while True:
#         last = cookie.pop()
#
#         if last >= k:
#             return count
#         if cookie:
#             bef_last = cookie.pop()
#             new = last + 2 * bef_last
#             cookie.append(new)
#             cookie = sorted(cookie)[::-1]
#             count += 1
#         else:
#             return -1


# def cookies(k, A):
#     # Write your code here
#     arr = sorted(A)
#     count = 0
#     cookie = arr[::-1]
#     if cookie[-1] >= k:
#         return count
#
#     while cookie[-1] <= k:
#         new = cookie[-1] + 2 * cookie[-2]
#         cookie.pop()
#         cookie.pop()
#         cookie.append(new)
#         count += 1
#         cookie.sort()
#         cookie = cookie[::-1]
#         if cookie[-1] < k and len(cookie) < 2:
#             return -1
#
#     return count if count > 0 else -1
