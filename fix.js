const fs = require('fs');
const html = fs.readFileSync('Portfolio.html', 'utf8');

const updated = html.replace(
    /Mismatch 02 · Leaderboard · Figure A2<\\u002Fspan><span class=\\"i18n-zh\\">失配 02 · 排行榜 · 附图 A2<\\u002Fspan><\\u002Fspan>\\n              <div class=\\"m-screens\\">\\n                <span class=\\"screen-pill\\">Weekly rankings<\\u002Fspan>\\n                <span class=\\"screen-pill\\">XP comparison<\\u002Fspan>\\n                <span class=\\"screen-pill\\">Tier promotion prompt<\\u002Fspan>\\n                <span class=\\"screen-pill\\">Stranger profiles<\\u002Fspan>\\n              <\\u002Fdiv>/,
    'Mismatch 02 · Leaderboard<\\u002Fspan><span class=\\"i18n-zh\\">失配 02 · 排行榜<\\u002Fspan><\\u002Fspan>'
);

if (html !== updated) {
    fs.writeFileSync('Portfolio.html', updated);
    console.log("Updated!");
} else {
    console.log("No match found.");
    
    // Print a bit of context around 'Mismatch 02' if it exists
    const match = html.match(/.{0,50}Mismatch 02.{0,150}/);
    if (match) console.log("Found instead:", match[0]);
}
