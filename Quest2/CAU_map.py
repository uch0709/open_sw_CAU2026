def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def A_(graph, start, goal):
    open_list = []
    closed_set = set()
    came_from = {}         
    g_score = {start: 0}
    
    open_list.append((0, start))
    
    while open_list:
        f_val, current = open_list.pop(0)
        #도착 시
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        closed_set.add(current)
        #주변 노드 확인
        for neighbor, cost in graph.get(current, {}).items():
            if neighbor in closed_set:
                continue
            #새 비용
            new_g = g_score.get(current, float('inf')) + cost
            #새 비용이 더 좋을 때
            if new_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = new_g
                h = heuristic(neighbor, goal)
                f = new_g + h
                open_list.append((f, neighbor))
                open_list.sort(key=lambda x: x[0])
    
    return None

if __name__ == "__main__":
    # 그래프 : (층, x, y)
    # key = 현재 위치, value = {이웃 위치: 이동 비용}
    # 그래프는 지도에 따라 변경
    graph = {
        (1,0,0): {(1,5,0):5, (1,2,2):3},   # 1층 101호
        (1,5,0): {(1,0,0):5},
        (1,2,2): {(2,2,2):4, (1,0,0):3},   # 엘리베이터
        (2,2,2): {(1,2,2):4, (2,0,0):4},   # 엘리베이터
        (2,0,0): {(2,2,2):4}               # 2층 201호
    }
    
    path = A_(graph, (1,0,0), (2,0,0))
    print(path)
