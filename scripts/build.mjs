import { cpSync, existsSync, mkdirSync, rmSync } from "node:fs";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";

const root = resolve(import.meta.dirname, "..");
const dist = join(root, "dist");
const check = spawnSync(process.execPath, [join(root, "scripts", "check.mjs")], { stdio: "inherit" });
if (check.status !== 0) process.exit(check.status ?? 1);

rmSync(dist, { recursive: true, force: true });
mkdirSync(join(dist, "server"), { recursive: true });
mkdirSync(join(dist, "client"), { recursive: true });

for (const name of ["index.html", "style.css", "script.js", "images", "work", "resume", "robots.txt"]) {
  const source = join(root, name);
  if (existsSync(source)) cpSync(source, join(dist, "client", name), { recursive: true });
}

const worker = `export default {\n  async fetch(request, env) {\n    if (env && env.ASSETS && typeof env.ASSETS.fetch === "function") return env.ASSETS.fetch(request);\n    return new Response("Portfolio assets are unavailable.", { status: 503 });\n  }\n};\n`;
await import("node:fs/promises").then(({ writeFile }) => writeFile(join(dist, "server", "index.js"), worker));
console.log("Production build created in dist/.");
