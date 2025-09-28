#!/usr/bin/env python3
"""
ResilientEdge Demo: Adaptive IoT Orchestration for Critical Infrastructure
Demonstrates dynamic policy adaptation based on network conditions and resource constraints.

This prototype showcases:
1. Real-time monitoring of network conditions
2. Dynamic policy switching (latency-optimized vs energy-efficient vs security-focused)
3. Predictive adaptation using simple ML
4. Zero-downtime reconfiguration simulation
"""

import time
import random
import json
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum
import threading
import queue

class PolicyType(Enum):
    LATENCY_OPTIMIZED = "latency_optimized"
    ENERGY_EFFICIENT = "energy_efficient"
    SECURITY_FOCUSED = "security_focused"
    DEGRADED_MODE = "degraded_mode"

@dataclass
class SystemMetrics:
    network_latency: float  # ms
    bandwidth: float        # Mbps
    cpu_usage: float       # percentage
    memory_usage: float    # percentage
    security_threat_level: int  # 1-5 scale
    energy_consumption: float   # watts
    timestamp: float

@dataclass
class PolicyConfig:
    policy_type: PolicyType
    max_latency: float
    min_bandwidth: float
    max_cpu_usage: float
    max_memory_usage: float
    security_threshold: int
    energy_budget: float
    priority_weights: Dict[str, float]

