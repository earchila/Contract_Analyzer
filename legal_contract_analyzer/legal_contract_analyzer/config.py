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
"""Configuration module for the Legal Contract Analysis agent."""

import os
import logging
from typing import Optional # Changed from | None for broader Python compatibility if needed, though | is fine for 3.10+
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field


logging.basicConfig(level=logging.INFO) # Adjusted default logging level
logger = logging.getLogger(__name__)


class AgentModelSettings(BaseModel):
    """Agent model settings."""
    # Defaulting to gemini-pro as discussed in our plan, but example had flash
    name: str = Field(default="ContractAnalysisAgent")
    model: str = Field(default="gemini-2.0-flash-001") # Keeping flash as per example, can be changed


class Config(BaseSettings):
    """Configuration settings for the Legal Contract Analysis agent."""

    model_config = SettingsConfigDict(
        env_file=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), ".env" # Assumes .env is in the same directory as config.py
        ),
        env_prefix="GOOGLE_", # This will load GOOGLE_CLOUD_PROJECT, GOOGLE_CLOUD_LOCATION etc.
        case_sensitive=True,
        extra='ignore' # Ignores extra fields in .env not defined in Config
    )

    agent_settings: AgentModelSettings = Field(default_factory=AgentModelSettings)
    app_name: str = "LegalContractAnalysisApp"

    # These will be loaded from .env due to env_prefix="GOOGLE_"
    CLOUD_PROJECT: str = Field(default="YOUR_PROJECT_ID_HERE") # Default if not in .env
    CLOUD_LOCATION: str = Field(default="us-central1")      # Default if not in .env
    GENAI_USE_VERTEXAI: str = Field(default="1")             # Default if not in .env
    API_KEY: Optional[str] = Field(default=None)             # Default if not in .env

# Instantiate the config object for easy import and use elsewhere
settings = Config()

# Example of how to access settings:
if __name__ == "__main__":
    logger.info(f"Application Name: {settings.app_name}")
    logger.info(f"Agent Name: {settings.agent_settings.name}")
    logger.info(f"Agent Model: {settings.agent_settings.model}")
    logger.info(f"Google Cloud Project: {settings.CLOUD_PROJECT}")
    logger.info(f"Google Cloud Location: {settings.CLOUD_LOCATION}")
    logger.info(f"Use Vertex AI: {settings.GENAI_USE_VERTEXAI}")
    logger.info(f"API Key (masked): {'********' if settings.API_KEY else 'Not set'}")
    # Check if .env was loaded
    if settings.CLOUD_PROJECT == "YOUR_PROJECT_ID_HERE" and os.path.exists(settings.model_config.env_file):
        # A more robust check would be to see if a value expected from .env is different from default
        pass # Basic check already in place
    elif not os.path.exists(settings.model_config.env_file):
         logger.warning(f".env file not found at {settings.model_config.env_file}")