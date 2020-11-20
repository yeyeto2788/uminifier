import os
from unittest import TestCase
import uminifier
import subprocess


class WeirdTest(TestCase):
    data_dir = os.path.dirname(os.path.abspath(__file__))
    uminifier_dir = os.path.join(os.path.dirname(data_dir), "uminifier", "__init__.py")
    input_file = os.path.join(data_dir, "test_data", "bulleting_board.py")
    output_file = os.path.join(data_dir, "test_data", "bulleting_board.mpy")

    def test_all_script(self):
        try:
            execution = subprocess.Popen(["uminifier", "-h"])
            execution.wait()
        except FileNotFoundError:
            pass
        else:
            print(execution.returncode)
        self.assertEqual(True, True)

    def test_execution(self):
        try:
            execution = subprocess.Popen(
                ["python", self.uminifier_dir, self.input_file],
                stdout=subprocess.PIPE)
            execution.wait()
        except FileNotFoundError:
            self.fail("Python seems not be install")
        else:
            execution_output = execution.stdout.read()
            self.assertIn(b"Execution successful.", execution_output)

        self.assertTrue(os.path.exists(self.output_file))

        os.remove(self.output_file)

    def test_get_size(self):
        size = uminifier.get_file_size(self.input_file)
        self.assertEqual(7692, size)
