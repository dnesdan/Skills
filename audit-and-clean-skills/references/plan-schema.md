# Cleanup plan schema

Write `plan.json` with this shape:

```json
{
  "schema_version": 1,
  "created_at": "ISO-8601 timestamp",
  "audit_roots": ["/absolute/path"],
  "inventory_sha256": "sha256 of inventory.json",
  "actions": [
    {
      "id": "A-001",
      "operation": "KEEP | REPAIR_ALIAS | UPDATE | MERGE | MOVE_TO_PROJECT | ARCHIVE | DISABLE | UNINSTALL | DELETE",
      "sources": ["/absolute/path"],
      "destination": "/absolute/path or null",
      "expected_hashes": {
        "/absolute/path": "sha256 or null"
      },
      "reason": "Evidence-based reason",
      "preserve": ["Unique behavior or artifact"],
      "risk": "low | medium | high",
      "recovery": "One-step recovery method",
      "restart_required": false,
      "approved": false
    }
  ],
  "human_decisions": []
}
```

Use absolute paths. Keep `approved` false in the audit. Do not store credentials, file contents, session excerpts, or secret-bearing environment values.
