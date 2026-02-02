"""Project-specific exceptions."""


class ConfigError(Exception):
    """Raised when the configuration file is invalid."""


class MazeError(Exception):
    """Raised when maze generation/solving fails."""
