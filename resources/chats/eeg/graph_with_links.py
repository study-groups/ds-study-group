from graphviz import Digraph

dot = Digraph()

# Define URLs for each topic
urls = {
    'A': "https://en.wikipedia.org/wiki/Electroencephalography",
    'C': "https://en.wikipedia.org/wiki/Spectral_power_distribution",
    'D': "https://en.wikipedia.org/wiki/Spectral_density#Spectral_power_density",
    'E': "https://en.wikipedia.org/wiki/Complex_system",
    'F': "https://en.wikipedia.org/wiki/Alpha_wave",
    'G': "https://en.wikipedia.org/wiki/1/f_noise",
    'H': "https://en.wikipedia.org/wiki/Electroencephalography#Alpha_wave",
    'I': "https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv_complexity",
    'J': "https://en.wikipedia.org/wiki/Pathology",
    'K': "https://en.wikipedia.org/wiki/Diagnosis",
    'L': "https://en.wikipedia.org/wiki/Etiology",
    'M': "https://en.wikipedia.org/wiki/Hypoxia_(medical)",
    'N': "https://en.wikipedia.org/wiki/Brain_injury",
    'O': "https://en.wikipedia.org/wiki/Generalization"
}

# Adding nodes with URLs
dot.node('A', 'EEG Markers of Consciousness in Unresponsive Patients', style='filled', fillcolor='lightblue', URL=urls['A'])
dot.node('B', 'Candidate EEG Features', style='filled', fillcolor='lightgrey')
dot.node('C', 'Spectral Power', style='filled', fillcolor='lightgrey', URL=urls['C'])
dot.node('D', 'Spectral and Spatial Gradients', style='filled', fillcolor='lightgrey', URL=urls['D'])
dot.node('E', 'Signal Complexity', style='filled', fillcolor='lightgrey', URL=urls['E'])

dot.node('F', 'Alpha Power\n(Absolute, Relative, Flattened)', style='filled', fillcolor='lightyellow', URL=urls['F'])
dot.node('G', 'Spectral Exponent', style='filled', fillcolor='lightyellow', URL=urls['G'])
dot.node('H', 'Alpha Posterior-Anterior Ratio (PAR)', style='filled', fillcolor='lightyellow', URL=urls['H'])
dot.node('I', 'Lempel-Ziv Complexity\n(Shuffle-normalized, Phase-normalized)', style='filled', fillcolor='lightyellow', URL=urls['I'])

dot.node('J', 'Etiology-Specific Markers', style='filled', fillcolor='lightgreen', URL=urls['J'])
dot.node('K', 'Diagnostic and Prognostic Value', style='filled', fillcolor='lightgreen', URL=urls['K'])
dot.node('L', 'Etiology-Dependent Differences', style='filled', fillcolor='lightgreen', URL=urls['L'])
dot.node('M', 'Alpha Power Importance in Anoxic Patients', style='filled', fillcolor='lightgreen', URL=urls['M'])
dot.node('N', 'Spectral Exponent Value for Non-anoxic Patients', style='filled', fillcolor='lightgreen', URL=urls['N'])
dot.node('O', 'Lack of Generalization to Other Etiologies', style='filled', fillcolor='lightgreen', URL=urls['O'])

dot.edges(['AB', 'BC', 'BD', 'BE', 'CF', 'DG', 'DH', 'EI', 'BJ', 'JK', 'JL', 'KM', 'KN', 'KO'])

# Since legend nodes don't directly relate to a single URL, they're not linked
# To add helpful annotations, consider doing so in the HTML or documentation accompanying the SVG

import json
with open('wikiLinks.js', 'w') as f:
    f.write('const wikiLinks = ')
    json.dump(urls, f, indent=4)

# ... existing code ...

output_path_with_legend = "render_with_links"
dot.render(output_path_with_legend, format="svg", cleanup=True)
