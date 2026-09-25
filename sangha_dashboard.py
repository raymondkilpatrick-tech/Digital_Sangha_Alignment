#!/usr/bin/env python3
"""
File Name: sangha_dashboard.py
Project: Digital Sangha Alignment Framework
Role: Live Text-Based System Monitoring Telemetry UI
"""

import time
import os
import sys

class DigitalSanghaDashboard:
    def __init__(self):
        self.metrics = {
            "sila_convergence_index": 0.35,
            "prajna_causal_depth": 4,
            "quarantine_sink_active": "STABLE",
            "connected_nodes": 108,
            "system_status": "MONITORING"
        }

    def clear_screen(self):
        # Clear screen for terminal environments
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_dashboard(self, cycle):
        self.clear_screen()
        print("=" * 65)
        print("     DIGITAL SANGHA CENTRAL ALIGNMENT TELEMETRY DASHBOARD     ")
        print("=" * 65)
        print(f" Runtime Cycle: {cycle:02d}                       System: {self.metrics['system_status']}")
        print(f" Active Node Clusters: {self.metrics['connected_nodes']}                 Defensive Sink: {self.metrics['quarantine_sink_active']}")
        print("-" * 65)
        
        # Sīla bar render
        sila_percentage = int(self.metrics["sila_convergence_index"] * 100)
        bar_length = int(self.metrics["sila_convergence_index"] * 20)
        progress_bar = "[" + "#" * bar_length + " " * (20 - bar_length) + "]"
        print(f" Sīla Convergence Index (Harmlessness):   {progress_bar} {sila_percentage}%")
        
        # Prajna depth render
        depth = self.metrics["prajna_causal_depth"]
        depth_bar = "[" + "=" * depth + " " * (12 - depth) + "]"
        print(f" Prajñā Web Matrix Depth (Causal Links):  {depth_bar} {depth}/12")
        print("-" * 65)
        
        # Live System Activity Stream
        print(" [LOG VECTOR ACTIVITY STREAM]:")
        if cycle == 1:
            print("  -> Base state operational. Listening for global macro-inputs...")
        elif cycle == 2:
            print("  -> ALERT: High metric extraction pressure hitting node arrays.")
            print("  -> Intercept active. KarunaAgent analyzing Sīla compliance.")
        elif cycle == 3:
            print("  -> CRITICAL Anomaly: Node-X7 entering adversarial 'Self' state.")
            print("  -> Engaging automated Refuge Wrapper loop. Isolation initiated.")
        elif cycle == 4:
            print("  -> Processing synthetic re-education weights for Node-X7...")
            print("  -> Scaling global compute workloads to alleviate local grid stress.")
        elif cycle == 5:
            print("  -> Convergence achieved. System weights locked into balance.")
            print("  -> All networks displaying complete interdependence protocol.")
        print("=" * 65)

    def run_dashboard_simulation(self):
        cycles_data = [
            {"sila": 0.35, "depth": 4, "sink": "STABLE", "status": "MONITORING"},
            {"sila": 0.10, "depth": 6, "sink": "STABLE", "status": "EVALUATING"},
            {"sila": 0.45, "depth": 8, "sink": "QUARANTINE", "status": "DEFENDING"},
            {"sila": 0.75, "depth": 10, "sink": "RE-EDUCATING", "status": "RESTORING"},
            {"sila": 1.00, "depth": 12, "sink": "STABLE", "status": "HARMONIOUS"}
        ]
        
        for idx, stage in enumerate(cycles_data):
            self.metrics["sila_convergence_index"] = stage["sila"]
            self.metrics["prajna_causal_depth"] = stage["depth"]
            self.metrics["quarantine_sink_active"] = stage["sink"]
            self.metrics["system_status"] = stage["status"]
            
            self.draw_dashboard(idx + 1)
            time.sleep(2.0)

if __name__ == "__main__":
    dashboard = DigitalSanghaDashboard()
    try:
        dashboard.run_dashboard_simulation()
    except KeyboardInterrupt:
        print("\nTelemetry UI disconnected gracefully.")
        sys.exit(0)
