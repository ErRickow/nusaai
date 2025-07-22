<!-- Start SDK Example Usage [usage] -->
```typescript
import { Neosantara } from "neosantara-ai";

const neosantara = new Neosantara({
  apiKey: process.env["NEOSANTARA_API_KEY"] ?? "",
});

async function run() {
  const result = await neosantara.chat.chatCompletions({
    model: "nusantara-base",
    messages: [
      {
        role: "system",
        content: "<value>",
      },
    ],
  });

  console.log(result);
}

run();

```
<!-- End SDK Example Usage [usage] -->