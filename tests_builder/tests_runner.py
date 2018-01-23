import datetime
import os
import unittest
from tests_builder import HTMLTestRunner
from tests_environment.set_env_config import SetEnvConfig


class TestsRunner:
    def test_runner(self, test_suite):
        if SetEnvConfig().set_runner() == 'unit':
            runner = unittest.TextTestRunner(
                resultclass=unittest.TextTestResult,
                verbosity=2)
        else:
            if not os.path.exists('test_reports'):
                os.makedirs('test_reports')

            # open the report file
            outfile = open(os.getcwd() + "/test_reports/" + self.__gen_report_name(), "w")

            # configure HTMLTestRunner options
            runner = HTMLTestRunner.HTMLTestRunner(
                verbosity=2,
                stream=outfile,
                title=self.__gen_report_title(),
                description=self.__gen_report_description())

        result = runner.run(unittest.TestSuite(test_suite))
        print(['Result:', result])
        return result.wasSuccessful()

    # Test case loader
    def test_case_loader(self, test):
        return unittest.TestLoader().loadTestsFromTestCase(test)

    @staticmethod
    def __gen_report_name():
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_name = now + '_' + SetEnvConfig().set_browser() + '_' + SetEnvConfig().set_test_case() + '.html'
        return report_name

    @staticmethod
    def __gen_report_title():
        return 'Test Report - ' + SetEnvConfig().set_test_case() + ' functional_tests'

    @staticmethod
    def __gen_report_description():
        return str(['app_url:', SetEnvConfig().set_app_url(),
                    'grid_url:', SetEnvConfig().set_grid_url(),
                    'browser:', SetEnvConfig().set_browser(),
                    'original_resolution:', SetEnvConfig().set_original_resolution(),
                    'test_case:', SetEnvConfig().set_test_case()])
