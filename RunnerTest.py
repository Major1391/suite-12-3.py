import unittest
import runner

is_frozen = True


class RunnerTest(unittest.TestCase):
    @unittest.skipUnless(is_frozen, '')
    def test_walk(self):  # метод, в котором создаётся
        v_test = runner.Runner('Djo')  # объект класса Runner с произвольным именем.
        for i in range(10):  # вызовите метод walk у этого объекта 10 раз
            v_test.walk()
        self.assertEqual(v_test.distance, 50)  # методом assertEqual сравниваем distance с значением 50

    @unittest.skipUnless(is_frozen, '')
    def test_run(self):
        v_test = runner.Runner('Oleg')
        for i in range(10):
            v_test.run()
        self.assertEqual(v_test.distance, 100)

    @unittest.skipUnless(is_frozen, '')
    def test_challenge(self):
        obj1 = runner.Runner('Alisa')
        obj2 = runner.Runner('Lev')
        for i in range(10):
            obj1.walk()
            obj2.run()
        self.assertNotEqual(obj1.distance, obj2.distance)


if __name__ == 'main':
    unittest.main()
