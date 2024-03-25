#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """Bot Configuration"""

    ASSISTANT_ID = "asst_08b7K1bJIjQ7uRc7yZpVnwHN"
    MODEL = "gpt-3.5-turbo"  # we could use "gpt-4-turbo-preview" here
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
