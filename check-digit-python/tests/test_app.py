import io
import unittest
from contextlib import redirect_stdout

import app


class CheckDigitTests(unittest.TestCase):
    def test_example_values(self) -> None:
        self.assertEqual(app.calc_check_digit("1234"), "3")
        self.assertEqual(app.calc_check_digit("2345"), "4")

    def test_multiple_of_six_short_circuits_to_one(self) -> None:
        self.assertEqual(app.calc_check_digit("0000"), "1")
        self.assertEqual(app.calc_check_digit("0003"), "1")

    def test_even_value_can_become_zero_after_dividing(self) -> None:
        self.assertEqual(app.calc_check_digit("0001"), "0")

    def test_main_prints_appended_values(self) -> None:
        buffer = io.StringIO()

        with redirect_stdout(buffer):
            app.main(["1234", "2345"])

        self.assertEqual(buffer.getvalue(), "12343\n23454\n")


if __name__ == "__main__":
    unittest.main()
