from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    TYPE = "Power"
    CAPACITY_PERCENT = 0.25
    MEMORY_PERCENT = 1.75

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(
            name,
            PowerHardware.TYPE,
            int(capacity_consumption * PowerHardware.CAPACITY_PERCENT),
            int(memory_consumption * PowerHardware.MEMORY_PERCENT)
        )
