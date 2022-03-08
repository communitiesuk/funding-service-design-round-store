from typing import List

from tests.sample_data.rounds import ROUNDS

from .models import Round


def select_rounds(fund_id: str) -> List[Round]:
    rounds = []
    for fund_round in ROUNDS:
        if fund_round.get("fund_id") == fund_id:
            rounds.append(Round.from_dict(fund_round))
    return rounds


def select_round(fund_id: str, round_id: str) -> Round | None:
    for fund_round in ROUNDS:
        if fund_round.get("fund_id") == fund_id and round_id == fund_round.get(
            "round_id"
        ):
            return Round.from_dict(fund_round)
    return None


def select_json_rounds(fund_id: str) -> List[dict] | None:
    rounds = select_rounds(fund_id)
    if rounds:
        return [r.as_json() for r in rounds]


def select_json_round(fund_id: str, round_id: str) -> List[dict] | None:
    round = select_round(fund_id, round_id)
    if round:
        return round.as_json()
