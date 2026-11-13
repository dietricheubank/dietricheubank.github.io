"""Standard-library-only synthetic LLM request monitoring endpoint."""
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, HTTPServer

@dataclass
class Metrics:
    requests: int = 0
    errors: int = 0
    total_latency_ms: float = 0
    observations: list[float] = field(default_factory=list)

    def record(self, latency_ms: float, status: int) -> None:
        if latency_ms < 0 or not 100 <= status <= 599:
            raise ValueError("invalid observation")
        self.requests += 1
        self.errors += int(status >= 500)
        self.total_latency_ms += latency_ms
        self.observations.append(latency_ms)

    def prometheus(self) -> str:
        return (f"# TYPE demo_llm_requests_total counter\ndemo_llm_requests_total {self.requests}\n"
                f"# TYPE demo_llm_errors_total counter\ndemo_llm_errors_total {self.errors}\n"
                f"# TYPE demo_llm_latency_ms_sum counter\ndemo_llm_latency_ms_sum {self.total_latency_ms}\n"
                f"# TYPE demo_llm_latency_ms_count counter\ndemo_llm_latency_ms_count {self.requests}\n")

def serve(port: int = 9108) -> None:
    metrics = Metrics()
    for latency, status in [(120, 200), (200, 200), (900, 503)]:
        metrics.record(latency, status)
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path != "/metrics":
                self.send_error(404)
                return
            body = metrics.prometheus().encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
    print(f"Serving synthetic /metrics on 127.0.0.1:{port}")
    HTTPServer(("127.0.0.1", port), Handler).serve_forever()

if __name__ == "__main__":
    serve()
