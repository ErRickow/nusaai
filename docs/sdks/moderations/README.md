# Moderations
(*moderations*)

## Overview

Content moderation

### Available Operations

* [moderations](#moderations) - Content moderation check

## moderations

Melakukan pengecekan moderasi konten.

### Example Usage

```typescript
import { Neosantara } from "neosantara-ai";

const neosantara = new Neosantara({
  apiKeyAuth: process.env["NAI_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await neosantara.moderations.moderations({
    input: "Ini adalah teks yang akan dimoderasi",
    model: "text-moderation-latest",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { NeosantaraCore } from "neosantara-ai/core.js";
import { moderationsModerations } from "neosantara-ai/funcs/moderationsModerations.js";

// Use `NeosantaraCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const neosantara = new NeosantaraCore({
  apiKeyAuth: process.env["NAI_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await moderationsModerations(neosantara, {
    input: "Ini adalah teks yang akan dimoderasi",
    model: "text-moderation-latest",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("moderationsModerations failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [components.ModerationsRequest](../../models/components/moderationsrequest.md)                                                                                                 | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.ModerationsResponse](../../models/components/moderationsresponse.md)\>**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.BadRequestError | 400                    | application/json       |
| errors.AuthError       | 401                    | application/json       |
| errors.ServerError     | 500                    | application/json       |
| errors.SDKError        | 4XX, 5XX               | \*/\*                  |