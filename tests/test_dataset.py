import os

import pytest
from deepeval.dataset import EvaluationDataset
from deepeval.metrics import HallucinationMetric
from deepeval.evaluator import assert_test
from deepeval.test_case import LLMTestCase

dataset = EvaluationDataset()


def test_create_dataset():
    module_b_dir = os.path.dirname(os.path.realpath(__file__))

    file_path = os.path.join(module_b_dir, "data", "dataset.csv")

    dataset.add_test_cases_from_csv_file(
        file_path,
        input_col_name="query",
        actual_output_col_name="actual_output",
        expected_output_col_name="expected_output",
        context_col_name="context",
    )
    assert len(dataset.test_cases) == 5, "Test Cases not loaded from CSV"
    file_path = os.path.join(module_b_dir, "data", "dataset.json")
    dataset.add_test_cases_from_json_file(
        file_path,
        input_key_name="query",
        actual_output_key_name="actual_output",
        expected_output_key_name="expected_output",
        context_key_name="context",
    )
    assert len(dataset.test_cases) == 10, "Test Cases not loaded from JSON"

    # dataset.push("alias")


# dataset.pull("alias")
# @pytest.mark.parametrize(
#     "test_case",
#     dataset,
# )
# def test_customer_chatbot(test_case: LLMTestCase):
#     hallucination_metric = HallucinationMetric(minimum_score=0.3)
#     assert_test(test_case, [hallucination_metric])
