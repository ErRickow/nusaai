<!-- Start SDK Example Usage [usage] -->
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