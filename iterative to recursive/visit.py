from datastructure import Stack, BinarySearchTree, Node


# visita postorder
def visita(T):
    if T is not None:
        visita(T.left)
        visita(T.right)
        print(T.data)
















def iterative_preorder(T: Node):
    stackT = Stack()
    ct = T
    last = None
    while ct is not None or not stackT.isEmpty():
        while ct is not None:
            stackT.push(ct)
            ct = ct.left
        ct = stackT.top()
        if last is not ct.right and ct.right is not None:  # vengo da sinistra e il figlio e not null
            ct = ct.right
        else:
            last = ct
            print(ct.data)
            stackT.pop()
            ct = None


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(8)
    tree.insert(6)
    tree.insert(1)
    tree.insert(4)
    tree.insert(9)
    tree.insert(8)
    tree.insert(3)
    stack = Stack()
    print(stack.isEmpty())
    tree.printlevelorder(tree.root, tree.countNodes(tree.root))
    visita(tree.root)
    print('\n')
    iterative_preorder(tree.root)

# teoria del prof
# inizializzazione
# while(!terminazione)do
#    if(nuova chiamata)
#        simula la chiamata fino a quella riga
#     else si recupera dallo stack
#        if(1 chiamata)
#            effettua 2 chiamata
#         else
#            termina
# ITERATIVO
# visitaitr(T)
#     lastT = NULL
#     stack = NULL
#     currentT = T
#     //se currentT e diversa da null allora stiamo iniziando una nuova ricorsione
#     // oppure non c'e nessuna chiamata ricorsiva da riprendere
#     while(currentT != NULL or stack != NULL )do
#        if (currentT != NULL)then
#            stack.push(currentT)
#             currentT =currentT->sx
#         else
#             currentT = stack.top()
#             if(lastT != currentT ->dx and currentT!=NULL)
#                 currentT =currentT->dx
#             else
#                visita currentT
#                 lastT = currentT
#                 stack.pop()
#                 //e dobbiamo forzare terminazione
#                 ct = NULL
#         fi


#     done


# other solutions

# void postOrderIterative(struct Node * root)
# {
#     // Check for empty tree
#     if (root == NULL)
#         return

#     struct Stack * stack = createStack(MAX_SIZE);
#     do
#     {
#         // Move to leftmost node
#         while (root)
#         {
#             // Push root's right child and then root to stack.
#             if (root ->right)
#                 push(stack, root ->right);
#             push(stack, root);

#             // Set root as root's left child
#             root = root ->left;
#         }

#         // Pop an item from datastructure and set it as root
#         root = pop(stack);
#         if (root ->right && peek(stack) == root->right){
#             pop(stack);
#             push(stack, root);
#             root = root ->right;
#         }
#         else
#         {
#             printf("%d ", root ->data);
#             root = NULL;         }
#     } while (!isEmpty(stack)); }
