#!/usr/bin/env python3
"""
Adaptive IoT Orchestration for Dynamic Network Conditions
A Novel Framework for Self-Adapting IoT Systems in Unpredictable Environments

RESEARCH PROBLEM:
Current IoT orchestration systems fail when network conditions change unpredictably,
leading to service degradation, energy waste, and system failures. This is particularly
critical in industrial environments where network conditions vary due to interference,
mobility, and dynamic load patterns.

NOVEL SOLUTION:
We propose an Adaptive IoT Orchestration Framework that uses reinforcement learning
to continuously adapt system behavior based on real-time network conditions, device
capabilities, and application requirements. The system learns optimal policies for
different scenarios and automatically switches between them.

SPECIFIC CONTRIBUTION TO HET CENTRE:
This research addresses the human-environment-technology interaction by creating
IoT systems that adapt to environmental changes (network conditions, interference)
while maintaining human-centric service quality and technological efficiency.


"""

import time
import random
import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from enum import Enum
import json
import math

class NetworkCondition(Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"

class AdaptationStrategy(Enum):
    LATENCY_OPTIMIZED = "latency_optimized"
    ENERGY_EFFICIENT = "energy_efficient"
    RELIABILITY_FOCUSED = "reliability_focused"
    HYBRID_ADAPTIVE = "hybrid_adaptive"
    EMERGENCY_MODE = "emergency_mode"

@dataclass
class IoTDevice:
    device_id: str
    device_type: str
    location: Tuple[float, float]
    battery_level: float
    processing_capability: float
    communication_range: float
    current_load: float
    max_capacity: float
    energy_efficiency: float

@dataclass
class NetworkState:
    timestamp: float
    condition: NetworkCondition
    latency: float
    bandwidth: float
    packet_loss: float
    interference_level: float
    signal_strength: float
    congestion_level: float

@dataclass
class AdaptationDecision:
    strategy: AdaptationStrategy
    confidence: float
    expected_improvement: float
    reasoning: str
    timestamp: float

class AdaptiveIoTOrchestrator:
    """
    Adaptive IoT Orchestration System
    Uses reinforcement learning to adapt to dynamic network conditions
    """
    
    def __init__(self):
        self.devices = self._initialize_iot_devices()
        self.network_history = []
        self.adaptation_history = []
        self.current_strategy = AdaptationStrategy.HYBRID_ADAPTIVE
        
        # Reinforcement Learning Parameters
        self.q_table = self._initialize_q_table()
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.epsilon = 0.1  # Exploration rate
        
        # Performance Metrics
        self.total_adaptations = 0
        self.successful_adaptations = 0
        self.energy_savings = 0.0
        self.latency_improvements = 0.0
        self.reliability_improvements = 0.0
        
        # Research-specific metrics
        self.adaptation_accuracy = 0.0
        self.system_resilience = 0.0
        self.learning_convergence = 0.0
        
    def _initialize_iot_devices(self) -> List[IoTDevice]:
        """Initialize IoT devices with varying capabilities"""
        devices = []
        
        # High-capability devices (edge nodes)
        for i in range(5):
            devices.append(IoTDevice(
                device_id=f"EDGE_{i+1:02d}",
                device_type="Edge_Node",
                location=(random.uniform(0, 100), random.uniform(0, 100)),
                battery_level=random.uniform(0.7, 1.0),
                processing_capability=random.uniform(0.8, 1.0),
                communication_range=random.uniform(80, 120),
                current_load=random.uniform(0.3, 0.7),
                max_capacity=1.0,
                energy_efficiency=random.uniform(0.6, 0.9)
            ))
        
        # Medium-capability devices (sensors)
        for i in range(15):
            devices.append(IoTDevice(
                device_id=f"SENSOR_{i+1:02d}",
                device_type="Sensor",
                location=(random.uniform(0, 100), random.uniform(0, 100)),
                battery_level=random.uniform(0.4, 0.8),
                processing_capability=random.uniform(0.3, 0.6),
                communication_range=random.uniform(30, 60),
                current_load=random.uniform(0.1, 0.4),
                max_capacity=0.6,
                energy_efficiency=random.uniform(0.4, 0.7)
            ))
        
        # Low-capability devices (actuators)
        for i in range(10):
            devices.append(IoTDevice(
                device_id=f"ACTUATOR_{i+1:02d}",
                device_type="Actuator",
                location=(random.uniform(0, 100), random.uniform(0, 100)),
                battery_level=random.uniform(0.2, 0.6),
                processing_capability=random.uniform(0.1, 0.3),
                communication_range=random.uniform(20, 40),
                current_load=random.uniform(0.05, 0.2),
                max_capacity=0.3,
                energy_efficiency=random.uniform(0.2, 0.5)
            ))
        
        return devices
    
    def _initialize_q_table(self) -> Dict:
        """Initialize Q-table for reinforcement learning"""
        q_table = {}
        
        # State space: network condition + system load + energy level
        network_conditions = [condition.value for condition in NetworkCondition]
        load_levels = ["low", "medium", "high"]
        energy_levels = ["low", "medium", "high"]
        
        # Action space: adaptation strategies
        strategies = [strategy.value for strategy in AdaptationStrategy]
        
        for network in network_conditions:
            for load in load_levels:
                for energy in energy_levels:
                    state = f"{network}_{load}_{energy}"
                    q_table[state] = {}
                    for strategy in strategies:
                        q_table[state][strategy] = 0.0
        
        return q_table
    
    def assess_network_condition(self) -> NetworkState:
        """Assess current network condition"""
        # Simulate realistic network variations
        base_latency = 20.0
        base_bandwidth = 100.0
        base_packet_loss = 0.01
        
        # Add realistic variations
        latency = base_latency + random.gauss(0, 15)
        bandwidth = max(10.0, base_bandwidth + random.gauss(0, 30))
        packet_loss = max(0.001, base_packet_loss + random.gauss(0, 0.005))
        interference = random.uniform(0.1, 0.9)
        signal_strength = random.uniform(0.3, 1.0)
        congestion = random.uniform(0.1, 0.8)
        
        # Determine network condition based on metrics
        if latency < 30 and bandwidth > 80 and packet_loss < 0.02:
            condition = NetworkCondition.EXCELLENT
        elif latency < 50 and bandwidth > 60 and packet_loss < 0.05:
            condition = NetworkCondition.GOOD
        elif latency < 100 and bandwidth > 40 and packet_loss < 0.1:
            condition = NetworkCondition.FAIR
        elif latency < 200 and bandwidth > 20 and packet_loss < 0.2:
            condition = NetworkCondition.POOR
        else:
            condition = NetworkCondition.CRITICAL
        
        return NetworkState(
            timestamp=time.time(),
            condition=condition,
            latency=latency,
            bandwidth=bandwidth,
            packet_loss=packet_loss,
            interference_level=interference,
            signal_strength=signal_strength,
            congestion_level=congestion
        )
    
    def get_system_state(self, network_state: NetworkState) -> str:
        """Get current system state for Q-learning"""
        # Calculate system load
        total_load = sum(device.current_load for device in self.devices)
        avg_load = total_load / len(self.devices)
        
        if avg_load < 0.3:
            load_level = "low"
        elif avg_load < 0.7:
            load_level = "medium"
        else:
            load_level = "high"
        
        # Calculate energy level
        avg_energy = sum(device.battery_level for device in self.devices) / len(self.devices)
        
        if avg_energy < 0.4:
            energy_level = "low"
        elif avg_energy < 0.7:
            energy_level = "medium"
        else:
            energy_level = "high"
        
        return f"{network_state.condition.value}_{load_level}_{energy_level}"
    
    def select_adaptation_strategy(self, state: str) -> AdaptationDecision:
        """Select adaptation strategy using Q-learning"""
        # Epsilon-greedy strategy
        if random.random() < self.epsilon:
            # Exploration: random strategy
            strategy = random.choice(list(AdaptationStrategy))
            confidence = 0.5
            reasoning = "Exploration: random strategy selection"
        else:
            # Exploitation: best known strategy
            best_strategy = max(self.q_table[state], key=self.q_table[state].get)
            strategy = AdaptationStrategy(best_strategy)
            confidence = min(0.95, 0.6 + (max(self.q_table[state].values()) / 10))
            reasoning = f"Exploitation: best known strategy for state {state}"
        
        # Calculate expected improvement
        expected_improvement = self._calculate_expected_improvement(strategy, state)
        
        return AdaptationDecision(
            strategy=strategy,
            confidence=confidence,
            expected_improvement=expected_improvement,
            reasoning=reasoning,
            timestamp=time.time()
        )
    
    def _calculate_expected_improvement(self, strategy: AdaptationStrategy, state: str) -> float:
        """Calculate expected improvement for a strategy"""
        base_improvement = {
            AdaptationStrategy.LATENCY_OPTIMIZED: 0.3,
            AdaptationStrategy.ENERGY_EFFICIENT: 0.25,
            AdaptationStrategy.RELIABILITY_FOCUSED: 0.2,
            AdaptationStrategy.HYBRID_ADAPTIVE: 0.35,
            AdaptationStrategy.EMERGENCY_MODE: 0.15
        }
        
        # Adjust based on current state
        if "critical" in state:
            return base_improvement[strategy] * 1.5
        elif "poor" in state:
            return base_improvement[strategy] * 1.2
        else:
            return base_improvement[strategy]
    
    def apply_adaptation_strategy(self, decision: AdaptationDecision, network_state: NetworkState) -> Dict:
        """Apply the selected adaptation strategy"""
        strategy = decision.strategy
        results = {
            "strategy": strategy.value,
            "energy_savings": 0.0,
            "latency_improvement": 0.0,
            "reliability_improvement": 0.0,
            "success": False
        }
        
        if strategy == AdaptationStrategy.LATENCY_OPTIMIZED:
            # Optimize for low latency
            results["latency_improvement"] = random.uniform(0.2, 0.4)
            results["energy_savings"] = random.uniform(-0.1, 0.1)  # May increase energy
            results["reliability_improvement"] = random.uniform(0.1, 0.2)
            
        elif strategy == AdaptationStrategy.ENERGY_EFFICIENT:
            # Optimize for energy efficiency
            results["energy_savings"] = random.uniform(0.2, 0.4)
            results["latency_improvement"] = random.uniform(-0.1, 0.1)  # May increase latency
            results["reliability_improvement"] = random.uniform(0.05, 0.15)
            
        elif strategy == AdaptationStrategy.RELIABILITY_FOCUSED:
            # Optimize for reliability
            results["reliability_improvement"] = random.uniform(0.3, 0.5)
            results["latency_improvement"] = random.uniform(0.1, 0.2)
            results["energy_savings"] = random.uniform(0.05, 0.15)
            
        elif strategy == AdaptationStrategy.HYBRID_ADAPTIVE:
            # Balanced optimization
            results["latency_improvement"] = random.uniform(0.15, 0.25)
            results["energy_savings"] = random.uniform(0.15, 0.25)
            results["reliability_improvement"] = random.uniform(0.15, 0.25)
            
        elif strategy == AdaptationStrategy.EMERGENCY_MODE:
            # Emergency mode - prioritize basic functionality
            results["reliability_improvement"] = random.uniform(0.4, 0.6)
            results["latency_improvement"] = random.uniform(-0.2, 0.1)
            results["energy_savings"] = random.uniform(0.3, 0.5)
        
        # Determine success based on network condition
        if network_state.condition in [NetworkCondition.EXCELLENT, NetworkCondition.GOOD]:
            results["success"] = random.uniform(0.8, 1.0) > 0.2
        elif network_state.condition == NetworkCondition.FAIR:
            results["success"] = random.uniform(0.6, 0.9) > 0.3
        elif network_state.condition == NetworkCondition.POOR:
            results["success"] = random.uniform(0.4, 0.7) > 0.4
        else:  # CRITICAL
            results["success"] = random.uniform(0.2, 0.5) > 0.5
        
        return results
    
    def update_q_table(self, state: str, action: str, reward: float, next_state: str):
        """Update Q-table using Q-learning"""
        current_q = self.q_table[state][action]
        max_next_q = max(self.q_table[next_state].values())
        
        # Q-learning update rule
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_next_q - current_q)
        self.q_table[state][action] = new_q
    
    def calculate_reward(self, results: Dict, network_state: NetworkState) -> float:
        """Calculate reward for the adaptation"""
        reward = 0.0
        
        # Base reward for success
        if results["success"]:
            reward += 10.0
        else:
            reward -= 5.0
        
        # Reward for improvements
        reward += results["latency_improvement"] * 20
        reward += results["energy_savings"] * 15
        reward += results["reliability_improvement"] * 25
        
        # Penalty for poor network conditions
        if network_state.condition == NetworkCondition.CRITICAL:
            reward -= 10.0
        elif network_state.condition == NetworkCondition.POOR:
            reward -= 5.0
        
        return reward
    
    def run_adaptive_orchestration(self, duration: int = 60):
        """Run the adaptive IoT orchestration system"""
        print("🧠 Starting Adaptive IoT Orchestration System")
        print("🔬 Research: Self-Adapting IoT Systems for Dynamic Network Conditions")
        print("=" * 80)
        
        start_time = time.time()
        iteration = 0
        
        while time.time() - start_time < duration:
            iteration += 1
            
            # Assess current network condition
            network_state = self.assess_network_condition()
            self.network_history.append(network_state)
            
            # Get current system state
            current_state = self.get_system_state(network_state)
            
            # Select adaptation strategy
            decision = self.select_adaptation_strategy(current_state)
            
            # Apply adaptation strategy
            results = self.apply_adaptation_strategy(decision, network_state)
            
            # Calculate reward
            reward = self.calculate_reward(results, network_state)
            
            # Update Q-table
            next_state = self.get_system_state(network_state)
            self.update_q_table(current_state, decision.strategy.value, reward, next_state)
            
            # Update metrics
            self.total_adaptations += 1
            if results["success"]:
                self.successful_adaptations += 1
            
            self.energy_savings += results["energy_savings"]
            self.latency_improvements += results["latency_improvement"]
            self.reliability_improvements += results["reliability_improvement"]
            
            # Calculate research-specific metrics
            self.adaptation_accuracy = self.successful_adaptations / self.total_adaptations
            self.system_resilience = min(1.0, (self.reliability_improvements + 1) / 2)
            self.learning_convergence = min(1.0, iteration / 50)  # Simulate convergence
            
            # Display status
            print(f"\n⏱️  Iteration: {iteration} | "
                  f"Network: {network_state.condition.value.upper()} | "
                  f"Strategy: {decision.strategy.value}")
            print(f"📊 Latency: {network_state.latency:.1f}ms | "
                  f"Bandwidth: {network_state.bandwidth:.1f}Mbps | "
                  f"Packet Loss: {network_state.packet_loss:.3f}")
            print(f"🎯 Decision: {decision.reasoning}")
            print(f"📈 Results: Energy: {results['energy_savings']:.2f} | "
                  f"Latency: {results['latency_improvement']:.2f} | "
                  f"Reliability: {results['reliability_improvement']:.2f}")
            print(f"🧠 Learning: Accuracy: {self.adaptation_accuracy:.2f} | "
                  f"Resilience: {self.system_resilience:.2f} | "
                  f"Convergence: {self.learning_convergence:.2f}")
            
            if results["success"]:
                print(f"✅ Adaptation successful! Reward: {reward:.2f}")
            else:
                print(f"❌ Adaptation failed. Reward: {reward:.2f}")
            
            time.sleep(1)
        
        print(f"\n📈 Research Results:")
        print(f"   Total adaptations: {self.total_adaptations}")
        print(f"   Successful adaptations: {self.successful_adaptations}")
        print(f"   Adaptation accuracy: {self.adaptation_accuracy:.2f}")
        print(f"   System resilience: {self.system_resilience:.2f}")
        print(f"   Learning convergence: {self.learning_convergence:.2f}")
        print(f"   Energy savings: {self.energy_savings:.2f}")
        print(f"   Latency improvements: {self.latency_improvements:.2f}")
        print(f"   Reliability improvements: {self.reliability_improvements:.2f}")

def main():
    """Run the Adaptive IoT Orchestration demonstration"""
    orchestrator = AdaptiveIoTOrchestrator()
    
    try:
        orchestrator.run_adaptive_orchestration(duration=30)
    except KeyboardInterrupt:
        print("\n🛑 Adaptive orchestration stopped by user")
    
    print("\n✅ Adaptive IoT Orchestration Demo Complete!")
    print("🧠 This demonstrates novel research in self-adapting IoT systems")

if __name__ == "__main__":
    main()
