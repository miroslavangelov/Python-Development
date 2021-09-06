from project.software.software import Software


class ExpressSoftware(Software):
    TYPE = "Express"
    MEMORY_CONSUMPTION_PERCENT = 2

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(
            name,
            ExpressSoftware.TYPE,
            capacity_consumption,
            int(memory_consumption * ExpressSoftware.MEMORY_CONSUMPTION_PERCENT)
        )
