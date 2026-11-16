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
    textContent: "", className: "", checked: false,
    children: [], listeners: {},
    append(...children) { this.children.push(...children); },
    addEventListener(type, fn) { this.listeners[type] = fn; },
    set innerHTML(value) { this.children = []; },
  };
}

function boot() {
  const initial = { users: 160, wave: 30, numbers: 92, licenses: 96, tests: 90, support: 90 };
  const nodes = Object.fromEntries(
    [...Object.entries(initial).map(([k, v]) => [k, element(v)]),
      ...["gates", "waves", "eligible", "status", "brief", "reset", "print"].map(k => [k, element()])]
  );
  const document = {
    getElementById: id => nodes[id],
    createElement: () => element(),
    createTextNode: text => ({ textContent: text })
  };
  const source = fs.readFileSync(path.join(__dirname, "../lab/uc-migration.js"), "utf8");
  vm.runInNewContext(source, { document, print() {} }, { filename: "uc-migration.js" });
  const change = (id, value) => {
    nodes[id].value = String(value);
    nodes[id].listeners.input();
  };
  const checkAll = () => {
    for (const label of nodes.gates.children) {
      const checkbox = label.children[0];
      checkbox.checked = true;
      checkbox.onchange();
    }
  };
  return { nodes, change, checkAll };
}

test("default scenario holds and reports overlap bounds", () => {
  const { nodes } = boot();
  assert.equal(nodes.waves.textContent, 6);
  assert.equal(nodes.eligible.textContent, 147);
  assert.equal(nodes.status.textContent, "HOLD");
  assert.match(nodes.brief.textContent, /at least 141/);
});

test("all gates and high readiness enable review", () => {
  const { nodes, change, checkAll } = boot();
  checkAll();
  for (const id of ["numbers", "licenses", "tests", "support"]) change(id, 100);
  assert.equal(nodes.status.textContent, "REVIEW");
  assert.equal(nodes.eligible.textContent, 160);
});

test("missing or invalid values never authorize migration", () => {
  const { nodes, change, checkAll } = boot();
  checkAll();
  for (const id of ["numbers", "licenses", "tests", "support"]) change(id, 100);
  change("wave", 0);
  assert.equal(nodes.status.textContent, "Invalid");
  assert.equal(nodes.waves.textContent, "—");
  change("wave", 30);
  change("numbers", "");
  assert.equal(nodes.status.textContent, "Invalid");
});

test("reset restores the conservative fictional baseline", () => {
  const { nodes, change, checkAll } = boot();
  checkAll();
  change("users", 250);
  nodes.reset.onclick();
  assert.equal(nodes.users.value, 160);
  assert.equal(nodes.status.textContent, "HOLD");
  assert.equal(nodes.gates.children.filter(label => label.children[0].checked).length, 2);
});
