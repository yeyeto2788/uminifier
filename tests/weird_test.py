import os
from unittest import TestCase
import uminifier
import subprocess


class WeirdTest(TestCase):
    data_dir = os.path.dirname(os.path.abspath(__file__))
    uminifier_dir = os.path.join(os.path.dirname(data_dir), "uminifier", "__init__.py")
    test_data = os.path.join(data_dir, "test_data")
    input_file = os.path.join(test_data, "bulleting_board.py")
    intermediary_file = os.path.join(test_data, "ibulleting_board.py")
    output_file = os.path.join(test_data, "bulleting_board.mpy")

    def setUp(self) -> None:
        files_needed = ["bulleting_board.py"]
        files_on_system = os.listdir(self.test_data)
        if files_on_system != files_needed:
            msg = f"Seems like file on {self.test_data}:\n{files_on_system}" \
                  f"Are different to {files_needed}"
            self.fail(msg=msg)

    def test_all_script(self) -> None:
        try:
            execution = subprocess.Popen(["uminifier", "-h"])
            execution.wait()
        except FileNotFoundError:
            pass
        else:
            print(execution.returncode)
        self.assertEqual(True, True)

    def test_execution(self) -> None:
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

    def test_execution_keeping_files(self) -> None:
        try:
            execution = subprocess.Popen(
                ["python", self.uminifier_dir, self.input_file, "-k"],
                stdout=subprocess.PIPE)
            execution.wait()
        except FileNotFoundError:
            self.fail("Python seems not be install")
        else:
            execution_output = execution.stdout.read()
            self.assertIn(b"Execution successful.", execution_output)

        self.assertTrue(os.path.exists(self.output_file))
        self.assertTrue(os.path.exists(self.intermediary_file))

    def test_get_size(self) -> None:
        size = uminifier.get_file_size(self.input_file)
        self.assertEqual(7692, size)

    def tearDown(self) -> None:

        files_to_delete = [
            self.intermediary_file,
            self.output_file
        ]
        for file in files_to_delete:
            if os.path.exists(file):
                print(f"Removing file {file}", flush=True)
                os.remove(file)
