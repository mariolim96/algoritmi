def algo(A: list, p: int, r: int):
#     ret = 0
#     if p <= r:
#         if p == r:
#             ret = A[p]
#         else:
#             q1 = (p + 2*r) // 3
#             ret = algo(A, p, q1)
#             q2 = (2*p + r) // 3
#             ret = ret+algo(A, q1+1, q2)
#             ret = ret+algo(A, q2+1, r)
#     return ret