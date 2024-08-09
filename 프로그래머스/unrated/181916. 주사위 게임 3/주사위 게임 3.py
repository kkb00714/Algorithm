    # a, b, c, d == p (주사위 숫자) => 1111 * p 점
    # 네 개 중 3개 == p & 나머지 한 개 == q & q(p != q) 일 때 => (10 * p + q) ** 2
    # 네 개 중 2개 == p, 나머지 2개 == q & 나온 숫자들을 각각 p, q 라고 할 때 => (p + q) * abs(p-q)
    # a != b != c != d 일 때 => min(a, b, c, d)

def solution(a, b, c, d):
    
    nums = [a, b, c, d]
    counts = []
    
    for i in nums:
        count_i = nums.count(i)
        counts.append(count_i)
        # nums에 입력된 주사위 숫자를 저장함
        # 리스트에 입력된 각 숫자들의 빈도수를 counts 리스트에 추가
        
    if max(counts) == 4:
        # 네 개의 주사위가 모두 같은 숫자일 때
        return a * 1111
    
    elif max(counts) == 3:
        # 세 개의 주사위가 같은 숫자, 나머지 다른 하나가 다를 때
        p = nums[counts.index(3)]
        # p에 세 개의 같은 숫자를 할당
        q = nums[counts.index(1)]
        # q에 나머지 다른 하나의 숫자를 할당
        return (10 * p + q) ** 2
    
    elif max(counts) == 2:
        #두 개의 주사위가 같은 숫자, 나머지 두 개의 주사위도 같은 숫자일 때
        if min(counts) == 2:
            # 먼저 다른 두 개의 주사위가 같은 숫자일 때
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        
        else:
            p = nums[counts.index(2)]
            # 만약 다른 두 개의 주사위가 서로 다를 때
            return (a * b * c * d) / p**2
        
    else:
        return min(nums)
    
    