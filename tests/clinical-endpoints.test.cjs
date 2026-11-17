"use strict";
const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

function element(value = "") {
  return {
    _value: String(value),
    get value() { return this._value; },
    set value(next) { this._value = String(next); },
    textContent: "", checked: false, children: [], listeners: {},
    append(...items) { this.children.push(...items); },
    addEventListener(event, callback) { this.listeners[event] = callback; },
    set innerHTML(_) { this.children = []; }
  };
}
function boot() {
  const inputs = { mix: "balanced", devices: 1200, rate: 24, teams: 3, pilot: 60 };
  const nodes = Object.fromEntries([
    ...Object.entries(inputs).map(([id, value]) => [id, element(value)]),
    ...["gates", "shared", "assigned", "weeks", "status", "waves", "narrative", "reset", "print"].map(id => [id, element()])
  ]);
  const document = {
    getElementById: id => nodes[id],
    createElement: () => element(),
    createTextNode: value => ({ textContent: value })
  };
  const source = fs.readFileSync(path.join(__dirname, "../lab/clinical-endpoints.js"), "utf8");
  vm.runInNewContext(source, { document, window: { print() {} } }, { filename: "clinical-endpoints.js" });
  function change(id, value) { nodes[id].value = value; nodes[id].listeners.change(); }
  function checkAll() {
    for (const label of nodes.gates.children) {
      const check = label.children[0];
      check.checked = true;
      check.onchange();
    }
  }
  return { nodes, change, checkAll };
}
test("default model shows a conservative hold and consistent migration waves", () => {
  const { nodes } = boot();
  assert.equal(nodes.shared.textContent, "600");
  assert.equal(nodes.assigned.textContent, "600");
  assert.equal(nodes.weeks.textContent, 16);
  assert.equal(nodes.waves.children.length, 16);
  assert.equal(nodes.status.textContent, "HOLD");
});
test("configuration mix and validation gates update the recommendation", () => {
  const { nodes, change, checkAll } = boot();
  change("mix", "shared");
  assert.equal(nodes.shared.textContent, "900");
  checkAll();
  assert.equal(nodes.status.textContent, "Pilot gate met");
  assert.match(nodes.narrative.textContent, /signed clinical go\/no-go/);
});
test("invalid inputs do not produce a rollout or readiness approval", () => {
  const { nodes, change, checkAll } = boot();
  checkAll();
  change("pilot", 1200);
  assert.equal(nodes.status.textContent, "Check inputs");
  assert.equal(nodes.waves.children.length, 0);
  change("pilot", 60);
  change("rate", "");
  assert.equal(nodes.status.textContent, "Check inputs");
});
test("low-capacity scenarios show every wave rather than truncating at 300", () => {
  const { nodes, change } = boot();
  change("devices", 402);
  change("pilot", 100);
  change("rate", 1);
  change("teams", 1);
  assert.equal(nodes.weeks.textContent, 302);
  assert.equal(nodes.waves.children.length, 302);
  const last = nodes.waves.children.at(-1).children;
  assert.equal(last[0].textContent, "Wave 302");
  assert.equal(last[1].textContent, "1");
});
test("reset restores the fictional baseline and conservative gates", () => {
  const { nodes, change, checkAll } = boot();
  checkAll();
  change("devices", 500);
  nodes.reset.onclick();
  assert.equal(nodes.devices.value, "1200");
  assert.equal(nodes.status.textContent, "HOLD");
  assert.equal(nodes.gates.children.filter(label => label.children[0].checked).length, 2);
});
