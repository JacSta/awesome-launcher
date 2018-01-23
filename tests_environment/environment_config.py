import argparse


class EnvironmentConfig:
    @staticmethod
    def get_env_config():
        """
            --browser - browser instance for tests
            --app_url - link for web application
            --grid_url - link for grid/node (worker selenium), default: localhost
            --test_case - test case name with tests set
        """

        resolution = None

        parser = argparse.ArgumentParser()

        # Browser instance for tests
        parser.add_argument('--browser', '-b', default='chrome')

        # Web application URL address
        parser.add_argument('--app_url', '-url', default='http://automationpractice.com/index.php')

        # Worker address (node)
        parser.add_argument('--grid_url', '-gurl', default='http://localhost:4444/wd/hub')

        # Return result to terminal (unit) or to html file (html)
        parser.add_argument('--runner', '-r', default='html')

        parser.add_argument('--resolution', '-res', default='max')

        parser.add_argument('--test_case', '-tc', required=True)

        args = parser.parse_args()

        resolutions_list = {992: '1025',  # Tablet horizontal
                            768: '801',   # Tablet vertical
                            480: '513'}   # Smartphone
        if args.resolution == 'max':
            resolution = 'max'
        else:
            for key, value in resolutions_list.items():
                if args.resolution == str(key):
                    resolution = value
                    break
                else:
                    resolution = args.resolution
                    continue

        return {
            'browser': args.browser,
            'app_url': args.app_url,
            'grid_url': args.grid_url,
            'runner': args.runner,
            'original_resolution': args.resolution,
            'resolution': resolution,
            'resolutions_list': resolutions_list.values(),
            'test_case': args.test_case
        }
