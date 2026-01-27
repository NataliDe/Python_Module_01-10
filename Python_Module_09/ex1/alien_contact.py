#!/usr/bin/env python3
"""
ex1/alien_contact.py

Exercise 1: Alien Contact Logs
Pydantic v2: Enum + model_validator(mode="after")
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, model_validator


class ContactType(str, Enum):
    """Allowed alien contact types."""
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Validated alien contact report."""

    contact_id: str = Field(
        ...,
        min_length=5,
        max_length=15,
    )
    timestamp: datetime
    location: str = Field(
        ...,
        min_length=3,
        max_length=100,
    )
    contact_type: ContactType
    signal_strength: float = Field(
        ...,
        ge=0.0,
        le=10.0,
    )
    duration_minutes: int = Field(
        ...,
        ge=1,
        le=1440,
    )
    witness_count: int = Field(
        ...,
        ge=1,
        le=100,
    )
    message_received: Optional[str] = Field(
        None,
        max_length=500,
    )
    is_verified: bool = False

    @model_validator(mode="after")
    def check_business_rules(self) -> "AlienContact":
        """Validate rules that depend on multiple fields."""
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals should include received messages"
            )

        return self


def print_contact(contact: AlienContact) -> None:
    """Print contact info in a clear format."""
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")

    if contact.message_received:
        print(f"Message: '{contact.message_received}'")
    else:
        print("Message: None")


def main() -> None:
    """Demo: show valid and invalid contact reports."""
    print("Alien Contact Log Validation")
    print("=" * 38)

    print("Valid contact report:")
    valid = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-03-10T18:45:00",
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )
    print_contact(valid)

    print()
    print("=" * 38)
    print("Expected validation error:")

    try:
        AlienContact(
            contact_id="AC_BAD_01",
            timestamp="2024-03-10",
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=4.0,
            duration_minutes=10,
            witness_count=1,  # invalid for telepathic
        )
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
