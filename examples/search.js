// GET /v1/search. Change the values below, then run it.
//
// Needs Node 18 or newer. From the repo folder:
//     node examples/search.js

const API = "https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod";
const KEY = "dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD";

const QUERY = "cinematic";
const DURATION = "30-120"; // 0-30, 30-120, 120-240, 240-480
const CONTENT = "human"; // all, human, ai
const ORDER = "latest"; // relevant, latest, editors_choice

async function main() {
  const params = new URLSearchParams({
    q: QUERY,
    duration: DURATION,
    content: CONTENT,
    order: ORDER,
  });
  const response = await fetch(`${API}/v1/search?${params}`, {
    headers: { "x-api-key": KEY },
  });
  if (!response.ok) {
    throw new Error(`${response.status} ${await response.text()}`);
  }
  const data = await response.json();
  console.log(data.total, "tracks, page", data.page, "of", data.pages);
  for (const track of data.tracks) {
    console.log(
      String(track.id).padStart(8),
      String(track.duration).padStart(7),
      "views",
      String(track.stats.views).padEnd(6),
      track.name,
    );
  }
}

main().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
