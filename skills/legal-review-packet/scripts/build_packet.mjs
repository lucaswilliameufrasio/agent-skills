// Builds one A4 PDF from a cover and Markdown drafts for legal review.
// Usage: node build_packet.mjs --out packet.pdf --cover cover.md a.md b.md
// Needs `marked` and a Playwright Chromium (`playwright` or `@playwright/test`)
// resolvable from the current directory.
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { resolve } from "node:path";

const require = createRequire(resolve(process.cwd(), "noop.js"));
const load = (names) => {
  for (const name of names) {
    try {
      return require(name);
    } catch {
      // try the next package name
    }
  }
  throw new Error(`install one of: ${names.join(", ")} in the current project`);
};
const { marked } = load(["marked"]);
const { chromium } = load(["playwright", "@playwright/test"]);

const args = process.argv.slice(2);
let out;
let cover;
const files = [];
for (let index = 0; index < args.length; index += 1) {
  if (args[index] === "--out") {
    out = args[++index];
  } else if (args[index] === "--cover") {
    cover = args[++index];
  } else {
    files.push(args[index]);
  }
}
if (!out || (!cover && files.length === 0)) {
  console.error("usage: node build_packet.mjs --out packet.pdf --cover cover.md [drafts.md ...]");
  process.exit(2);
}

const clean = (text) =>
  text
    .replace(/^---\n[\s\S]*?\n---\n/, "")
    // Relative links do not work outside the repository: keep the text.
    .replace(/\[([^\]]+)\]\((?!https?:)[^)]+\)/g, "$1");
const parts = [cover, ...files].filter(Boolean).map((file) => marked.parse(clean(readFileSync(file, "utf8"))));
const html = `<!doctype html><html><meta charset="utf-8"><style>
body{font-family:system-ui,sans-serif;font-size:11.5pt;line-height:1.5;color:#111;max-width:46rem;margin:auto}
h1{font-size:18pt}h2{font-size:14pt;margin-top:1.4em}h3{font-size:12pt}
blockquote{border-left:3px solid #999;margin:0;padding-left:1em;color:#444}
code{font-size:10pt}table{border-collapse:collapse}td,th{border:1px solid #bbb;padding:4px 6px;vertical-align:top}
.page{page-break-before:always}</style><body>${parts
  .map((part, index) => (index === 0 ? part : `<div class="page">${part}</div>`))
  .join("")}</body></html>`;

const browser = await chromium.launch();
const page = await browser.newPage();
await page.setContent(html);
await page.pdf({
  path: out,
  format: "A4",
  margin: { top: "18mm", bottom: "18mm", left: "16mm", right: "16mm" }
});
await browser.close();
console.log(`wrote ${out}`);
