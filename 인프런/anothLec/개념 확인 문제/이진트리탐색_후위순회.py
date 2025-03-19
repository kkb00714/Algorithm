# 후위순회
def postorder_traversal(v):
    if v > 7:
        return
    else:
        postorder_traversal(v*2) # 부모노드 * 2 => 왼쪽 자식노드 호출
        postorder_traversal(v*2+1) # 부모노드 * 2 + 1 => 오른쪽 자식노드 호출
        print(v, end=' ')

postorder_traversal(1)