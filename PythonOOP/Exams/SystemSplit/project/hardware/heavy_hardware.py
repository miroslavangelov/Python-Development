from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    TYPE = "Heavy"
    CAPACITY_PERCENT = 2
    MEMORY_PERCENT = 0.75

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(
            name,
            HeavyHardware.TYPE,
            int(capacity_consumption * HeavyHardware.CAPACITY_PERCENT),
            int(memory_consumption * HeavyHardware.MEMORY_PERCENT)
        )
