# pseudo code to find the min of an bst in recursive way
def findMin(root):
    if root is None:
        return None
    if root.left is None:
        return root.data
    findMin(root.left)


def iterativeFindMin(t):
    if t is None:
        return None
    while t.left is not None:
        t = t.left
    return t.data


# def findMin(t)
#    if t =!null & & t -> sx =! null:
#         ret = min(t -> sx)
#     else ret = t
#     return ret


def iterativeFindMin(t):
    while t.left != null:
        t = t.left
    return t.data


# modo generale di farlo

# esistono due tipi di ricorsione
# quella in coda e quella in testa
