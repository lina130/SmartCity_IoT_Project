import heapq

class NetworkManager:
    def __init__(self, region_name):
        self.region_name = region_name
        # 数据结构 (Data Structure)：图 (Graph)
        # 使用邻接表 (Adjacency List) 的形式存储网络拓扑
        # 格式: { 'Node_A': {'Node_B': latency1, 'Node_C': latency2}, ... }
        self.network_graph = {}
        
        # 结合 Task 1 的 OOP 概念：用一个列表专门管理注册到网络中的传感器对象
        self.registered_sensors = [] 

    def register_device(self, sensor_obj):
        """将 Task 1 中创建的传感器对象注册到网络中"""
        if sensor_obj not in self.registered_sensors:
            self.registered_sensors.append(sensor_obj)
            print(f"Success: {sensor_obj.sensor_id} is now registered to {self.region_name} Network.")

    def add_node(self, node_id):
        """在图中添加一个网络节点（比如路由器、基站或中央服务器）"""
        if node_id not in self.network_graph:
            self.network_graph[node_id] = {}

    def add_connection(self, node1, node2, latency):
        """
        在图中添加一条无向边 (Undirected Edge)
        代表两个节点之间的通信链路，latency 代表延迟（权重）
        """
        self.add_node(node1)
        self.add_node(node2)
        # 双向连接
        self.network_graph[node1][node2] = latency
        self.network_graph[node2][node1] = latency

    def find_optimal_route(self, start_node, target_node):
        """
        算法 (Algorithm)：Dijkstra 最短路径算法
        用于在复杂的嵌入式网络中，寻找数据包从起点到终点的最低延迟路由。
        """
        # 初始化所有节点的距离为无穷大
        distances = {node: float('inf') for node in self.network_graph}
        distances[start_node] = 0
        
        # 记录路径，方便最后打印出具体的路由节点
        previous_nodes = {node: None for node in self.network_graph}
        
        # 优先队列 (Priority Queue)，存储 (当前总延迟, 节点名)
        pq = [(0, start_node)]

        while pq:
            # 弹出当前延迟最小的节点
            current_distance, current_node = heapq.heappop(pq)

            # 如果找到了目标节点，可以提前结束
            if current_node == target_node:
                break

            # 如果弹出的节点距离大于已记录的最短距离，说明是冗余数据，跳过
            if current_distance > distances[current_node]:
                continue

            # 遍历当前节点的所有邻居
            for neighbor, weight in self.network_graph[current_node].items():
                distance = current_distance + weight

                # 如果发现更短的路径，则更新距离并将其推入优先队列
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # 回溯构建最短路径
        path = []
        curr = target_node
        while curr is not None:
            path.append(curr)
            curr = previous_nodes[curr]
        path.reverse() # 因为是反向回溯的，所以要反转一下列表

        # 如果起点和终点没有连通
        if distances[target_node] == float('inf'):
            return None, float('inf')

        return path, distances[target_node]