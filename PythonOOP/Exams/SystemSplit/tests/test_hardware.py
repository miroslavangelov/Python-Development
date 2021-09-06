import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("H", "Heavy", 100, 100)
        self.software = ExpressSoftware("S", 10, 10)

    def test_init(self):
        self.assertEqual(self.hardware.name, "H")
        self.assertEqual(self.hardware.type, "Heavy")
        self.assertEqual(self.hardware.capacity, 100)
        self.assertEqual(self.hardware.memory, 100)
        self.assertEqual(self.hardware.software_components, [])

    def test_available_memory(self):
        self.hardware.install(self.software)
        self.assertEqual(self.hardware.available_memory, 80)

    def test_available_capacity(self):
        self.hardware.install(self.software)
        self.assertEqual(self.hardware.available_capacity, 90)

    def test_install_capacity_exception(self):
        self.hardware.capacity = 100
        self.software.capacity_consumption = 110
        with self.assertRaises(Exception) as exception:
            self.hardware.install(self.software)
        actual_message = str(exception.exception)
        expected_message = "Software cannot be installed"
        self.assertEqual(actual_message, expected_message)

    def test_install_memory_exception(self):
        self.hardware.memory = 100
        self.software.memory_consumption = 110
        with self.assertRaises(Exception) as exception:
            self.hardware.install(self.software)
        actual_message = str(exception.exception)
        expected_message = "Software cannot be installed"
        self.assertEqual(actual_message, expected_message)

    def test_install_software(self):
        self.hardware.install(self.software)
        self.assertIn(self.software, self.hardware.software_components)

    def test_uninstall_software(self):
        self.hardware.install(self.software)
        self.assertIn(self.software, self.hardware.software_components)
        self.hardware.uninstall(self.software)
        self.assertNotIn(self.software, self.hardware.software_components)