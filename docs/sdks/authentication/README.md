# Authentication
(*authentication*)

## Overview

### Available Operations

* [checkApiKeyStatus](#checkapikeystatus) - Check API Key status

## checkApiKeyStatus

Check status and remaining usage of API Key.

### Example Usage

```typescript
import { Neosantara } from "neosantara-ai";

const neosantara = new Neosantara({
  apiKey: process.env["NEOSANTARA_API_KEY"] ?? "",
});

async function run() {
  const result = await neosantara.authentication.checkApiKeyStatus();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { NeosantaraCore } from "neosantara-ai/core.js";
import { authenticationCheckApiKeyStatus } from "neosantara-ai/funcs/authenticationCheckApiKeyStatus.js";

// Use `NeosantaraCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const neosantara = new NeosantaraCore({
  apiKey: process.env["NEOSANTARA_API_KEY"] ?? "",
});

async function run() {
  const res = await authenticationCheckApiKeyStatus(neosantara);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("authenticationCheckApiKeyStatus failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.CheckApiKeyStatusResponseBody](../../models/operations/checkapikeystatusresponsebody.md)\>**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.AuthError      | 401                   | application/json      |
| errors.RateLimitError | 429                   | application/json      |
| errors.ServerError    | 500                   | application/json      |
| errors.NAIError       | 4XX, 5XX              | \*/\*                 |