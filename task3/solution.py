from task3.test_data import tests


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals["lesson"]
    total_time = 0

    tutor_intervals = normalize_intervals(intervals["tutor"])
    pupil_intervals = normalize_intervals(intervals["pupil"])

    for tutor_start, tutor_end in zip(tutor_intervals[::2],
                                      tutor_intervals[1::2]):
        for pupil_start, pupil_end in zip(pupil_intervals[::2],
                                          pupil_intervals[1::2]):
            overlap_start = max(tutor_start, pupil_start, lesson_start)
            overlap_end = min(tutor_end, pupil_end, lesson_end)
            total_time += max(0, overlap_end - overlap_start)

    return total_time


def normalize_intervals(intervals: list[int]) -> list[int]:
    normalized_intervals: list[int] = []

    for i in range(0, len(intervals), 2):
        start, end = intervals[i], intervals[i + 1]
        merged = False

        for j in range(0, len(normalized_intervals), 2):
            norm_start, norm_end = normalized_intervals[j], \
            normalized_intervals[j + 1]

            if max(norm_start, start) <= min(norm_end, end):
                normalized_intervals[j] = min(norm_start, start)
                normalized_intervals[j + 1] = max(norm_end, end)
                merged = True
                break

        if not merged:
            normalized_intervals.extend([start, end])

    return normalized_intervals


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test[
            'answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
