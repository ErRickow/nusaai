# Completions
(*completions*)

## Overview

Text completions

### Available Operations

* [textCompletions](#textcompletions) - OpenAI compatible completions (text only)

## textCompletions

Membuat text completion menggunakan prompt string.

### Example Usage

```typescript
import { SDK } from "openapi";

const sdk = new SDK({
  apiKeyAuth: "<YOUR_BEARER_TOKEN_HERE>",
});

async function run() {
  const result = await sdk.completions.textCompletions({
    model: "nusantara-base",
    prompt: "Sebutkan 3 manfaat AI:",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { SDKCore } from "openapi/core.js";
import { completionsTextCompletions } from "openapi/funcs/completionsTextCompletions.js";

// Use `SDKCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const sdk = new SDKCore({
  apiKeyAuth: "<YOUR_BEARER_TOKEN_HERE>",
});

async function run() {
  const res = await completionsTextCompletions(sdk, {
    model: "nusantara-base",
    prompt: "Sebutkan 3 manfaat AI:",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("completionsTextCompletions failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [models.TextCompletionsRequest](../../models/textcompletionsrequest.md)                                                                                                        | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[models.TextCompletionResponse](../../models/textcompletionresponse.md)\>**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.BadRequestError | 400                    | application/json       |
| errors.AuthError       | 401                    | application/json       |
| errors.RateLimitError  | 429                    | application/json       |
| errors.ServerError     | 500                    | application/json       |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |