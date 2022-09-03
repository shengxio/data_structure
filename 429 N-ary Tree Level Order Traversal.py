def levelOrder(self, root: 'Node') -> List[List[int]]:
    
    def breadth_first_search(node_ls):
        if node_ls is None:
            return []
        
        val_ls = []
        val_ls.append([n.val for n in node_ls if n])
        
        children_ls = []
        
        for n in node_ls:
            if n is None:
                continue
            if n.children:
                children_ls = children_ls + n.children
        if children_ls:
            val_ls = val_ls + breadth_first_search(children_ls)
        return val_ls
    
    return breadth_first_search([root]) if root else []