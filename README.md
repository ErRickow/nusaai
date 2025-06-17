# nusaai
early sdk

<!-- Start Summary [summary] -->
## Summary

NusantaraAI API: API NusantaraAI - OpenAI Compatible

**Rate Limit**
Setiap API KEY memiliki limit berdasarkan tier:
- Free: 10 request/menit, 100/hari, 10.000 tokens/menit, 50.000/hari
- Basic: 50 request/menit, 500/hari, 100.000 tokens/menit, 500.000/hari
- Standard: 60 request/menit, 2000/hari, 100.000 tokens/menit, 1.000.000/hari
- Pro: 120 request/menit, 10.000/hari, 200.000 tokens/menit, 5.000.000/hari
- Enterprise: 200 request/menit, 50.000/hari, 500.000 tokens/menit, 10.000.000/hari

Limit berlaku **per API key** dan juga **per user** (akumulasi).
Jika limit terlewati, akan mendapat error 429.
Reset harian dan bulanan otomatis, serta auto-downgrade ke Free jika subscription habis.

Untuk detail sistem rate limit, lihat dokumentasi MDX.

**Auth:** Gunakan header `Authorization: Bearer <API_KEY>`.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [nusaai](#nusaai)
  * [SDK Installation](#sdk-installation)
  * [Requirements](#requirements)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Standalone functions](#standalone-functions)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to npm and others you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


The SDK can be installed with either [npm](https://www.npmjs.com/), [pnpm](https://pnpm.io/), [bun](https://bun.sh/) or [yarn](https://classic.yarnpkg.com/en/) package managers.

### NPM

```bash
npm add https://github.com/ErRickow/nusaai
```

### PNPM

```bash
pnpm add https://github.com/ErRickow/nusaai
```

### Bun

```bash
bun add https://github.com/ErRickow/nusaai
```

### Yarn

```bash
yarn add https://github.com/ErRickow/nusaai zod

# Note that Yarn does not install peer dependencies automatically. You will need
# to install zod as shown above.
```
<!-- End SDK Installation [installation] -->

<!-- Start Requirements [requirements] -->
## Requirements

For supported JavaScript runtimes, please consult [RUNTIMES.md](RUNTIMES.md).
<!-- End Requirements [requirements] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```typescript
import { Neosantara } from "neosantara-ai";

const neosantara = new Neosantara({
  apiKeyAuth: process.env["NAI_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await neosantara.chat.chatCompletions({
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
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name         | Type | Scheme      | Environment Variable |
| ------------ | ---- | ----------- | -------------------- |
| `apiKeyAuth` | http | HTTP Bearer | `NAI_API_KEY_AUTH`   |

To authenticate with the API the `apiKeyAuth` parameter must be set when initializing the SDK client instance. For example:
```typescript
import { Neosantara } from "neosantara-ai";

const neosantara = new Neosantara({
  apiKeyAuth: process.env["NAI_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await neosantara.chat.chatCompletions({
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
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [chat](docs/sdks/chat/README.md)

* [chatCompletions](docs/sdks/chat/README.md#chatcompletions) - Create chat completion (OpenAI-Compatible)

### [completions](docs/sdks/completions/README.md)

* [textCompletions](docs/sdks/completions/README.md#textcompletions) - OpenAI compatible completions (text only)

### [embeddings](docs/sdks/embeddings/README.md)

* [embeddings](docs/sdks/embeddings/README.md#embeddings) - Create embeddings (OpenAI-Compatible)

### [models](docs/sdks/models/README.md)

* [listModels](docs/sdks/models/README.md#listmodels) - List available models

### [moderations](docs/sdks/moderations/README.md)

* [moderations](docs/sdks/moderations/README.md#moderations) - Content moderation check


### [reasoning](docs/sdks/reasoning/README.md)

* [reasoning](docs/sdks/reasoning/README.md#reasoning) - Enhanced reasoning completion

### [system](docs/sdks/system/README.md)

* [systemStatus](docs/sdks/system/README.md#systemstatus) - System status and info

### [usage](docs/sdks/usage/README.md)

* [usage](docs/sdks/usage/README.md#usage) - Get usage statistics

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Standalone functions [standalone-funcs] -->
## Standalone functions

All the methods listed above are available as standalone functions. These
functions are ideal for use in applications running in the browser, serverless
runtimes or other environments where application bundle size is a primary
concern. When using a bundler to build your application, all unused
functionality will be either excluded from the final bundle or tree-shaken away.

To read more about standalone functions, check [FUNCTIONS.md](./FUNCTIONS.md).

<details>

<summary>Available standalone functions</summary>

- [`chatChatCompletions`](docs/sdks/chat/README.md#chatcompletions) - Create chat completion (OpenAI-Compatible)
- [`completionsTextCompletions`](docs/sdks/completions/README.md#textcompletions) - OpenAI compatible completions (text only)
- [`embeddingsEmbeddings`](docs/sdks/embeddings/README.md#embeddings) - Create embeddings (OpenAI-Compatible)
- [`modelsListModels`](docs/sdks/models/README.md#listmodels) - List available models
- [`moderationsModerations`](docs/sdks/moderations/README.md#moderations) - Content moderation check
- [`reasoningReasoning`](docs/sdks/reasoning/README.md#reasoning) - Enhanced reasoning completion
- [`systemSystemStatus`](docs/sdks/system/README.md#systemstatus) - System status and info
- [`usageUsage`](docs/sdks/usage/README.md#usage) - Get usage statistics

</details>
<!-- End Standalone functions [standalone-funcs] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries.  If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API.  However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a retryConfig object to the call:
```typescript
import { Neosantara } from "neosantara-ai";

const neosantara = new Neosantara({
  apiKeyAuth: process.env["NAI_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await neosantara.chat.chatCompletions({
    model: "nusantara-base",
    messages: [
      {
        role: "user",
        content: "Apa itu NusantaraAI?",
      },
    ],
  }, {
    retries: {
      strategy: "backoff",
      backoff: {
        initialInterval: 1,
        maxInterval: 50,
        exponent: 1.1,
        maxElapsedTime: 100,
      },
      retryConnectionErrors: false,
    },
  });

  console.log(result);
}

run();

```

If you'd like to override the default retry strategy for all operations that support retries, you can provide a retryConfig at SDK initialization:
```typescript
import { Neosantara } from "neosantara-ai";

const neosantara = new Neosantara({
  retryConfig: {
    strategy: "backoff",
    backoff: {
      initialInterval: 1,
      maxInterval: 50,
      exponent: 1.1,
      maxElapsedTime: 100,
    },
    retryConnectionErrors: false,
  },
  apiKeyAuth: process.env["NAI_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await neosantara.chat.chatCompletions({
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
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`NeosantaraError`](./src/models/errors/neosantaraerror.ts) is the base class for all HTTP error responses. It has the following properties:

| Property            | Type       | Description                                                                             |
| ------------------- | ---------- | --------------------------------------------------------------------------------------- |
| `error.message`     | `string`   | Error message                                                                           |
| `error.statusCode`  | `number`   | HTTP response status code eg `404`                                                      |
| `error.headers`     | `Headers`  | HTTP response headers                                                                   |
| `error.body`        | `string`   | HTTP body. Can be empty string if no body is returned.                                  |
| `error.rawResponse` | `Response` | Raw HTTP response                                                                       |
| `error.data$`       |            | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```typescript
import { Neosantara } from "neosantara-ai";
import * as errors from "neosantara-ai/models/errors";

const neosantara = new Neosantara({
  apiKeyAuth: process.env["NAI_API_KEY_AUTH"] ?? "",
});

async function run() {
  try {
    const result = await neosantara.chat.chatCompletions({
      model: "nusantara-base",
      messages: [
        {
          role: "user",
          content: "Apa itu NusantaraAI?",
        },
      ],
    });

    console.log(result);
  } catch (error) {
    // The base class for HTTP error responses
    if (error instanceof errors.NeosantaraError) {
      console.log(error.message);
      console.log(error.statusCode);
      console.log(error.body);
      console.log(error.headers);

      // Depending on the method different errors may be thrown
      if (error instanceof errors.BadRequestError) {
        console.log(error.data$.error); // errors.ErrorT
        console.log(error.data$.metadata); // components.Metadata
      }
    }
  }
}

run();

```

### Error Classes
**Primary errors:**
* [`NeosantaraError`](./src/models/errors/neosantaraerror.ts): The base class for HTTP error responses.
  * [`AuthError`](docs/models/errors/autherror.md): Error jika API key salah/kurang. Status code `401`.

<details><summary>Less common errors (9)</summary>

<br />

**Network errors:**
* [`ConnectionError`](./src/models/errors/httpclienterrors.ts): HTTP client was unable to make a request to a server.
* [`RequestTimeoutError`](./src/models/errors/httpclienterrors.ts): HTTP request timed out due to an AbortSignal signal.
* [`RequestAbortedError`](./src/models/errors/httpclienterrors.ts): HTTP request was aborted by the client.
* [`InvalidRequestError`](./src/models/errors/httpclienterrors.ts): Any input used to create a request is invalid.
* [`UnexpectedClientError`](./src/models/errors/httpclienterrors.ts): Unrecognised or unexpected error.


**Inherit from [`NeosantaraError`](./src/models/errors/neosantaraerror.ts)**:
* [`BadRequestError`](docs/models/errors/badrequesterror.md): Error untuk request yang tidak valid. Status code `400`. Applicable to 5 of 8 methods.*
* [`ServerError`](docs/models/errors/servererror.md): Error server internal. Status code `500`. Applicable to 5 of 8 methods.*
* [`RateLimitError`](docs/models/errors/ratelimiterror.md): Error jika terkena rate limit. Status code `429`. Applicable to 3 of 8 methods.*
* [`ResponseValidationError`](./src/models/errors/responsevalidationerror.ts): Type mismatch between the data returned from the server and the structure expected by the SDK. See `error.rawValue` for the raw value and `error.pretty()` for a nicely formatted multi-line string.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `serverURL: string` optional parameter when initializing the SDK client instance. For example:
```typescript
import { Neosantara } from "neosantara-ai";

const neosantara = new Neosantara({
  serverURL: "https://api.nusa.xyz/v1",
  apiKeyAuth: process.env["NAI_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await neosantara.chat.chatCompletions({
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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The TypeScript SDK makes API calls using an `HTTPClient` that wraps the native
[Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). This
client is a thin wrapper around `fetch` and provides the ability to attach hooks
around the request lifecycle that can be used to modify the request or handle
errors and response.

The `HTTPClient` constructor takes an optional `fetcher` argument that can be
used to integrate a third-party HTTP client or when writing tests to mock out
the HTTP client and feed in fixtures.

The following example shows how to use the `"beforeRequest"` hook to to add a
custom header and a timeout to requests and how to use the `"requestError"` hook
to log errors:

```typescript
import { Neosantara } from "neosantara-ai";
import { HTTPClient } from "neosantara-ai/lib/http";

const httpClient = new HTTPClient({
  // fetcher takes a function that has the same signature as native `fetch`.
  fetcher: (request) => {
    return fetch(request);
  }
});

httpClient.addHook("beforeRequest", (request) => {
  const nextRequest = new Request(request, {
    signal: request.signal || AbortSignal.timeout(5000)
  });

  nextRequest.headers.set("x-custom-header", "custom value");

  return nextRequest;
});

httpClient.addHook("requestError", (error, request) => {
  console.group("Request Error");
  console.log("Reason:", `${error}`);
  console.log("Endpoint:", `${request.method} ${request.url}`);
  console.groupEnd();
});

const sdk = new Neosantara({ httpClient });
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass a logger that matches `console`'s interface as an SDK option.

> [!WARNING]
> Beware that debug logging will reveal secrets, like API tokens in headers, in log messages printed to a console or files. It's recommended to use this feature only during local development and not in production.

```typescript
import { Neosantara } from "neosantara-ai";

const sdk = new Neosantara({ debugLogger: console });
```

You can also enable a default debug logger by setting an environment variable `NAI_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
