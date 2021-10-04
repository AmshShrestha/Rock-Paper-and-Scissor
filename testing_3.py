import pytest

def score_obtained(score):
    return score

def testing_highscore():
    high_score=1
    assert(score_obtained(0)<high_score) is True==True