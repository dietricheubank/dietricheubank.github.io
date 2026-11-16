"use strict";
const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

function element(value = "") {
  return {
    value: String(value), textContent: "", className: "", listeners: {},
    style: { width: "" },
    addEventListener(type, fn) { this.listeners[type] = fn; }
  };
}

function boot() {
  const initial = { fleet: 1200, done: 275, capacity: 72, blockers: 2, tested: 88, health: 97 };
  const nodes = Object.fromEntries([
    ...Object.entries(initial).map(([key, value]) => [key, element(value)]),
    ...["percent", "remaining", "duration", "decision", "bar", "brief", "reset", "print"]
      .map(key => [key, element()])
  ]);
  const source = fs.readFileSync(path.join(__dirname, "../lab/clinical-dashboard.js"), "utf8");
  vm.runInNewContext(source, { document: { getElementById: id => nodes[id] }, print() {} },
    { filename: "clinical-dashboard.js" });
  function change(id, value) {
    nodes[id].value = String(value);
    nodes[id].listeners.input();
  }
  return { nodes, change };
}

test("default scenario shows correct progress, capacity and conservative hold", () => {
  const { nodes } = boot();
  assert.equal(nodes.percent.textContent, "22.9%");
  assert.equal(nodes.remaining.textContent, "925");
  assert.equal(nodes.duration.textContent, 13);
  assert.equal(nodes.decision.textContent, "HOLD");
  assert.equal(nodes.bar.style.width, (100 * 275 / 1200) + "%");
});

test("readiness threshold allows review but still requires clinical authorization", () => {
  const { nodes, change } = boot();
  change("blockers", 0);
  change("tested", 95);
  change("health", 98);
  assert.equal(nodes.decision.textContent, "REVIEW");
  assert.match(nodes.brief.textContent, /signed clinical acceptance/);
  change("health", 97.9);
  assert.equal(nodes.decision.textContent, "HOLD");
});

test("invalid and inconsistent inputs never enable review", () => {
  const { nodes, change } = boot();
  change("blockers", 0);
  change("tested", 100);
  change("health", 100);
  change("done", 1201);
  assert.equal(nodes.decision.textContent, "Invalid");
  assert.equal(nodes.remaining.textContent, "—");
  change("done", 1200);
  change("capacity", "");
  assert.equal(nodes.decision.textContent, "Invalid");
  change("capacity", 0);
  assert.equal(nodes.decision.textContent, "Invalid");
});

test("completed rollout has zero remaining weeks and resets to baseline", () => {
  const { nodes, change } = boot();
  change("done", 1200);
  assert.equal(nodes.percent.textContent, "100.0%");
  assert.equal(nodes.duration.textContent, 0);
  nodes.reset.onclick();
  assert.equal(nodes.done.value, 275);
  assert.equal(nodes.blockers.value, 2);
  assert.equal(nodes.decision.textContent, "HOLD");
});
