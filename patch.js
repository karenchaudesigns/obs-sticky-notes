const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const target = `
        currentSelectedNoteId = note.id;
        updateSelectionIndicators();

        // Bring to front
`;

const replacement = `
        const previousSelectedId = currentSelectedNoteId;
        currentSelectedNoteId = note.id;
        updateSelectionIndicators();

        if (currentViewMode === 'dock' && previousSelectedId !== currentSelectedNoteId) {
          populateEditorForm();
          renderDockView();
        }

        // Bring to front
`;

html = html.replace(target, replacement);
fs.writeFileSync('index.html', html);
