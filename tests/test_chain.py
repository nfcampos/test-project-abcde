from langchain.llms import HumanInputLLM

from langchain_test_project_abcde import get_chain


def test_my_chain() -> None:
    """Edit this test to test your chain."""
    llm = HumanInputLLM(input_func=lambda: "baz")
    chain = get_chain(llm)
    chain.invoke({"text": "foo"})
