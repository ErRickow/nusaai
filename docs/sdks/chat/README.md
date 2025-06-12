# Chat
(*chat*)

## Overview

Chat completion ala OpenAI

### Available Operations

* [chatCompletions](#chatcompletions) - Create chat completion (OpenAI-Compatible)

## chatCompletions

Membuat completion chat seperti OpenAI API. Kirim array messages (role: user/assistant, content: string).

### Example Usage

```typescript
import { Nusa } from "nusaai";

const nusa = new Nusa({
  apiKeyAuth: process.env["NUSA_XYZ_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await nusa.chat.chatCompletions({
    model: "nusantara-base",
    messages: [
      {
        role: "user",
        content: "Apa itu NusantaraAI?",
      },
    ],
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { NusaCore } from "nusaai/core.js";
import { chatChatCompletions } from "nusaai/funcs/chatChatCompletions.js";

// Use `NusaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const nusa = new NusaCore({
  apiKeyAuth: process.env["NUSA_XYZ_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await chatChatCompletions(nusa, {
    model: "nusantara-base",
    messages: [
      {
        role: "user",
        content: "Apa itu NusantaraAI?",
      },
    ],
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("chatChatCompletions failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [components.ChatCompletionsRequest](../../models/components/chatcompletionsrequest.md)                                                                                         | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
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
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |