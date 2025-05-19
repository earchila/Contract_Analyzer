# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Contract Analyzer Agent"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.breaches_analysis import breaches_analysis_agent
from .sub_agents.penalty_calculation import penalty_calculation_agent

MODEL = "gemini-2.5-pro-preview-05-06"

contract_analyzer = LlmAgent(
    name="contract_analyzer",
    model=MODEL,
    description=(
        "analyzing contracts provided by the users, "
        "providing breaches identified,"
        "and calculate poenalties"
    ),
    instruction=prompt.CONTRACT_ANALYZER_PROMPT,
    output_key="contract",
    tools=[
        AgentTool(agent=breaches_analysis_agent),
        AgentTool(agent=penalty_calculation_agent),
    ],
)

root_agent = contract_analyzer