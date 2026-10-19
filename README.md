# LangChain Tool Calling Demo

> **Learning project.** I built this to understand how LLM tool calling works. It is not production code.

## What it does

The LLM receives a request in plain English ("Add 1 and 40") and does not do the math itself. Instead, it returns a structured tool call with the arguments. My Python code reads those arguments and computes the result.

1. `Add` is a Pydantic schema that describes the tool (name, docstring, typed fields)
2. `bind_tools` tells the model the tool exists
3. The model answers with `tool_calls` containing `a` and `b`
4. `extract_and_add` reads the arguments and returns the sum

## Example output

```
LLM extracted: a = 1, b = 40
Result: 41
```

## What I learned

1. How to describe a tool with a Pydantic `BaseModel`, where the docstring and field descriptions guide the model
2. The model does not run the tool, it only returns the arguments
3. The structured data lives in `response.tool_calls`, not in `response.content`
4. `bind_tools` does not force a tool call, so the code must handle the case where there is none
5. The difference between `bind_tools` and `with_structured_output`

## Tech

Python, LangChain, Pydantic, Groq (`openai/gpt-oss-120b`)

## How to run

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # then add your own GROQ_API_KEY
python main.py
```
