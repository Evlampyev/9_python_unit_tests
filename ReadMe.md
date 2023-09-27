### Создание Unit-тестов

Для этого используется библиотека unittest

для создания requirements.txt
используем: pip freeze > requirements.txt

Для их автоматической установки:
pip install -r requirements.txt

Метод	                    Эквивалент

.assertEqual(a, b)	    a == b

.assertTrue(x)	        bool(x) is True

.assertFalse(x)	        bool(x) is False

.assertIs(a, b)	        a is b

.assertIsNone(x)	    x is None

.assertIn(a, b)	        a in b

.assertIsInstance(a, b)	isinstance(a, b)