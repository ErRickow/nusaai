# Chat

Types:

```python
from neosantaraai.types import (
    ChatCompletionsResponse,
    ChatMessage,
    Function,
    Metadata,
    ResponseFormat,
    Usage,
)
```

Methods:

- <code title="post /chat/completions">client.chat.<a href="./src/neosantaraai/resources/chat.py">create_completion</a>(\*\*<a href="src/neosantaraai/types/chat_create_completion_params.py">params</a>) -> <a href="./src/neosantaraai/types/chat_completions_response.py">ChatCompletionsResponse</a></code>

# Completions

Types:

```python
from neosantaraai.types import CompletionCreateResponse
```

Methods:

- <code title="post /completions">client.completions.<a href="./src/neosantaraai/resources/completions.py">create</a>(\*\*<a href="src/neosantaraai/types/completion_create_params.py">params</a>) -> <a href="./src/neosantaraai/types/completion_create_response.py">CompletionCreateResponse</a></code>

# Models

Types:

```python
from neosantaraai.types import ModelListResponse
```

Methods:

- <code title="get /models">client.models.<a href="./src/neosantaraai/resources/models.py">list</a>() -> <a href="./src/neosantaraai/types/model_list_response.py">ModelListResponse</a></code>

# Embeddings

Types:

```python
from neosantaraai.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/neosantaraai/resources/embeddings.py">create</a>(\*\*<a href="src/neosantaraai/types/embedding_create_params.py">params</a>) -> <a href="./src/neosantaraai/types/embedding_create_response.py">EmbeddingCreateResponse</a></code>

# Moderations

Types:

```python
from neosantaraai.types import ModerationCreateCheckResponse
```

Methods:

- <code title="post /moderations">client.moderations.<a href="./src/neosantaraai/resources/moderations.py">create_check</a>(\*\*<a href="src/neosantaraai/types/moderation_create_check_params.py">params</a>) -> <a href="./src/neosantaraai/types/moderation_create_check_response.py">ModerationCreateCheckResponse</a></code>

# Usage

Types:

```python
from neosantaraai.types import CurrentUsage, UsageRetrieveResponse
```

Methods:

- <code title="get /usage">client.usage.<a href="./src/neosantaraai/resources/usage.py">retrieve</a>(\*\*<a href="src/neosantaraai/types/usage_retrieve_params.py">params</a>) -> <a href="./src/neosantaraai/types/usage_retrieve_response.py">UsageRetrieveResponse</a></code>

# Reasoning

Methods:

- <code title="post /reasoning">client.reasoning.<a href="./src/neosantaraai/resources/reasoning.py">create</a>(\*\*<a href="src/neosantaraai/types/reasoning_create_params.py">params</a>) -> <a href="./src/neosantaraai/types/chat_completions_response.py">ChatCompletionsResponse</a></code>

# System

Types:

```python
from neosantaraai.types import SystemRetrieveStatusResponse
```

Methods:

- <code title="get /system/status">client.system.<a href="./src/neosantaraai/resources/system.py">retrieve_status</a>() -> <a href="./src/neosantaraai/types/system_retrieve_status_response.py">SystemRetrieveStatusResponse</a></code>
