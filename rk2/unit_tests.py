import unittest
import rk2

class TestTaskFunctions(unittest.TestCase):

    def test_task1(self):
        in_data = (('RAM', 75, 'Kingston'), ('memory card', 40, 'Kingston'), ('CPU', 125, 'AMD'), ('motherboard', 200, 'Asus'), ('PSU', 66, 'Corsair'), ('graphics card', 374, 'Nvidia'))
        correct_out = [('CPU', 125, 'AMD'), ('PSU', 66, 'Corsair'), ('RAM', 75, 'Kingston'), ('graphics card', 374, 'Nvidia'), ('memory card', 40, 'Kingston'), ('motherboard', 200, 'Asus')]
        out = rk2.first_task(in_data)
        self.assertEqual(out, correct_out)

    def test_task2(self):
        in_data = (('RAM', 75, 'Kingston'), ('memory card', 40, 'Kingston'), ('CPU', 125, 'AMD'), ('motherboard', 200, 'Asus'), ('PSU', 66, 'Corsair'), ('graphics card', 374, 'Nvidia'))
        correct_out = [('Kingston', 2), ('AMD', 1), ('Asus', 1), ('Corsair', 1), ('Nvidia', 1)]
        out = rk2.second_task(in_data)
        self.assertEqual(out, correct_out)

    def test_task3(self):
        in_data = (('memory card', 40, 'AMD'), ('CPU', 125, 'AMD'), ('motherboard', 200, 'Asus'), ('graphics card', 374, 'Asus'), ('RAM', 75, 'Corsair'))
        correct_out = [('memory card', 'AMD'), ('CPU', 'AMD'), ('RAM', 'Corsair')]
        out = rk2.third_task(in_data, 200)
        self.assertEqual(out, correct_out)


if __name__ == '__main__':
    unittest.main()