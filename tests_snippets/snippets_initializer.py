class SnippetInitializer:
    """Each base snippet inherit from this"""

    def __init__(self, selenium, data_helper):
        self.selenium = selenium
        self.data_helper = data_helper

    @property
    def google_snippets(self):
        from .google_snippets.base_snippet import BaseSnippet
        return BaseSnippet(self.selenium, self.data_helper)

    @property
    def register_snippets(self):
        from .automationpractice_snippet.base_snippet import BaseSnippet
        return BaseSnippet(self.selenium, self.data_helper)
