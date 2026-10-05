import tkinter as tk
from tkinter import ttk, scrolledtext
# 依然从你之前写的模块中导入核心类
from sensor_node import AirQualitySensor, TrafficCamera, AbstractSensor
from network_manager import NetworkManager

class SmartCityGUI:
    def __init__(self, root):
        """初始化 GUI 窗口和后台系统"""
        self.root = root
        self.root.title("Smart City IoT Resource Manager")
        self.root.geometry("650x550")
        
        # 1. 初始化后台数据 (Backend Setup)
        self.city_net = NetworkManager("Kowloon-HK Island Core")
        self.setup_backend()
        
        # 2. 构建前端界面 (Frontend UI)
        self.create_widgets()

    def setup_backend(self):
        """后台逻辑：实例化传感器并搭建网络拓扑"""
        self.sensor1 = AirQualitySensor("AQ-Central-01", "Central", "NO2")
        self.sensor2 = TrafficCamera("CAM-MongKok-01", "Mong Kok", "4K")
        
        self.city_net.register_device(self.sensor1)
        self.city_net.register_device(self.sensor2)

        # 构建图数据结构连线 (模拟城市网络)
        self.city_net.add_connection("AQ-Central-01", "Router-Admiralty", 2)
        self.city_net.add_connection("Router-Admiralty", "Router-TST", 5)
        self.city_net.add_connection("Router-TST", "CAM-MongKok-01", 3)
        self.city_net.add_connection("Router-Admiralty", "Server-HQ", 10)
        self.city_net.add_connection("Router-TST", "Server-HQ", 1)

    def create_widgets(self):
        """构建界面的各个组件"""
        # --- 标题 ---
        title_label = tk.Label(self.root, text="Smart City IoT Dashboard", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # --- 区域1：传感器状态面板 ---
        sensor_frame = tk.LabelFrame(self.root, text="Edge Devices (Sensors) Status", font=("Helvetica", 10, "bold"))
        sensor_frame.pack(fill="x", padx=15, pady=5)

        self.btn_status = tk.Button(sensor_frame, text="Initialize & Load Sensors", command=self.show_status, bg="#E1F5FE")
        self.btn_status.pack(pady=5)

        self.status_text = scrolledtext.ScrolledText(sensor_frame, height=6, width=70)
        self.status_text.pack(padx=10, pady=5)

        # --- 区域2：网络路由调度面板 (Dijkstra) ---
        route_frame = tk.LabelFrame(self.root, text="Network Routing (Dijkstra's Algorithm)", font=("Helvetica", 10, "bold"))
        route_frame.pack(fill="x", padx=15, pady=15)

        # 下拉菜单控制区
        control_frame = tk.Frame(route_frame)
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="Start Node:").grid(row=0, column=0, padx=5)
        nodes = ["AQ-Central-01", "CAM-MongKok-01", "Router-Admiralty", "Router-TST", "Server-HQ"]
        self.start_combo = ttk.Combobox(control_frame, values=nodes, state="readonly", width=18)
        self.start_combo.current(0) # 默认选中第一个
        self.start_combo.grid(row=0, column=1, padx=5)

        tk.Label(control_frame, text="Target Node:").grid(row=0, column=2, padx=5)
        self.target_combo = ttk.Combobox(control_frame, values=nodes, state="readonly", width=18)
        self.target_combo.current(4) # 默认选中最后一个 (Server-HQ)
        self.target_combo.grid(row=0, column=3, padx=5)

        self.btn_route = tk.Button(route_frame, text="Calculate Optimal Route", command=self.calculate_route, bg="#E8F5E9")
        self.btn_route.pack(pady=5)

        self.route_text = scrolledtext.ScrolledText(route_frame, height=5, width=70)
        self.route_text.pack(padx=10, pady=5)

    def show_status(self):
        """按钮点击事件：显示传感器信息"""
        self.status_text.delete(1.0, tk.END) # 清空文本框
        # 调用魔法方法 __str__ 和类方法
        self.status_text.insert(tk.END, f"[Device Loaded] {self.sensor1}\n")
        self.status_text.insert(tk.END, f"[Device Loaded] {self.sensor2}\n")
        self.status_text.insert(tk.END, "-"*40 + "\n")
        self.status_text.insert(tk.END, f"[System] {AbstractSensor.get_network_status()}\n")

    def calculate_route(self):
        """按钮点击事件：执行 Dijkstra 算法"""
        self.route_text.delete(1.0, tk.END)
        start = self.start_combo.get()
        target = self.target_combo.get()

        # 调用我们在 network_manager 里写的算法
        path, latency = self.city_net.find_optimal_route(start, target)
        
        if path:
            self.route_text.insert(tk.END, "✅ Path Found!\n")
            self.route_text.insert(tk.END, f"Optimal Route: {' ➔ '.join(path)}\n")
            self.route_text.insert(tk.END, f"Total Network Latency: {latency} ms\n")
        else:
            self.route_text.insert(tk.END, "❌ Error: No valid route found between these nodes.\n")

# Top-level 环境执行 [cite: 852, 910]
if __name__ == "__main__":
    # 初始化 Tkinter 主窗口
    root = tk.Tk()
    # 实例化我们的 GUI 应用类
    app = SmartCityGUI(root)
    # 启动界面事件循环
    root.mainloop()