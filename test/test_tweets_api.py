# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.79
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.tweets_api import TweetsApi


class TestTweetsApi(unittest.TestCase):
    """TweetsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TweetsApi()

    def tearDown(self) -> None:
        pass

    def test_add_or_delete_rules(self) -> None:
        """Test case for add_or_delete_rules

        Add/Delete rules
        """
        pass

    def test_create_tweet(self) -> None:
        """Test case for create_tweet

        Creation of a Tweet
        """
        pass

    def test_delete_tweet_by_id(self) -> None:
        """Test case for delete_tweet_by_id

        Tweet delete by Tweet ID
        """
        pass

    def test_find_tweet_by_id(self) -> None:
        """Test case for find_tweet_by_id

        Tweet lookup by Tweet ID
        """
        pass

    def test_find_tweets_by_id(self) -> None:
        """Test case for find_tweets_by_id

        Tweet lookup by Tweet IDs
        """
        pass

    def test_find_tweets_that_quote_a_tweet(self) -> None:
        """Test case for find_tweets_that_quote_a_tweet

        Retrieve Tweets that quote a Tweet.
        """
        pass

    def test_find_tweets_that_retweet_a_tweet(self) -> None:
        """Test case for find_tweets_that_retweet_a_tweet

        Retrieve Tweets that retweet a Tweet.
        """
        pass

    def test_get_rules(self) -> None:
        """Test case for get_rules

        Rules lookup
        """
        pass

    def test_get_tweets_firehose_stream(self) -> None:
        """Test case for get_tweets_firehose_stream

        Firehose stream
        """
        pass

    def test_get_tweets_sample10_stream(self) -> None:
        """Test case for get_tweets_sample10_stream

        Sample 10% stream
        """
        pass

    def test_hide_reply_by_id(self) -> None:
        """Test case for hide_reply_by_id

        Hide replies
        """
        pass

    def test_lists_id_tweets(self) -> None:
        """Test case for lists_id_tweets

        List Tweets timeline by List ID.
        """
        pass

    def test_sample_stream(self) -> None:
        """Test case for sample_stream

        Sample stream
        """
        pass

    def test_search_stream(self) -> None:
        """Test case for search_stream

        Filtered stream
        """
        pass

    def test_space_buyers(self) -> None:
        """Test case for space_buyers

        Retrieve the list of Users who purchased a ticket to the given space
        """
        pass

    def test_space_tweets(self) -> None:
        """Test case for space_tweets

        Retrieve Tweets from a Space.
        """
        pass

    def test_tweet_counts_full_archive_search(self) -> None:
        """Test case for tweet_counts_full_archive_search

        Full archive search counts
        """
        pass

    def test_tweet_counts_recent_search(self) -> None:
        """Test case for tweet_counts_recent_search

        Recent search counts
        """
        pass

    def test_tweets_fullarchive_search(self) -> None:
        """Test case for tweets_fullarchive_search

        Full-archive search
        """
        pass

    def test_tweets_recent_search(self) -> None:
        """Test case for tweets_recent_search

        Recent search
        """
        pass

    def test_users_id_like(self) -> None:
        """Test case for users_id_like

        Causes the User (in the path) to like the specified Tweet
        """
        pass

    def test_users_id_liked_tweets(self) -> None:
        """Test case for users_id_liked_tweets

        Returns Tweet objects liked by the provided User ID
        """
        pass

    def test_users_id_mentions(self) -> None:
        """Test case for users_id_mentions

        User mention timeline by User ID
        """
        pass

    def test_users_id_retweets(self) -> None:
        """Test case for users_id_retweets

        Causes the User (in the path) to retweet the specified Tweet.
        """
        pass

    def test_users_id_timeline(self) -> None:
        """Test case for users_id_timeline

        User home timeline by User ID
        """
        pass

    def test_users_id_tweets(self) -> None:
        """Test case for users_id_tweets

        User Tweets timeline by User ID
        """
        pass

    def test_users_id_unlike(self) -> None:
        """Test case for users_id_unlike

        Causes the User (in the path) to unlike the specified Tweet
        """
        pass

    def test_users_id_unretweets(self) -> None:
        """Test case for users_id_unretweets

        Causes the User (in the path) to unretweet the specified Tweet
        """
        pass


if __name__ == '__main__':
    unittest.main()
