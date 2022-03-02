from apis.models import api


class FundingRounds:
    """A dummy interface to use instead of a database ORM."""

    def __init__(self):
        self.rounds = {}

    def get_all(self, fund_id: str):
        rounds = [
            round_data
            for key, round_data in self.rounds.items()
            if key.startswith(self.get_key(fund_id, ""))
        ]
        return rounds

    @staticmethod
    def get_key(fund_id: str, round_id: str):
        return "|".join([fund_id, round_id])

    def create(self, data):
        key = self.get_key(data["fund_id"], data["round_id"])
        self.rounds[key] = data

    def load_dummy(self, fund_data):

        for fund in fund_data:

            self.create(fund)

    def get(self, fund_id: str, round_id: str):
        key = self.get_key(fund_id, round_id)
        if key in self.rounds.keys():
            return self.rounds[key]
        api.abort(
            404,
            f"Round with ID '{round_id}' for fund with ID '{fund_id}' "
            "could not be found",
        )
