# GPTClass
**GPTClass** is a Python class that uses OpenAI's GPT to generated the code that does what you need with minimal information.

[![version](https://img.shields.io/pypi/v/gptclass?logo=pypi&logoColor=white)](https://pypi.org/project/gptclass/)

## Installation
```bash
pip install gptclass
```

## Usage
Do whatever you need: 
```python
>>> import openai
>>> openai.api_key = "..."

>>> from gptclass import GPTClass
>>> gpt = GPTClass()

>>> gpt.add(1, 2)
3
>>> gpt.n_unique([1, 2, 5, 5])
3
>>> gpt.prime_numbers_below(10)
[2, 3, 5, 7]
>>> gpt.count_vowels("Today I had a nice coffee!")
10
>>> gpt.from_celsius_to_fahrenheit(25)
77.0
```

## Show me the generated code
Adding explain before invoking the method will print the code:

```python
>>> gpt.explain.from_celsius_to_fahrenheit(25)
def from_celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32
```

## Notes
- Inspired on: [davinci-functions](https://github.com/odashi/davinci-functions/tree/main)

## Warning
- The code produced may not be reliable and should be validated before executing it.