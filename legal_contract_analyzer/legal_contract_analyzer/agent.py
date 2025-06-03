from google.adk.agents import Agent
# Assuming tools.py is in the same directory or accessible in PYTHONPATH
from .tools.tools import process_contract_document, detect_contract_breaches, calculate_contract_penalties
from .config import settings # Import the settings object

# Define the main contract analysis agent
root_agent = Agent(
    name=settings.agent_settings.name,
    model=settings.agent_settings.model,
    description=(
        "Orchestrates the contract analysis workflow, manages user interaction, "
        "and delegates tasks to specialized tools for parsing contracts, "
        "extracting key data, identifying potential breaches, and calculating penalties."
    ),
    instruction=(
        "You are an AI assistant for legal contract analysis. Your primary role is to help "
        "users by processing PDF contract documents. "
        "When a user provides a PDF contract (either by mentioning a file or if a file is uploaded/attached), "
        "your first step is to use the 'process_contract_document' tool to analyze it. "
        "The 'pdf_file_path' parameter for this tool should be the reference to the provided contract. "
        "After processing, present the summary and extracted data to the user. "
        "Then, inform the user that they can request 'breach detection' or 'penalty calculation' next. "
        "Await further instructions from the user to invoke those subsequent tools."
    ),
    tools=[
        process_contract_document,
        detect_contract_breaches,
        calculate_contract_penalties
    ],
    # enable_reflection=True # Optional: for more advanced agent behaviors if needed
)

if __name__ == '__main__':
    # This block is for conceptual testing if you run this file directly.
    # For ADK, you'd typically run `adk run ContractAnalysisAgent` from the
    # directory containing the 'legal_contract_analyzer' PARENT folder,
    # or ensure 'legal_contract_analyzer.agent' is discoverable.
    print(f"root_agent defined with name: {root_agent.name} and model: {root_agent.model}")
    print(f"Registered tools: {[tool.__name__ for tool in root_agent.tools]}")
    print(f"To run, typically use: adk run {settings.agent_settings.name}") # ADK run uses the agent's configured name

    # Example of how you might simulate an interaction (very basic):
    # This is NOT how ADK agents are typically run for real interactions.
    # It's just for a quick conceptual check.
    print("\n--- Conceptual Test (Direct tool call, not ADK runtime) ---")
    if root_agent.tools:
        first_tool = root_agent.tools[0]
        print(f"Attempting to conceptually call the first registered tool: {first_tool.__name__}")
        
        # Create a dummy PDF for the conceptual test (relative to where this script might be run from)
        # For this __main__ block, it's tricky due to packaging.
        # Better to test tools directly from their own __main__ blocks or via ADK.
        dummy_pdf_for_agent_test = "dummy_for_agent_test.pdf" 
        # Note: Path for dummy file in __main__ might need adjustment if running from package root.
        # For simplicity, this test might fail on FileNotFoundError if not run from the correct context.
        
        # A more robust way for a __main__ test in a package might be to create the dummy file
        # in a known temporary location or ensure the script's CWD is predictable.
        # For now, we'll just print a message.
        print(f"Conceptual test would try to use a dummy file like: {dummy_pdf_for_agent_test}")
        print("To properly test, run the agent via ADK or test tools.py directly.")

    else:
        print("No tools registered with the agent yet.")