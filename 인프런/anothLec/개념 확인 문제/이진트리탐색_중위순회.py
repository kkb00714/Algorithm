# 중위순회
def inorder_traversal(v):
    if v > 7:
        return
    else:
        inorder_traversal(v*2) # 부모노드 * 2 => 왼쪽 자식노드 호출
        
        print(v, end=' ')
        
        inorder_traversal(v*2+1) # 부모노드 * 2 + 1 => 오른쪽 자식노드 호출

inorder_traversal(1)