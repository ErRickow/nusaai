# Chat

Types:

```python
from neosantara.types import (
    ChatCompletionsResponse,
    ChatMessage,
    Function,
    Metadata,
    ResponseFormat,
    Usage,
)
```

Methods:

- <code title="post /chat/completions">client.chat.<a href="./src/neosantara/resources/chat.py">create_completion</a>(\*\*<a href="src/neosantara/types/chat_create_completion_params.py">params</a>) -> <a href="./src/neosantara/types/chat_completions_response.py">ChatCompletionsResponse</a></code>

# Completions

Types:

```python
from neosantara.types import CompletionCreateResponse
```

Methods:

- <code title="post /completions">client.completions.<a href="./src/neosantara/resources/completions.py">create</a>(\*\*<a href="src/neosantara/types/completion_create_params.py">params</a>) -> <a href="./src/neosantara/types/completion_create_response.py">CompletionCreateResponse</a></code>

# Models

Types:

```python
from neosantara.types import ModelListResponse
```

Methods:

- <code title="get /models">client.models.<a href="./src/neosantara/resources/models.py">list</a>() -> <a href="./src/neosantara/types/model_list_response.py">ModelListResponse</a></code>

# Embeddings

Types:

```python
from neosantara.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/neosantara/resources/embeddings.py">create</a>(\*\*<a href="src/neosantara/types/embedding_create_params.py">params</a>) -> <a href="./src/neosantara/types/embedding_create_response.py">EmbeddingCreateResponse</a></code>

# Moderations

Types:

```python
from neosantara.types import ModerationCreateCheckResponse
```

Methods:

- <code title="post /moderations">client.moderations.<a href="./src/neosantara/resources/moderations.py">create_check</a>(\*\*<a href="src/neosantara/types/moderation_create_check_params.py">params</a>) -> <a href="./src/neosantara/types/moderation_create_check_response.py">ModerationCreateCheckResponse</a></code>

# Usage

Types:

```python
from neosantara.types import CurrentUsage, UsageRetrieveResponse
```

Methods:

- <code title="get /usage">client.usage.<a href="./src/neosantara/resources/usage.py">retrieve</a>(\*\*<a href="src/neosantara/types/usage_retrieve_params.py">params</a>) -> <a href="./src/neosantara/types/usage_retrieve_response.py">UsageRetrieveResponse</a></code>

# Reasoning

Methods:

- <code title="post /reasoning">client.reasoning.<a href="./src/neosantara/resources/reasoning.py">create</a>(\*\*<a href="src/neosantara/types/reasoning_create_params.py">params</a>) -> <a href="./src/neosantara/types/chat_completions_response.py">ChatCompletionsResponse</a></code>

# System

Types:

```python
from neosantara.types import SystemRetrieveStatusResponse
```

Methods:

- <code title="get /system/status">client.system.<a href="./src/neosantara/resources/system.py">retrieve_status</a>() -> <a href="./src/neosantara/types/system_retrieve_status_response.py">SystemRetrieveStatusResponse</a></code>
