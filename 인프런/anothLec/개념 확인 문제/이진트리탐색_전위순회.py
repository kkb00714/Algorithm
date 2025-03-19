# 이진 트리 순회(DFS)에서 전위순회, 중위순회, 후위순회 출력하기
# 트리 구조
# tree = [
    #     [],
    # [2, 3],
    # [4, 5],
    # [6, 7], 
    # [], 
    # [], 
    # [], 
    # []
# ]


# 전위순회
def preorder_traversal(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        preorder_traversal(v*2) # 부모노드 * 2 => 왼쪽 자식노드 호출
        preorder_traversal(v*2+1) # 부모노드 * 2 + 1 => 오른쪽 자식노드 호출

preorder_traversal(1)