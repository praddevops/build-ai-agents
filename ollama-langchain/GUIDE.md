# User vs System in Chat Prompt Templates

When designing chat prompt templates, understanding the distinction between user and system messages is crucial for creating effective AI interactions. Here's a breakdown:

## System Messages
**Purpose:** Provide high-level context, set the tone, persona, or constraints for the AI.  
**Examples:**
- "You are a friendly and knowledgeable assistant."
- "Always respond in a professional tone and provide concise answers."

**Role:** These messages establish the AI's behavior and guide its responses throughout the interaction.

## User Messages
**Purpose:** Represent the input or queries from the user interacting with the AI.  
**Examples:**
- "What is the weather like today?"
- "Can you help me write a cover letter?"

**Role:** These messages are dynamic and task-specific, driving the immediate interaction.

## Key Differences
| Aspect    | System Messages                        | User Messages                       |
|-----------|---------------------------------------|------------------------------------|
| Focus     | High-level context and instructions   | Specific tasks or queries          |
| Tone      | Directive and guiding                 | Conversational and varied          |
| Frequency | Typically set once per session        | Changes with each user interaction  |



References:
https://langchain-doc.readthedocs.io/en/latest/getting_started/getting_started.html
https://lagnchain.readthedocs.io/en/stable/modules/prompts/chat_prompt_template.html
