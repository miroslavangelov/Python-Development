from project.software.software import Software


class LightSoftware(Software):
    TYPE = "Light"
    CAPACITY_CONSUMPTION_PERCENT = 1.5
    MEMORY_CONSUMPTION_PERCENT = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(
            name,
            LightSoftware.TYPE,
            int(capacity_consumption * LightSoftware.CAPACITY_CONSUMPTION_PERCENT),
            int(memory_consumption * LightSoftware.MEMORY_CONSUMPTION_PERCENT)
        )
