from graphviz import Digraph

dot = Digraph()

dot.node('A', 'EEG Markers of Consciousness in Unresponsive Patients', style='filled', fillcolor='lightblue')
dot.node('B', 'Candidate EEG Features', style='filled', fillcolor='lightgrey')
dot.node('C', 'Spectral Power', style='filled', fillcolor='lightgrey')
dot.node('D', 'Spectral and Spatial Gradients', style='filled', fillcolor='lightgrey')
dot.node('E', 'Signal Complexity', style='filled', fillcolor='lightgrey')

dot.node('F', 'Alpha Power\n(Absolute, Relative, Flattened)', style='filled', fillcolor='lightyellow')
dot.node('G', 'Spectral Exponent', style='filled', fillcolor='lightyellow')
dot.node('H', 'Alpha Posterior-Anterior Ratio (PAR)', style='filled', fillcolor='lightyellow')
dot.node('I', 'Lempel-Ziv Complexity\n(Shuffle-normalized, Phase-normalized)', style='filled', fillcolor='lightyellow')

dot.node('J', 'Etiology-Specific Markers', style='filled', fillcolor='lightgreen')
dot.node('K', 'Diagnostic and Prognostic Value', style='filled', fillcolor='lightgreen')
dot.node('L', 'Etiology-Dependent Differences', style='filled', fillcolor='lightgreen')
dot.node('M', 'Alpha Power Importance in Anoxic Patients', style='filled', fillcolor='lightgreen')
dot.node('N', 'Spectral Exponent Value for Non-anoxic Patients', style='filled', fillcolor='lightgreen')
dot.node('O', 'Lack of Generalization to Other Etiologies', style='filled', fillcolor='lightgreen')

dot.edges(['AB', 'BC', 'BD', 'BE', 'CF', 'DG', 'DH', 'EI', 'BJ', 'JK', 'JL', 'KM', 'KN', 'KO'])
dot.graph_attr['rankdir'] = 'TB'

# Add legend
dot.node('L1', '**EEG**: Electroencephalogram; a test used to evaluate the electrical activity in the brain.', shape='plaintext')
dot.node('L2', '**Anoxic**: Relating to or marked by a lack of oxygen.', shape='plaintext')
dot.node('L3', '**Spectral Power**: The square of the amplitude of the EEG signal for specific frequency bands.', shape='plaintext')
dot.node('L4', '**Spectral Exponent**: A parameter describing the decay of power spectral density with frequency.', shape='plaintext')
dot.node('L5', '**Posterior-Anterior Ratio (PAR)**: A measure comparing the power of EEG signals from the back to the front of the brain.', shape='plaintext')
dot.node('L6', '**Lempel-Ziv Complexity**: A measure of the complexity or randomness of a signal.', shape='plaintext')
dot.node('L7', '**Shuffle-normalized**: Normalization technique involving random shuffling of a data series.', shape='plaintext')
dot.node('L8', '**Phase-normalized**: Normalization technique based on randomizing the phase of a signal while preserving its amplitude spectrum.', shape='plaintext')


# Save the output to an SVG file with legends
output_path_with_legend = "./render.svg"
dot.render(output_path_with_legend, format="svg", cleanup=True)
# Output the dot source and render the SVG
