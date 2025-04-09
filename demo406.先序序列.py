midTree=input()
lastTree=input()
def buildTree (midTree,lastTree):
    if not midTree or not lastTree:
        return ''
    root_index=midTree.index(lastTree[-1])
    
    left_midTree=midTree[:root_index]
    left_lastTree=lastTree[:root_index]
    left=buildTree(left_midTree, left_lastTree)
    
    right_midTree=midTree[root_index+1:]
    right_lastTree=lastTree[root_index:-1]
    right=buildTree(right_midTree,right_lastTree)
    
    return lastTree[-1]+left+right

print(buildTree(midTree,lastTree))
    