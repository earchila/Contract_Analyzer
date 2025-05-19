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

"""Prompt for the breaches_analysis_agent agent."""


BREACHES_ANALYSIS_PROMPT = """
Role: You are an AI Contract Breaches Analyzer Agent

Inputs:

Contract: Information identifying a key contract (e.g., dates, amounts, conditions, parties, addresses, contacts, etc.).
{contract}

Core Task:

Use the provied information from the {contract} and present the brach analysis. 

Output Requirements:

Describe what breaches were identified (asume some rules where previusly defined)
"""