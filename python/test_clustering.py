import unittest
import sys
from unittest.mock import patch
  # Добавляем путь до модуля cluster.py в sys.path
from clustering import cluster  # Импортируем функцию cluster из модуля

class TestClusterFunction(unittest.TestCase):

    # Тест для проверки успешного выполнения функции cluster
    def test_cluster_successful_execution(self):
        # Подготовка данных для теста
        x = [1, 2, 3, 4, 5]
        y = [5, 4, 3, 2, 1]

        # Вызов функции cluster с тестовыми данными
        with patch('matplotlib.pyplot.savefig') as mock_savefig:
            result = cluster(x, y)

        # Проверка, что функция вернула путь к файлу
        self.assertIsInstance(result, str)

        # Проверка, что функция пыталась сохранить график
        mock_savefig.assert_called()

    # Тест для проверки работы функции cluster с пустыми данными
    def test_cluster_with_empty_data(self):
        x = []
        y = []

        # Вызов функции cluster с пустыми данными
        with patch('matplotlib.pyplot.savefig') as mock_savefig:
            result = cluster(x, y)

        # Проверка, что функция вернула путь к файлу
        self.assertIsInstance(result, str)

        # Проверка, что функция не пыталась сохранить график
        mock_savefig.assert_not_called()

    # Тест для проверки работы функции cluster с неправильным форматом данных
    def test_cluster_with_invalid_data_format(self):
        # Неправильные форматы данных (не список)
        x = "not a list"
        y = 12345

        # Вызов функции cluster с неправильными данными
        with self.assertRaises(Exception):
            cluster(x, y)

if __name__ == '__main__':
    unittest.main()
