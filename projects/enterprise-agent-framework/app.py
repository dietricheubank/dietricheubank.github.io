"""Safe synthetic agent workflow: allowlists, approval, and audit. No external effects."""
from dataclasses import dataclass, field
from typing import Callable

@dataclass
class Decision:
    tool: str
    args: dict
    approved: bool
    outcome: str

@dataclass
class Agent:
    tools: dict[str, Callable]
    privileged: set[str] = field(default_factory=set)
    audit: list[Decision] = field(default_factory=list)

    def execute(self, tool: str, args: dict, *, approved: bool = False) -> str:
        if tool not in self.tools:
            self.audit.append(Decision(tool, dict(args), False, "DENIED_UNKNOWN_TOOL"))
            return "DENIED_UNKNOWN_TOOL"
        if tool in self.privileged and not approved:
            self.audit.append(Decision(tool, dict(args), False, "AWAITING_APPROVAL"))
            return "AWAITING_APPROVAL"
        try:
            result = self.tools[tool](**args)
        except (TypeError, ValueError) as exc:
            outcome = f"ERROR:{type(exc).__name__}"
        else:
            outcome = str(result)
        self.audit.append(Decision(tool, dict(args), approved, outcome))
        return outcome

def read_status(service: str) -> str:
    return f"DEMO:{service}:DEGRADED"

def restart_mock(service: str) -> str:
    return f"SIMULATED_RESTART:{service}"

def example_agent() -> Agent:
    return Agent({"read_status": read_status, "restart_mock": restart_mock},
                 privileged={"restart_mock"})

if __name__ == "__main__":
    agent = example_agent()
    print(agent.execute("read_status", {"service": "demo-gateway"}))
    print(agent.execute("restart_mock", {"service": "demo-gateway"}))
    print(agent.execute("restart_mock", {"service": "demo-gateway"}, approved=True))
    print(agent.audit)
