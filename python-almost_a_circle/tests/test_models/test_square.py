#!/usr/bin/python3
import os
import unittest

from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    @classmethod
    def tearDown(cls):
        try:
            os.remove('Square.json')
        except IOError:
            pass

    def test_right_argument(self):
        shape_1 = Square(4)
        shape_2 = Square(2, 3)
        shape_3 = Square(2, 3, 8)
        shape_4 = Square(2, 3, 7, 3)
        self.assertEqual(shape_1.x, 0)
        self.assertEqual(shape_1.y, 0)
        self.assertEqual(shape_1.size, 4)
        self.assertEqual(shape_2.x, 3)
        self.assertEqual(shape_1.y, 0)
        self.assertEqual(shape_3.x, 3)
        self.assertEqual(shape_3.y, 8)
        self.assertEqual(shape_4.id, 3)

    def test_no_position_argument_type(self):
        with self.assertRaises(TypeError) as error:
            Square()
        message = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(TypeError) as error:
            Square(4, 4, 5, 6, 1)
        message = "__init__() takes from 2 to 5 positional arguments but 6 were given"
        self.assertEqual(str(error.exception), message)

    def test_invalid_size(self):
        with self.assertRaises(TypeError) as error:
            Square("3")
        message = "width must be an integer"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(ValueError) as error:
            Square(-4)
        message = "width must be > 0"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(ValueError) as error:
            Square(0)
        message = "width must be > 0"
        self.assertEqual(str(error.exception), message)

    def test_invalid_x(self):
        with self.assertRaises(ValueError) as error:
            Square(4, -3)
        message = "x must be >= 0"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(TypeError) as error:
            Square(4, "4")
        message = "x must be an integer"
        self.assertEqual(str(error.exception), message)

    def test_invalid_y(self):
        with self.assertRaises(ValueError) as error:
            Square(4, 5, -6)
        message = "y must be >= 0"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(TypeError) as error:
            Square(4, 5, 'er')
        message = "y must be an integer"
        self.assertEqual(str(error.exception), message)

    def test_area(self):
        sqr_1 = Square(2, 2)
        self.assertEqual(sqr_1.area(), 4)

    def test_str(self):
        shape = Square(2, 2)
        shape2 = Square(4, 5, 1, 3)
        self.assertEqual(str(shape), "[Square] (1) 2/0 - 2")
        self.assertEqual(str(shape2), "[Square] (3) 5/1 - 4")

    def test_to_dictionary(self):
        shape = Square(2, 2)
        self.assertEqual(shape.to_dictionary(), {"id": 1, 'size': 2, 'x': 2, 'y': 0})

    def test_update(self):
        shape = Square(2)
        shape.update(10)
        self.assertEqual(shape.id, 10)
        shape.update(10, 30)
        self.assertEqual(shape.size, 30)
        shape.update(2, 2, 3)
        self.assertEqual(shape.x, 3)
        shape.update(2, 2, 2, 2)
        self.assertEqual(shape.y, 2)
        shape.update(**{"id": 24})
        self.assertEqual(shape.id, 24)
        shape.update(id=15, size=10)
        self.assertEqual(shape.size, 10)
        shape.update(id=15, size=10, x=14)
        self.assertEqual(shape.x, 14)
        shape.update(id=12, size=34, x=2, y=5)
        self.assertEqual(shape.y, 5)

    def test_rectangle_create(self):
        shape = Square.create(**{'id': 89})
        self.assertEqual(shape.id, 89)

        shape1 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(shape1.size, 1)
        self.assertEqual(shape1.id, 89)

        shape2 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(shape2.size, 1)
        self.assertEqual(shape2.x, 2)
        self.assertEqual(shape2.id, 89)

        shape3 = Square.create(**{'id': 89, 'size': 1,
                                  'x': 2, 'y': 3})
        self.assertEqual(shape3.size, 1)
        self.assertEqual(shape3.x, 2)
        self.assertEqual(shape3.y, 3)
        self.assertEqual(shape3.id, 89)

    def test_save_to_file(self):
        Square.save_to_file(None)
        with open('Square.json', 'r', encoding="utf-8") as f:
            text = f.read()
        self.assertEqual(text, '[]')
        shape = Square(2, 2)
        Square.save_to_file([shape])
        with open('Square.json', 'r', encoding="utf-8") as f:
            text = f.read()
            self.assertEqual(Base.from_json_string(text), [{'id': 1, 'size': 2, 'x': 2, 'y': 0}])

    def test_save_to_file_empy_list(self):
        Square.save_to_file([])
        with open('Square.json', 'r', encoding="utf-8") as f:
            text = f.read()
        self.assertEqual(text, '[]')

    def test_load_from_file_no_file(self):
        shapes = Square.load_from_file()
        self.assertEqual(shapes, [])

    def test_load_from_file_file_exists(self):
        shape = Square(2, 2)
        Square.save_to_file([shape])
        returnedShape = Square.load_from_file()
        self.assertEqual(returnedShape[0].to_dictionary(), shape.to_dictionary())
