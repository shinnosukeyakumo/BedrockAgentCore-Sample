AgentCore Identity example (Cognito + OAuth inbound)

Files
- create_identity_config.py: Creates Cognito (User Pool + App Client + Hosted UI) and AgentCore Identity config, then saves settings.
- identity_agent.py: Runtime app that reads the config and uses AgentCore Identity.

Config file
- Identity/.agentcore_identity.json

Create Cognito + AgentCore Identity config
- uv run create_identity_config.py

Run runtime
- uv run identity_agent.py

Invoke (OAuth inbound)
- curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <cognito_access_token>" \
  -d '{"prompt":"アクセストークンを取得して"}'

Notes
- When USER_FEDERATION is used, the first request prints an authorization URL to the server console.
- Callback URL defaults to http://localhost:8080/oauth2/idpresponse (override with AGENTCORE_CALLBACK_URL if needed).
- Set AGENTCORE_FORCE_CREATE=1 to recreate Cognito + AgentCore Identity resources.
