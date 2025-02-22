// This file combines a few iconify icons into a single JSON file.
// It is NOT used anymore!
const fs = require('fs');

// Define the icons you need from each set
const selectedIcons = {
    "mdi": ['vr', 'file-transfer-outline', 'script-text-outline', 'arrow-left-bold', 'arrow-right-bold', 'linux', 'git', 'debian', 'fedora', 'arch', 'zip-box', 'code', 'tag', 'clock-time-four', 'calendar', 'grid', 'stars', 'cube', 'orbit', 'cloud', 'email', 'rss', 'twitter', 'archive', 'database-outline', 'file-transfer-outline'],
    "fa": ['search', 'apple'],
    "fa-brands": ['creative-commons', 'creative-commons-by', 'creative-commons-nc'],
    "la": ['cubes'],
    "raphael": ['opensource', 'db', 'clouddown', 'search'],
    "clarity": ['objects-solid'],
    "hugeicons": ['satellite-03'],
    "mingcute": ['cube-3d-line', 'pen-fill'],
    "ph": ['graphics-card', 'graph'],
    "ix": ['operating-system'],
    "solar": ['planet-4-bold', 'satellite-bold'],
    "gg": ['smartphone-chip'],
    "streamline": ['galaxy-2-solid'],
    "uil": ['moon-eclipse', 'windows'],
    "tabler": ['badge-3d-filled', 'view-360-number', 'stars', 'home-filled'],
    "gis": ['satellite'],
    "clarity": ['file-zip-line', 'language-solid'],
    "lsicon": ['filter-filled', 'path-filled', 'list-filled'],
    "iconoir": ['gamepad'],
    "ri": ['bluesky-fill', 'mastodon-fill', 'youtube-fill'],
    "majesticons": ['article'],
    "material-symbols": ['box', 'texture'],
    "simple-icons": ['flatpak'],
    "game-icons": ['asteroid', 'mesh-network'],
    "token": ['unix'],

};

const defaultSize = 30;
// Load and extract the icons dynamically
const combinedIcons = [];

for (const [setName, icons] of Object.entries(selectedIcons)) {
    try {
        const iconData = require(`@iconify/json/json/${setName}.json`);
        
        const filteredIcons = {
            prefix: iconData.prefix,
            icons: {}
        };

        icons.forEach(icon => {
            if (iconData.icons[icon]) {
                const iconDetails = iconData.icons[icon];

                if (!iconDetails.hasOwnProperty('width')) {
                    iconDetails.width = defaultSize;
                }
                if (!iconDetails.hasOwnProperty('height')) {
                    iconDetails.height = defaultSize;
                }

                filteredIcons.icons[icon] = iconDetails;
            }
        });

        combinedIcons.push(filteredIcons);
    } catch (error) {
        console.error(`❌ Error loading icon set "${setName}": ${error.message}`);
    }
}


// Save to a JSON file
fs.writeFileSync('custom-icons.json', JSON.stringify(combinedIcons));

console.log('✅ Generated icons.json with selected icons.');
