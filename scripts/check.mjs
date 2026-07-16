import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";

const root = resolve(import.meta.dirname, "..");
const ignored = new Set(["dist", "node_modules", ".git"]);

function walk(dir) {
  return readdirSync(dir).flatMap((name) => {
    if (ignored.has(name)) return [];
    const path = join(dir, name);
    return statSync(path).isDirectory() ? walk(path) : [path];
  });
}

const htmlFiles = walk(root).filter((file) => file.endsWith(".html"));
const errors = [];
const localTargetPattern = /(?:href|src)="(\/[^"]+)"/g;

for (const file of htmlFiles) {
  const html = readFileSync(file, "utf8");
  if (!/<title>[^<]+<\/title>/.test(html)) errors.push(`${file}: missing title`);
  if (!/<meta name="description" content="[^"]+">/.test(html)) errors.push(`${file}: missing description`);
  if (/[Â�]/.test(html)) errors.push(`${file}: contains encoding artifacts`);
  if (/href="#"/.test(html)) errors.push(`${file}: contains empty hash link`);
  if (!/<main(?:\s|>)/.test(html)) errors.push(`${file}: missing main landmark`);
  if (!/<h1(?:\s|>)/.test(html)) errors.push(`${file}: missing h1`);

  for (const match of html.matchAll(localTargetPattern)) {
    const raw = match[1].split(/[?#]/)[0];
    if (!raw || raw === "/") continue;
    let target = join(root, raw.slice(1));
    if (raw.endsWith("/")) target = join(target, "index.html");
    if (!existsSync(target)) errors.push(`${file}: missing local target ${raw}`);
  }
}

if (!existsSync(join(root, "style.css"))) errors.push("missing style.css");
if (!existsSync(join(root, "script.js"))) errors.push("missing script.js");

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}
console.log(`Checked ${htmlFiles.length} HTML pages: no structural or local-link errors.`);
