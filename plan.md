1. **Close popup when note loses focus**:
   - Modify the `handleCanvasPointerDown` function (around line 2193) or `currentSelectedNoteId = null` block to also hide the popup editor: `document.getElementById('popup-text-editor').classList.add('hidden');`.
   - Also check where selection changes to another note, so if we click another note, we should also hide the popup if it was open for the old note? The issue says "when a sticky note loses focus (i.e. is deselected), close the popup text editor". Currently, it seems we also want to hide it when the user clicks the canvas background. Wait, if the user clicks another note, the focus changes to that note, and we either open the popup or at least we should close the current one if it was open.
     Wait, in the dock mode, when a note loses focus it triggers `currentSelectedNoteId = null`. When we click another note, `previousSelectedId !== currentSelectedNoteId`. We can just hide the popup whenever `currentSelectedNoteId` changes or is set to null, OR just when it's set to null. The requirements: "when a sticky note loses focus (i.e. is deselected), close the popup text editor."
     - Let's add a check in `handleCanvasPointerDown`:
       ```javascript
       if (e.target.id === 'notes-canvas' || e.target.id === 'dock-preview-canvas' || e.target.id === 'overlay-container' || e.target.id === 'dock-preview-container') {
         currentSelectedNoteId = null;
         updateSelectionIndicators();
         document.getElementById('popup-text-editor').classList.add('hidden');
         // ...
       ```
     - And what if another note is selected? `currentSelectedNoteId` changes. The popup should also close.
       ```javascript
         const previousSelectedId = currentSelectedNoteId;
         currentSelectedNoteId = note.id;
         updateSelectionIndicators();
         if (previousSelectedId !== currentSelectedNoteId) {
             document.getElementById('popup-text-editor').classList.add('hidden');
         }
       ```

2. **Reposition the popup text editor**:
   - The popup text editor (`<div id="popup-text-editor">`) should be draggable so the user can reposition it.
   - We can implement dragging logic for the popup, similar to how the note is draggable.
   - Add a header/handle to the popup for dragging, or just make the top part (or the whole container minus inputs) draggable.
   - Let's look at the HTML for `popup-text-editor`.
     ```html
     <div id="popup-text-editor" class="hidden absolute z-50 bg-zinc-900 border border-zinc-700 rounded-lg shadow-2xl p-3" style="width: 300px;">
       <div class="flex justify-between items-center mb-2" id="popup-header" style="cursor: grab;">
          <!-- header contents -->
       </div>
       <!-- ... -->
     </div>
     ```
   - We will need to attach pointer down/move/up events to the popup header to drag it around.
   - Variables for drag state: `isDraggingPopup = false`, `popupStartX`, `popupStartY`, `popupInitialLeft`, `popupInitialTop`.

3. **Pre-commit instructions**:
   - Always run pre-commit tests and verify changes before submitting.
