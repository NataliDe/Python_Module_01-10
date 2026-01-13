#!/usr/bin/env python3
"""
Exercise 0: Data Processor Foundation (Code Nexus)

Goal:
- Demonstrate method overriding + subtype polymorphism via a shared interface.
- Use ABC + abstract methods.
- Provide error handling for invalid data.
- Include comprehensive type annotations.

Run:
    python3 ex0/stream_processor.py
"""


from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        for x in data:
            if not isinstance(x, (int, float)):
                return False
        return True

    def process(self, data: Any) -> str:
        nums = data
        count = len(nums)
        total = sum(nums)
        avg = 0.0
        if count > 0:
            avg = total / count
        return f"Processed {count} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        text = data
        chars = len(text)
        words = len(text.split())
        return f"Processed text: {chars} characters, {words} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return ":" in data

    def process(self, data: Any) -> str:
        left, right = data.split(":", 1)
        level = left.strip().upper()
        msg = right.strip()

        if level == "ERROR":
            return f"[ALERT] ERROR level detected: {msg}"
        return f"[INFO] INFO level detected: {msg}"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


def main() -> None:
    print("=== CODE NEXUS- DATA PROCESSOR FOUNDATION ===")

    num = NumericProcessor()
    nums = [1, 2, 3, 4, 5]
    print("Initializing Numeric Processor...")
    print(f"Processing data: {nums}")
    try:
        if num.validate(nums):
            print("Validation: Numeric data verified")
            print(num.format_output(num.process(nums)))
        else:
            print("Validation: Numeric data invalid")
    except (ValueError, TypeError):
        print("Error: Numeric processing failed")

    txt = TextProcessor()
    text = "Hello Nexus World"
    print("Initializing Text Processor...")
    print(f'Processing data: "{text}"')
    try:
        if txt.validate(text):
            print("Validation: Text data verified")
            print(txt.format_output(txt.process(text)))
        else:
            print("Validation: Text data invalid")
    except (ValueError, TypeError):
        print("Error: Text processing failed")

    logp = LogProcessor()
    log1 = "ERROR: Connection timeout"
    print("Initializing Log Processor...")
    print(f'Processing data: "{log1}"')
    try:
        if logp.validate(log1):
            print("Validation: Log entry verified")
            result = logp.process(log1)
            print(logp.format_output(result).replace("Output: ", "Output: "))
        else:
            print("Validation: Log entry invalid")
    except (ValueError, TypeError):
        print("Error: Log processing failed")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    p1 = NumericProcessor()
    p2 = TextProcessor()
    p3 = LogProcessor()

    d1 = [1, 2, 3]
    d2 = "Hello Nexus"
    d3 = "INFO: System ready"

    try:
        r1 = p1.process(d1)
        r2 = p2.process(d2)
        r3 = p3.process(d3)
        print(f"Result 1: {r1}")
        print(f"Result 2: {r2}")
        print(f"Result 3: {r3}")
    except (ValueError, TypeError):
        print("Error: Polymorphic demo failed")

    print("Foundation systems online.")
    print("Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
