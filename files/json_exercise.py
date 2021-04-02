from collections import defaultdict
import json
from pathlib import Path
from typing import List


def mean(items: List[int]) -> float:
    return sum(items) / len(items)

def print_scores(directory: str) -> None:
    """takes a directory name as an argument and prints a summary of the student scores it finds"""
    template = '    {} min: {}, max: {}, average: {}'

    for fname in Path(directory).iterdir():
        print(fname)

        with open(fname) as f:
            data = json.load(f)
            scores_by_subject = defaultdict(list)

            for person in data:
                for subject, score in person.items():
                    scores_by_subject[subject].append(score)

            for subject, scores in scores_by_subject.items():
                print(template.format(subject, min(scores), max(scores), mean(scores)))
