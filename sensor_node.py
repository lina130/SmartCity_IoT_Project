from abc import ABC, abstractmethod # [cite: 501]

# 1. 抽象数据类型 (ADT) / 抽象类 (Abstraction)
class AbstractSensor(ABC): # [cite: 502]
    # 2. 类属性 (Class Attribute) - 记录网络中总共注册了多少个传感器 [cite: 648]
    total_active_sensors = 0 
    NETWORK_SUFFIX = "@smartcity.hk" # 类似课件里的 EMAIL_SUFFIX [cite: 688]

    def __init__(self, sensor_id, location): # [cite: 136]
        self.sensor_id = sensor_id
        self.location = location
        # 3. 封装 (Encapsulation) - 隐藏内部状态，不允许外部直接修改电量 [cite: 213, 214]
        self._battery_level = 100.0  
        self._is_online = True
        
        # 每次初始化一个对象，类属性加1 [cite: 675]
        AbstractSensor.total_active_sensors += 1

    # 4. Getter 和 Setter 方法 - 规范数据访问 [cite: 203, 207]
    def get_battery_level(self):
        return self._battery_level

    def set_battery_level(self, level):
        if 0 <= level <= 100:
            self._battery_level = level
        else:
            print("Error: Battery level must be between 0 and 100.")

    # 5. 抽象方法 (Abstract Method) - 强制子类必须实现自己的信号处理逻辑 [cite: 508, 511]
    @abstractmethod
    def process_signal(self):
        pass

    # 6. 类方法 (Class Method) - 用于操作类级别的属性 [cite: 708, 709]
    @classmethod
    def get_network_status(cls):
        return f"Total active sensors on network: {cls.total_active_sensors}"

    # 7. 静态方法 (Static Method) - 逻辑上属于这个类，但不需要访问实例或类数据 [cite: 726, 764]
    # 比如：一个通用的信号转换工具函数 (A/D 转换)
    @staticmethod
    def analog_to_digital(raw_analog_voltage):
        # 模拟将 0-5V 的模拟电压信号转换为 0-1023 的数字信号
        return int((raw_analog_voltage / 5.0) * 1023)

    # 8. 魔法方法 (Magic Methods) - 自定义对象行为 [cite: 771, 772]
    def __str__(self): # 定义对象的字符串输出格式 [cite: 774, 815]
        return f"[Sensor {self.sensor_id}] at {self.location} | Battery: {self._battery_level}%"

    def __eq__(self, other): # 定义两个传感器是否"相等" (比如 ID 相同即为同一个设备) [cite: 775, 833]
        if isinstance(other, AbstractSensor):
            return self.sensor_id == other.sensor_id
        return False


# 9. 继承 (Inheritance) 和 多态 (Polymorphism) [cite: 320, 440]
class AirQualitySensor(AbstractSensor):
    def __init__(self, sensor_id, location, target_gas):
        # 调用父类的 __init__ [cite: 359]
        super().__init__(sensor_id, location)
        self.target_gas = target_gas

    # 实现父类规定的抽象方法 [cite: 531]
    def process_signal(self):
        # 多态体现：不同传感器处理信号的方式不同
        print(f"{self.sensor_id} is analyzing digital signal for {self.target_gas} concentration...")

class TrafficCamera(AbstractSensor):
    def __init__(self, sensor_id, location, resolution):
        super().__init__(sensor_id, location)
        self.resolution = resolution

    def process_signal(self):
        print(f"{self.sensor_id} is processing video feed at {self.resolution} resolution...")