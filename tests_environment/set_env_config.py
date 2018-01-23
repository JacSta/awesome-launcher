from tests_environment.environment_config import EnvironmentConfig


class SetEnvConfig:
    @staticmethod
    def set_env_config():
        return EnvironmentConfig().get_env_config()

    def set_browser(self):
        return self.set_env_config()['browser']

    def set_app_url(self):
        return self.set_env_config()['app_url']

    def set_grid_url(self):
        return self.set_env_config()['grid_url']

    def set_runner(self):
        return self.set_env_config()['runner']

    def set_original_resolution(self):
        return self.set_env_config()['original_resolution']

    def set_resolution(self):
        return self.set_env_config()['resolution']

    def set_resolutions_list(self):
        return self.set_env_config()['resolutions_list']

    def set_test_case(self):
        return self.set_env_config()['test_case']
