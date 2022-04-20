from operator import itemgetter
from typing import List

from database.initial_data import initial_round_store_state
from dateutil import parser as date_parser
from dateutil.tz import UTC
from slugify import slugify


class RoundDataAccessObject(object):
    """
    A data interface to our currently in-memory data store
    """

    def __init__(self):
        self._rounds: dict = initial_round_store_state

    @property
    def rounds_index(self) -> dict:
        rounds = {}
        for round_id, fund_round in self._rounds.items():
            round_summary = {
                "id": fund_round.get("id"),
                "fund_id": fund_round.get("fund_id"),
                "round_id": fund_round.get("round_id"),
                "round_title": fund_round.get("round_title"),
                "opens": fund_round.get("opens"),
                "deadline": fund_round.get("deadline"),
                "eligibility_criteria": fund_round.get("eligibility_criteria"),
                "assessment_deadline": fund_round.get("assessment_deadline"),
                "application_url": fund_round.get("application_url"),
            }
            rounds.update({fund_round.get("id"): round_summary})
        return rounds

    def create_round(self, fund_round):
        round_id = slugify(fund_round["name"])
        round_id, new_round = self.set_attributes(round_id, fund_round)
        self._rounds.update({round_id: new_round})
        return new_round

    def get_round(self, fund_round_id: str):
        return self._rounds.get(fund_round_id)

    def get_round_of_fund(self, fund_id: str, round_id: str):
        fund_round_id = ":".join([fund_id, round_id])
        return self._rounds.get(fund_round_id)

    def get_rounds_of_fund(self, fund_id: str) -> List:
        params = {
            "fund_id": fund_id,
        }
        return self.search_rounds(params)

    @staticmethod
    def set_attributes(round_id: str, round_raw: dict) -> tuple:
        fund_round = round_raw
        return fund_round["id"], fund_round

    def search_rounds(self, params) -> List:
        """
        Returns a list of rounds matching required params
        """
        matching_rounds = []
        datetime_opens = params.get("datetime_opens")
        datetime_deadline = params.get("datetime_deadline")
        fund_id = params.get("fund_id")
        order_by = params.get("order_by", "opens")
        order_rev = params.get("order_rev") == "1"

        for round_id, fund_round in self.rounds_index.items():
            match = True

            # Exclude results if given parameters are not a match

            if fund_id and fund_id != fund_round.get("fund_id"):
                match = False

            if datetime_opens:
                start = date_parser.parse(datetime_opens).astimezone(UTC)
                if start > fund_round["opens"].astimezone(UTC):
                    match = False

            if datetime_deadline:
                end = date_parser.parse(datetime_deadline).astimezone(UTC)
                if fund_round["deadline"].astimezone(UTC) > end:
                    match = False

            if match:
                matching_rounds.append(fund_round)

        if order_by and order_by in ["opens", "deadline"]:
            matching_rounds = sorted(
                matching_rounds, key=itemgetter(order_by), reverse=order_rev
            )

        return matching_rounds


# An in memory data object instance


ROUNDS = RoundDataAccessObject()
