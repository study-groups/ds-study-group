// Ensure the document is fully loaded before executing any script
document.addEventListener('DOMContentLoaded', function() {
    // Access the SVG object in the DOM
    const svgObject = document.getElementById('svgObject');
    if (!svgObject) {
        console.error('SVG object not found');
        return;
    }

    // Wait for the SVG content to fully load
    svgObject.addEventListener('load', function() {
        const svgDoc = svgObject.contentDocument;
        if (!svgDoc) {
            console.error('Failed to load SVG document');
            return;
        }

        // Attach mouseenter event listeners to elements that have corresponding Wikipedia links
        Object.keys(wikiLinks).forEach(function(key) {
            const element = svgDoc.getElementById(key);
            if (element) {
                element.addEventListener('mouseenter', function(event) {
                    fetchSummary(wikiLinks[key], event);
                });
            } else {
                console.warn(`Element with ID ${key} not found in SVG.`);
            }
        });
    });
});

// Fetches the summary from Wikipedia and displays it in a popup
async function fetchSummary(title, event) {
    const url = `https://en.wikipedia.org/api/rest_v1/page/summary/${title}`;
    const popup = document.getElementById('popup');
    if (!popup) {
        console.error('Popup element not found');
        return;
    }

    try {
        const response = await fetch(url);
        // Handle HTTP errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();

        // Only display the popup if a summary is available
        if (data.extract) {
            popup.innerHTML = data.extract;
            popup.style.display = 'block';
            // Ensure the popup position is updated with respect to the event's page coordinates
            updatePopupPosition(event, popup);
        }
    } catch (error) {
        console.error('Error fetching summary:', error);
    }
}

// Updates the position of the popup based on mouse coordinates
function updatePopupPosition(event, popup) {
    let x = event.pageX + 20; // Offset to prevent the cursor from covering the popup
    let y = event.pageY;

    // Adjustments to keep the popup within the viewport
    const popupRect = popup.getBoundingClientRect();
    const maxX = window.innerWidth - popupRect.width - 20; // 20px for margin
    const maxY = window.innerHeight - popupRect.height - 20;

    if (x > maxX) x = maxX;
    if (y > maxY) y = maxY;

    popup.style.left = `${x}px`;
    popup.style.top = `${y}px`;
}

// Update popup position on mouse move, only if the popup is visible
document.addEventListener('mousemove', function(e) {
    const popup = document.getElementById('popup');
    if (popup && popup.style.display === 'block') {
        updatePopupPosition(e, popup);
    }
});

// Hide the popup when the mouse leaves the SVG area
document.addEventListener('mouseleave', function() {
    const popup = document.getElementById('popup');
    if (popup) {
        popup.style.display = 'none';
    }
});
