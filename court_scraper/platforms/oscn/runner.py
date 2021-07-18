import logging

from court_scraper.base.runner import BaseRunner
from .site import Site


logger = logging.getLogger(__name__)


class Runner(BaseRunner):
    """
    Facade class to simplify invocation and usage of scrapers.

    Arguments:

    - cache_dir -- Path to cache directory for scraped file artifacts (default: {})
    - config_path -- Path to location of config file
    - place_id -- Scraper ID made up of state and county (e.g. ga_dekalb)

    """

    def search(self, search_terms=[], **kwargs):
        """
        For a given scraper, executes the search, acquisition
        and processing of case info.

        Keyword arguments:

        - search_terms - List of search terms

        Returns: List of dicts containing case metadata
        """
        site = Site(self.place_id)
        logger.info(
            "Executing search for {}".format(self.place_id)
        )
        data = site.search(search_terms=search_terms)
        return data