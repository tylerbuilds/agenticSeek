# Tool Creation Guide for AgenticSeek

This guide explains how to create custom tools for AgenticSeek agents.

## Prerequisites

- Python 3.10 or higher
- Basic familiarity with Python and AI models
- Understanding of the AgenticSeek architecture

## Tool Architecture

Tools are extensions that enable agents to perform specific actions, such as running Python code, making API calls, or conducting web searches. All tools inherit from the Tools base class, which provides methods for parsing and executing tool instructions.

## Understanding Tool Blocks

Agents invoke tools using a standardized format called a block. A block consists of the tool name followed by the content (e.g., code, query, or parameters) to execute.

### Basic Format

```<tool name>
<code or query to execute>
```

### Example

```web_search
What to do in Taipei?
```

### Multiple Arguments

Each tool can handle arguments in its own way within the block:

```trip_search
from=Paris
to=Toulouse
```

To extract these parameters, use the `get_parameter_value` method provided by the Tools class.

### Saving Output to Files

The content of blocks can be saved using :path notation:

```python:toto.py
print("Hello world")
```

This saves the code in toto.py file within the work_folder defined in config.ini

## Tool Implementation

When developing a tool, you must implement three abstract methods defined in the Tools class:

### 1. Execute Method

```python
@abstractmethod
def execute(self, blocks: [str], safety: bool) -> str:
    """
    Processes the provided block(s) and produces a result.
    
    Args:
        blocks: List of code/query blocks to execute
        safety: Whether human intervention is required
        
    Returns:
        str: The output/result from executing the tool
    """
    pass
```

### 2. Execution Failure Check

```python
@abstractmethod
def execution_failure_check(self, output: str) -> bool:
    """
    Analyzes the tool's output to determine if execution failed.
    
    Args:
        output: The output string from the tool execution
        
    Returns:
        bool: True if execution failed, False if successful
    """
    pass
```

### 3. Interpreter Feedback

```python
@abstractmethod
def interpreter_feedback(self, output: str) -> str:
    """
    Generates feedback message for the LLM.
    
    Args:
        output: The output from execution
        
    Returns:
        str: Feedback message for the LLM
    """
    pass
```

## Tool Methods Reference

- `load_exec_block`: Extracts and parses tool blocks from agent's response
- `get_parameter_value`: Retrieves parameter values from a block's content
- File handling: Supports saving block content to files when :path is specified

## Adding a Tool to an Agent

To add a tool to an agent:

1. Import the tool
2. Add the tool class to the **tools** dictionary
3. Update the agent prompt

### Example

```python
from sources.tools.flightSearch import FlightSearch

class CasualAgent(Agent):
    def __init__(self, name, prompt_path, provider, verbose=False):
        super().__init__(name, prompt_path, provider, verbose, None)
        self.tools = {
            "flight_search": FlightSearch(),
        }
        self.role = "en"
        self.type = "casual_agent"
```

## Prompting an Agent for Tool Usage

Update the agent's prompt file to instruct the LLM to use the tool:

```
You can search for flights using the flight_search tool. Example:
```flight_search
RY7481
```
You simply need to enter the flight number. You will receive information about:
- Airline
- Status
- Departure time
- Arrival time
```

## Best Practices

### Privacy First
- All core functionality must be able to run 100% locally
- Cloud services should only be optional alternatives
- Remote APIs are only allowed for specific tools (weather API, MCP, flight search, etc.)

### Tool Design
- Tools should be self-contained and follow the Tools base class
- Each tool should do one thing well
- Tools should provide clear feedback on success/failure

### Code Quality
- Write clear, self-documenting code
- Include type hints and docstrings
- Follow existing patterns in the codebase
- Add `if __name__ == "__main__"` at the bottom for individual testing
- Ideally include automated tests

### Error Handling
- Fail gracefully with meaningful messages
- Include recovery mechanisms where possible
- Log errors appropriately without exposing sensitive data

## Example Tool Structure

```python
import os, sys
import dotenv

dotenv.load_dotenv()

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from sources.tools.tools import Tools

class YourTool(Tools):
    def __init__(self, api_key: str = None):
        super().__init__()
        self.tag = "your_tool"
        self.name = "Your Tool Name"
        self.description = "Tool description"
        self.api_key = api_key or os.getenv("YOUR_API_KEY")

    def execute(self, blocks: str, safety: bool = True) -> str:
        # Implement your tool logic here
        pass

    def execution_failure_check(self, output: str) -> bool:
        # Check if execution failed
        return output.startswith("Error")

    def interpreter_feedback(self, output: str) -> str:
        # Generate feedback for the LLM
        if self.execution_failure_check(output):
            return f"Tool failed: {output}"
        return f"Tool succeeded:\n{output}"

if __name__ == "__main__":
    tool = YourTool()
    result = tool.execute(["test input"], safety=True)
    print(tool.interpreter_feedback(result))
```

## Testing Your Tool

Create a test in the `tests/` directory following the existing patterns.

## Contributing

See CONTRIBUTING.md for full contribution guidelines and how to submit your tool to the AgenticSeek project.

---

Created: 2025-11-05
Source: AgenticSeek CONTRIBUTING.md