class ResilientEdgeOrchestrator:
    """
    Adaptive IoT Orchestration System for Critical Infrastructure
    """
    
    def __init__(self):
        self.current_policy = PolicyType.LATENCY_OPTIMIZED
        self.policies = self._initialize_policies()
        self.metrics_history = []
        self.adaptation_count = 0
        self.monitoring_active = True
        
        # Policy switching thresholds
        self.latency_threshold = 50.0  # ms
        self.bandwidth_threshold = 10.0  # Mbps
        self.cpu_threshold = 80.0  # percentage
        self.security_threshold = 3  # threat level
        
    def _initialize_policies(self) -> Dict[PolicyType, PolicyConfig]:
        """Initialize different automation policies"""
        return {
            PolicyType.LATENCY_OPTIMIZED: PolicyConfig(
                policy_type=PolicyType.LATENCY_OPTIMIZED,
                max_latency=20.0,
                min_bandwidth=50.0,
                max_cpu_usage=90.0,
                max_memory_usage=85.0,
                security_threshold=2,
                energy_budget=100.0,
                priority_weights={"latency": 0.6, "throughput": 0.3, "energy": 0.1}
            ),
            PolicyType.ENERGY_EFFICIENT: PolicyConfig(
                policy_type=PolicyType.ENERGY_EFFICIENT,
                max_latency=100.0,
                min_bandwidth=20.0,
                max_cpu_usage=60.0,
                max_memory_usage=70.0,
                security_threshold=2,
                energy_budget=50.0,
                priority_weights={"energy": 0.7, "latency": 0.2, "throughput": 0.1}
            ),
            PolicyType.SECURITY_FOCUSED: PolicyConfig(
                policy_type=PolicyType.SECURITY_FOCUSED,
                max_latency=150.0,
                min_bandwidth=30.0,
                max_cpu_usage=70.0,
                max_memory_usage=80.0,
                security_threshold=1,
                energy_budget=80.0,
                priority_weights={"security": 0.8, "latency": 0.1, "throughput": 0.1}
            ),
            PolicyType.DEGRADED_MODE: PolicyConfig(
                policy_type=PolicyType.DEGRADED_MODE,
                max_latency=500.0,
                min_bandwidth=5.0,
                max_cpu_usage=95.0,
                max_memory_usage=95.0,
                security_threshold=4,
                energy_budget=30.0,
                priority_weights={"availability": 0.9, "latency": 0.05, "throughput": 0.05}
            )
        }
    
    def collect_metrics(self) -> SystemMetrics:
        """Simulate real-time system metrics collection"""
        # Simulate realistic IoT system metrics with some randomness
        base_latency = 25.0
        base_bandwidth = 45.0
        base_cpu = 45.0
        base_memory = 60.0
        base_security = 1
        base_energy = 75.0
        
        # Add realistic variations and occasional anomalies
        latency = base_latency + random.gauss(0, 10)
        bandwidth = max(5.0, base_bandwidth + random.gauss(0, 15))
        cpu = max(10.0, min(95.0, base_cpu + random.gauss(0, 20)))
        memory = max(20.0, min(90.0, base_memory + random.gauss(0, 15)))
        security = max(1, min(5, base_security + random.randint(-1, 2)))
        energy = max(30.0, base_energy + random.gauss(0, 20))
        
        # Simulate network degradation scenarios
        if random.random() < 0.1:  # 10% chance of network issues
            latency *= 3
            bandwidth *= 0.3
            security = max(security, 3)
        
        # Simulate high load scenarios
        if random.random() < 0.15:  # 15% chance of high load
            cpu = min(95.0, cpu + 30)
            memory = min(90.0, memory + 25)
            energy *= 1.5
        
        return SystemMetrics(
            network_latency=latency,
            bandwidth=bandwidth,
            cpu_usage=cpu,
            memory_usage=memory,
            security_threat_level=security,
            energy_consumption=energy,
            timestamp=time.time()
        )
    
    def predict_degradation(self, metrics: SystemMetrics) -> bool:
        """Simple ML-based prediction of system degradation"""
        if len(self.metrics_history) < 3:
            return False
        
        # Simple trend analysis
        recent_latency = [m.network_latency for m in self.metrics_history[-3:]]
        recent_cpu = [m.cpu_usage for m in self.metrics_history[-3:]]
        
        # Predict if trends indicate upcoming issues
        latency_trend = (recent_latency[-1] - recent_latency[0]) / len(recent_latency)
        cpu_trend = (recent_cpu[-1] - recent_cpu[0]) / len(recent_cpu)
        
        return (latency_trend > 5.0 or cpu_trend > 10.0 or 
                metrics.security_threat_level >= 3)
    
    def select_optimal_policy(self, metrics: SystemMetrics) -> PolicyType:
        """Determine the best policy based on current conditions"""
        
        # Check for critical conditions first
        if metrics.security_threat_level >= 4:
            return PolicyType.SECURITY_FOCUSED
        
        if metrics.network_latency > 200 or metrics.bandwidth < 10:
            return PolicyType.DEGRADED_MODE
        
        # Use predictive adaptation
        if self.predict_degradation(metrics):
            if metrics.energy_consumption > 90:
                return PolicyType.ENERGY_EFFICIENT
            elif metrics.security_threat_level >= 2:
                return PolicyType.SECURITY_FOCUSED
            else:
                return PolicyType.DEGRADED_MODE
        
        # Normal operation - choose based on current conditions
        if metrics.energy_consumption > 80:
            return PolicyType.ENERGY_EFFICIENT
        elif metrics.network_latency > 50:
            return PolicyType.LATENCY_OPTIMIZED
        else:
            return PolicyType.LATENCY_OPTIMIZED
    
    def adapt_policy(self, new_policy: PolicyType) -> bool:
        """Perform zero-downtime policy adaptation"""
        if new_policy == self.current_policy:
            return False
        
        print(f"\n🔄 ADAPTING POLICY: {self.current_policy.value} → {new_policy.value}")
        
        # Simulate WebAssembly hot-swapping
        print("  📦 Loading new policy configuration...")
        time.sleep(0.1)  # Simulate loading time
        
        print("  🔄 Hot-swapping runtime components...")
        time.sleep(0.2)  # Simulate swap time
        
        print("  ✅ Policy adaptation complete!")
        
        self.current_policy = new_policy
        self.adaptation_count += 1
        return True
    
    def execute_automation_task(self, metrics: SystemMetrics) -> Dict:
        """Execute automation task based on current policy"""
        policy = self.policies[self.current_policy]
        
        # Simulate task execution with policy-specific behavior
        if self.current_policy == PolicyType.LATENCY_OPTIMIZED:
            # Prioritize speed over efficiency
            execution_time = 0.05 + random.gauss(0, 0.01)
            energy_used = metrics.energy_consumption * 1.2
            result = {"status": "success", "latency": execution_time, "energy": energy_used}
            
        elif self.current_policy == PolicyType.ENERGY_EFFICIENT:
            # Prioritize energy efficiency
            execution_time = 0.15 + random.gauss(0, 0.02)
            energy_used = metrics.energy_consumption * 0.7
            result = {"status": "success", "latency": execution_time, "energy": energy_used}
            
        elif self.current_policy == PolicyType.SECURITY_FOCUSED:
            # Add security overhead
            execution_time = 0.25 + random.gauss(0, 0.03)
            energy_used = metrics.energy_consumption * 1.1
            result = {"status": "success", "latency": execution_time, "energy": energy_used, "security_checks": 5}
            
        else:  # DEGRADED_MODE
            # Minimal functionality
            execution_time = 0.5 + random.gauss(0, 0.1)
            energy_used = metrics.energy_consumption * 0.5
            result = {"status": "degraded", "latency": execution_time, "energy": energy_used}
        
        return result
    
    def run_monitoring_loop(self, duration: int = 60):
        """Run the adaptive orchestration system"""
        print("🚀 Starting ResilientEdge Adaptive IoT Orchestration System")
        print("=" * 60)
        
        start_time = time.time()
        task_count = 0
        
        while time.time() - start_time < duration and self.monitoring_active:
            # Collect current metrics
            metrics = self.collect_metrics()
            self.metrics_history.append(metrics)
            
            # Keep only recent history
            if len(self.metrics_history) > 10:
                self.metrics_history.pop(0)
            
            # Determine optimal policy
            optimal_policy = self.select_optimal_policy(metrics)
            
            # Adapt if necessary
            adapted = self.adapt_policy(optimal_policy)
            
            # Execute automation task
            task_result = self.execute_automation_task(metrics)
            task_count += 1
            
            # Display status
            print(f"\n⏱️  Time: {time.time() - start_time:.1f}s | "
                  f"Policy: {self.current_policy.value} | "
                  f"Tasks: {task_count}")
            print(f"📊 Latency: {metrics.network_latency:.1f}ms | "
                  f"Bandwidth: {metrics.bandwidth:.1f}Mbps | "
                  f"CPU: {metrics.cpu_usage:.1f}% | "
                  f"Security: {metrics.security_threat_level}")
            print(f"⚡ Energy: {metrics.energy_consumption:.1f}W | "
                  f"Task Result: {task_result['status']} | "
                  f"Task Latency: {task_result['latency']:.3f}s")
            
            if adapted:
                print(f"🎯 Adaptation #{self.adaptation_count} completed!")
            
            time.sleep(2)  # Monitoring interval
        
        print(f"\n📈 Final Statistics:")
        print(f"   Total adaptations: {self.adaptation_count}")
        print(f"   Total tasks executed: {task_count}")
        print(f"   Average task latency: {sum(r['latency'] for r in [self.execute_automation_task(self.metrics_history[-1]) for _ in range(5)])/5:.3f}s")

def main():
    """Run the ResilientEdge demonstration"""
    orchestrator = ResilientEdgeOrchestrator()
    
    try:
        orchestrator.run_monitoring_loop(duration=30)  # Run for 30 seconds
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user")
        orchestrator.monitoring_active = False
    
    print("\n✅ ResilientEdge Demo Complete!")

if __name__ == "__main__":
    main()
