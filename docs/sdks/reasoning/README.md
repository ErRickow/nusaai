# Reasoning
(*reasoning*)

## Overview

### Available Operations

* [reasoning](#reasoning) - Reasoning completion

## reasoning

Generate reasoning for complex problems.

### Example Usage

```typescript
import { Neosantara } from "neosantara-ai";

const neosantara = new Neosantara({
  apiKey: process.env["NEOSANTARA_API_KEY"] ?? "",
});

async function run() {
  const result = await neosantara.reasoning.reasoning({
    model: "nusantara-base",
    messages: [],
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { NeosantaraCore } from "neosantara-ai/core.js";
import { reasoningReasoning } from "neosantara-ai/funcs/reasoningReasoning.js";

// Use `NeosantaraCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const neosantara = new NeosantaraCore({
  apiKey: process.env["NEOSANTARA_API_KEY"] ?? "",
});

async function run() {
  const res = await reasoningReasoning(neosantara, {
    model: "nusantara-base",
    messages: [],
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("reasoningReasoning failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [components.ReasoningRequest](../../models/components/reasoningrequest.md)                                                                                                     | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.ChatCompletionsResponse](../../models/components/chatcompletionsresponse.md)\>**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.BadRequestError | 400                    | application/json       |
| errors.AuthError       | 401                    | application/json       |
| errors.RateLimitError  | 429                    | application/json       |
| errors.ServerError     | 500                    | application/json       |
| errors.NAIError        | 4XX, 5XX               | \*/\*                  |