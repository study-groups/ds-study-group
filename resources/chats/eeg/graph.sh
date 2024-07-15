svg_graph_enhance() {
    # Assuming the SVG file is named 'render_with_links.svg' and located in the current directory
    local svg_file="render_with_links.svg"
    local js_file="wiki_links.js"
    local html_file="index.html"
    local titles=(
        "Electroencephalography"
        "Spectral_power_distribution"
        "Spectral_density#Spectral_power_density"
        "Complex_system"
        "Alpha_wave"
        "1/f_noise"
        "Electroencephalography#Alpha_wave"
        "Lempel–Ziv_complexity"
        "Pathology"
        "Diagnosis"
        "Etiology"
        "Hypoxia_(medical)"
        "Brain_injury"
        "Generalization"
    )
    local urls=(
        "https://en.wikipedia.org/wiki/Electroencephalography"
        "https://en.wikipedia.org/wiki/Spectral_power_distribution"
        "https://en.wikipedia.org/wiki/Spectral_density#Spectral_power_density"
        "https://en.wikipedia.org/wiki/Complex_system"
        "https://en.wikipedia.org/wiki/Alpha_wave"
        "https://en.wikipedia.org/wiki/1/f_noise"
        "https://en.wikipedia.org/wiki/Electroencephalography#Alpha_wave"
        "https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv_complexity"
        "https://en.wikipedia.org/wiki/Pathology"
        "https://en.wikipedia.org/wiki/Diagnosis"
        "https://en.wikipedia.org/wiki/Etiology"
        "https://en.wikipedia.org/wiki/Hypoxia_(medical)"
        "https://en.wikipedia.org/wiki/Brain_injury"
        "https://en.wikipedia.org/wiki/Generalization"
    )

    # Generate JS file mapping IDs to URLs
    echo "const wikiLinks = {" > "$js_file"
    for i in "${!titles[@]}"; do
        echo "  \"$i\": \"${urls[$i]}\"," >> "$js_file"
    done
    echo "};" >> "$js_file"

    # Generate HTML file
    cat <<EOF > "$html_file"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Interactive SVG with Wikipedia Links</title>
    <link rel="stylesheet" href="style.css">
    <script src="$js_file"></script>
    <script defer src="fetchSummary.js"></script>
</head>
<body>
    <h1>EEG Markers of Consciousness in Unresponsive Patients</h1>
    <object type="image/svg+xml" data="$svg_file" id="svgObject"></object>
    <div id="popup" class="popup" style="display: none;"></div>
</body>
</html>
EOF

    echo "Generated HTML and JS files for interactive SVG."
}

