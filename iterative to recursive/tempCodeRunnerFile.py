    if T is not None:
            a = G(i)
            if(T.left is not None):
                stackT.push(T)
                stackI.push(i)
                T = T.left
                i = 2*i
            else:
                z = G(2*i)
                a = z+a+(T.data)*i
                if(T.right is not None):
                    stackT.push(T)
                    stackI.push(i)
                    stackA.push(a)
                    T = T.right
                    i = 2*i+1
                else:
                    z = G(2*i+1)+a
                    retval = 3*z
                    lastT = T
                    T = None
        else:
            T = stackT.top()
            if lastT is not T.right and T.right is not None:
                i = stackI.top()
                z = retval
                a = G(i)
                a = z+a+(T.data)*i
                stackA.push(a)
                T = T.right
                i = 2*i+1
            else:
                if T.right is not None:  # torno da destra
                    a = stackA.pop()
                    z = retval+a
                    retval = z*3
                    lastT = T
                    T = None
                    stackT.pop()
                    stackI.pop()
                else:  # torno da sinistra ma destro e nil
                    i = stackI.top()
                    z = retval
                    a = G(i)
                    a = z+a+(T.data)*i
                    z = G(2*i+1)+a
                    retval = z*3
                    lastT = T
                    T = None
                    stackT.pop()
                    i = stackI.pop()