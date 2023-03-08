from typing import Any
import textwrap

from .gpt_client import chat_completion


def function_writer(name: str, n_parameters: int) -> str:
    conversation = [
        {
            "role": "system",
            "content": textwrap.dedent(
                """You are a python code generator that returns the code that satisfies the provided description. The answer should contain no explanation about the code, how it is working or any description. The output should be just code.""".strip()
            ),
        },
        {
            "role": "user",
            "content": f"write a function named '{name}' that receives {n_parameters} parameter(s)",
        },
    ]
    generated_code = chat_completion(conversation)
    if "```python" in generated_code:
        cleaned_code = generated_code.split("```python")[1].split("```")[0].strip()
    return cleaned_code


def function_caller(name: str):
    def f(*args):
        code = function_writer(name, len(args))
        locals: dict[str, Any] = {}
        exec(code, globals(), locals)
        for key, value in locals.items():
            globals()[key] = value
        func = locals[name]
        return func(*args)

    return f


def function_explainer(name: str):
    def f(*args):
        print(function_writer(name, len(args)))

    return f


class Explainer:
    def __getattr__(self, name: str):
        return function_explainer(name)


class GPTClass:
    @property
    def explain(self):
        """Prints the code of the generated method
        Example: `GPTClass().explain.add(4, 5)`

        :return: None
        :rtype: None
        """
        return Explainer()

    def __getattr__(self, name: str):
        return function_caller(name)
