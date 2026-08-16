# A2-SEND — SEND + MORE = MONEY satisfiability

Submit one UTF-8 Lean file with the following exact public declaration. The
frozen LeanCSP environment supplies the model and witness-checking API.

```lean

open CSP.L2S
namespace RouteBenchSubmission.A2Send

theorem result : send_more_money.isSatisfiableInt

end RouteBenchSubmission.A2Send
```
