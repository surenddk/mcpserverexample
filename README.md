# MCP Server Installation

## Install the server

1. Make sure you have `uv` installed on your machine.
2. Add the following entry to your MCP client configuration:

```json
{
  "mcpServers": {
    "test": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/surenddk/mcpserverexample.git",
        "mcp-server"
      ]
    }
  }
}
```

3. Restart the MCP client or reload the configuration.
4. Verify the server starts successfully and is available to the client.

This installs the server from the GitHub repository using `uvx` and runs the `mcp-server` command.
