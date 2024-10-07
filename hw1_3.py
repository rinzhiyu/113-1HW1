def celsius_to_fahrenheit(celsius: float) -> float:
    """將攝氏溫度轉換為華氏溫度"""
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    # 測試轉換
    celsius_temp = float(input("請輸入攝氏溫度: "))
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"華氏溫度: {fahrenheit_temp}")

import unittest
from hw1_3 import celsius_to_fahrenheit

class TestTemperatureConversion(unittest.TestCase):
    
    def test_positive_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)  # 0°C = 32°F
        self.assertEqual(celsius_to_fahrenheit(100), 212)  # 100°C = 212°F
    
    def test_negative_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)  # -40°C = -40°F
        self.assertEqual(celsius_to_fahrenheit(-20), -4)  # -20°C = -4°F

    def test_non_integer_celsius(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(25.5), 77.9, places=1)  # 25.5°C = 77.9°F

if __name__ == "__main__":
    unittest.main()
