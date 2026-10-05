# Smart City IoT Sensor & Network Resource Manager

> **Course Project:** COMP2090SEF Data Structures, Algorithms and Problem Solving
> **Task 1:** OOP-based Application Development
> **Task 2:** Self-study on Graph Data Structure & Dijkstra's Algorithm

## 📌 Problem Definition
In modern smart city infrastructure, managing thousands of embedded edge devices (e.g., air quality monitors, traffic cameras) and routing their signal data efficiently to central servers is a critical engineering challenge. This project simulates a robust IoT network resource manager. It models hardware sensors using Object-Oriented Programming (OOP) principles and dynamically calculates the lowest-latency data transmission routes using advanced graph algorithms.

## 🛠️ System Architecture (Task 1: OOP Implementation)
The system is built with a strict modular programming approach, ensuring low coupling and high cohesion. It fully utilizes Python's OOP capabilities:
* **Abstraction (ADT):** `AbstractSensor` serves as the blueprint, enforcing a standard `process_signal()` interface for all edge devices.
* **Encapsulation:** Hardware states like `battery_level` are protected via private variables and accessed strictly through getter/setter methods.
* **Inheritance & Polymorphism:** Specific devices (`TrafficCamera`, `AirQualitySensor`) inherit from the base class but implement their own unique signal processing behaviors.
* **Class & Static Methods:** Features a `@staticmethod` for Analog-to-Digital Conversion (ADC) and a `@classmethod` to track global network device registry.
* **Magic Methods:** Overloads `__eq__` to prevent MAC address/Hardware ID conflicts during network registration.

## 🧮 Data Structure & Routing Algorithm (Task 2: Self-Study)
To optimize network traffic, this project implements a topology manager that falls outside the standard course syllabus:
* **Data Structure:** **Graph (Adjacency List)**. The city's router network is modeled as a weighted graph, which is highly memory-efficient for sparse embedded networks.
* **Algorithm:** **Dijkstra's Shortest Path Algorithm**. Integrated with Python's `heapq` (Priority Queue), it calculates the optimal, lowest-latency route for data packets traveling from remote sensors to the central server in $O((V + E) \log V)$ time complexity.

## 📂 File Structure
* `sensor_node.py`: Hardware modeling, ADTs, and signal processing logic.
* `network_manager.py`: Graph data structure implementation and Dijkstra routing algorithm.
* `main.py`: Top-level environment serving as the entry point for the simulation and test cases (includes a Tkinter GUI).

## 🚀 How to Run (User Guide)
1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Run the simulation from the terminal:
   ```bash
   python main.py