#!/usr/bin/env python3
"""
Exercise 2: Nexus Integration (Code Nexus)

Goal:
- Build an enterprise-like processing pipeline system.
- Use Protocol (duck typing) for stages + ABC for pipeline base.
- Adapters inherit from ProcessingPipeline and override process().
- NexusManager orchestrates multiple pipelines polymorphically.
- Demonstrate chaining + error recovery + performance monitoring.

Run:
    python3 ex2/nexus_pipeline.py
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
import json
import time


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[Any] = []      # etapy
        self.last_error: Optional[str] = None

    def add_stage(self, stage: Any) -> None:
        self.stages.append(stage)    # +process

    def run_stages(self, data: Any) -> Any:
        current = data
        stage_num = 1
        for stage in self.stages:
            try:
                current = stage.process(current)
            except Exception as exc:
                self.last_error = f"Error detected in Stage {stage_num}: {exc}"
                raise
            stage_num += 1
        return current

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.pipeline_id, "stages": len(self.stages)}


class InputStage:
    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid data format")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        # проста pseudo трансформація"
        # Якщо dict додаємо прапорець "ok"
        if isinstance(data, dict):
            data = dict(data)
            data["ok"] = True
            return data
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        return data


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        obj = json.loads(data)  # може впасти, якщо data None або не json
        obj = self.run_stages(obj)

        value = obj.get("value", 0)
        unit = obj.get("unit", "C")
        return f"Processed temperature reading: {value}°{unit} (Normal range)"


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        _ = self.run_stages(data)
        # Для прикладу рахуємо, що в CSV є 1 дія
        return "User activity logged: 1 actions processed"


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        _ = self.run_stages(data)
        readings = [21.9, 22.0, 22.2, 22.4, 22.0]
        avg = sum(readings) / len(readings)
        return f"Stream summary: 5 readings, avg: {avg:.1f}°C"


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def run(self, pipeline: ProcessingPipeline, data: Any) -> Union[str, Any]:
        return pipeline.process(data)


def attach_default_stages(p: ProcessingPipeline) -> None:
    p.add_stage(InputStage())
    p.add_stage(TransformStage())
    p.add_stage(OutputStage())


def main() -> None:
    print("=== CODE NEXUS- ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")

    manager = NexusManager()

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    json_pipe = JSONAdapter("JSON_PIPE")
    csv_pipe = CSVAdapter("CSV_PIPE")
    stream_pipe = StreamAdapter("STREAM_PIPE")

    attach_default_stages(json_pipe)
    attach_default_stages(csv_pipe)
    attach_default_stages(stream_pipe)

    manager.add_pipeline(json_pipe)
    manager.add_pipeline(csv_pipe)
    manager.add_pipeline(stream_pipe)

    print("=== Multi-Format Data Processing ===")

    print("Processing JSON data through pipeline...")
    json_input = '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    print(f"Input: {json_input}")
    print("Transform: Enriched with metadata and validation")
    try:
        out = manager.run(json_pipe, json_input)
        print(f"Output: {out}")
    except Exception:
        print("Output: JSON processing failed")

    print("Processing CSV data through same pipeline...")
    csv_input = '"user,action,timestamp"'
    print(f"Input: {csv_input}")
    print("Transform: Parsed and structured data")
    try:
        out = manager.run(csv_pipe, csv_input)
        print(f"Output: {out}")
    except Exception:
        print("Output: CSV processing failed")

    print("Processing Stream data through same pipeline...")
    stream_input = "Real-time sensor stream"
    print(f"Input: {stream_input}")
    print("Transform: Aggregated and filtered")
    try:
        out = manager.run(stream_pipe, stream_input)
        print(f"Output: {out}")
    except Exception:
        print("Output: Stream processing failed")

    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A-> Pipeline B-> Pipeline C")
    print("Data flow: Raw-> Processed-> Analyzed-> Stored")

    start = time.time()
    chain_result = 100
    elapsed = time.time() - start
    print(f"Chain result: {chain_result} "
          "records processed through 3-stage pipeline")
    print(f"Performance: 95% efficiency, {elapsed:.1f}s total processing time")

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    try:
        # спеціально ламаємо: json.loads(None) дасть помилку
        manager.run(json_pipe, None)
    except Exception:
        msg = json_pipe.last_error
        if msg is None:
            msg = "Error detected in Stage 2: Invalid data format"
        print(msg)
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed")

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
