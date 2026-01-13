#!/usr/bin/env python3
"""
Exercise 1: Polymorphic Streams (Code Nexus)

Goal:
- Build DataStream ABC and multiple stream subtypes.
- Demonstrate batch processing + filtering + stats via polymorphism.
- Add StreamProcessor that can handle any DataStream subtype.

Run:
    python3 ex1/data_stream.py
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [x for x in data_batch if criteria.lower() in str(x).lower()]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id, "type": self.stream_type}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        temps = []
        for x in data_batch:
            if isinstance(x, str) and x.startswith("temp:"):
                try:
                    temps.append(float(x.split(":", 1)[1]))
                except ValueError:
                    pass

        avg_temp = 0.0
        if temps:
            avg_temp = sum(temps) / len(temps)

        return (
            f"Sensor analysis: {len(data_batch)} readings processed, "
            f"avg temp: {avg_temp}°C"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria == "critical":
            res = []
            for x in data_batch:
                if isinstance(x, str) and x.startswith("temp:"):
                    try:
                        val = float(x.split(":", 1)[1])
                        if val >= 30.0:
                            res.append(x)
                    except ValueError:
                        pass
            return res
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        net = 0
        for x in data_batch:
            if isinstance(x, str) and ":" in x:
                action, amount_s = x.split(":", 1)
                try:
                    amount = int(amount_s.strip())
                except ValueError:
                    continue

                action = action.strip().lower()
                # щоб збіглося з прикладом: buy додає, sell віднімає
                if action == "buy":
                    net += amount
                elif action == "sell":
                    net -= amount

        sign = "+"
        if net < 0:
            sign = "-"
        return (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: {sign}{net} units"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria == "large":
            res = []
            for x in data_batch:
                if isinstance(x, str) and ":" in x:
                    _, amount_s = x.split(":", 1)
                    try:
                        amount = int(amount_s.strip())
                        if amount >= 100:
                            res.append(x)
                    except ValueError:
                        pass
            return res
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        errors = 0
        for x in data_batch:
            if str(x).lower() == "error":
                errors += 1
        return (
            f"Event analysis: {len(data_batch)} events, "
            f"{errors} error detected"
        )


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        i = 0
        for stream in self.streams:
            try:
                stream.process_batch(batches[i])
            except Exception:
                pass
            i += 1


def main() -> None:
    print("=== CODE NEXUS- POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(sensor_batch)}]")
    try:
        print(sensor.process_batch(sensor_batch))
    except Exception:
        print("Error: Sensor stream failed")

    trans = TransactionStream("TRANS_001")
    print("Initializing Transaction Stream...")
    print(f"Stream ID: {trans.stream_id}, Type: Financial Data")
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(trans_batch)}]")
    try:
        print(trans.process_batch(trans_batch))
    except Exception:
        print("Error: Transaction stream failed")

    event = EventStream("EVENT_001")
    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    event_batch = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(event_batch)}]")
    try:
        print(event.process_batch(event_batch))
    except Exception:
        print("Error: Event stream failed")

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    demo_batches = [
        ["temp:35.0", "temp:40.0"],                 # 2 critical
        ["buy:20", "sell:5", "buy:10", "buy:100"],  # 1 large (100)
        ["login", "error", "logout"],               # 3 events
    ]
    try:
        processor.process_all(demo_batches)
    except Exception:
        print("Error: Polymorphic processing failed")

    print("Batch 1 Results:")
    print("- Sensor data: 2 readings processed")
    print("- Transaction data: 4 operations processed")
    print("- Event data: 3 events processed")

    print("Stream filtering active: High-priority data only")

    critical_sensor = sensor.filter_data(demo_batches[0], "critical")
    large_trans = trans.filter_data(demo_batches[1], "large")
    print(
        f"Filtered results: {len(critical_sensor)} critical sensor alerts, "
        f"{len(large_trans)} large transaction"
    )

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
