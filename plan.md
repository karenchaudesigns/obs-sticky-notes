1. **Explore `index.html`**: Locate the `attachNoteInteractions` function where drag and drop functionality is implemented for sticky notes.
2. **Add Event Listener**: Implement a `wheel` event listener on the `element` to handle mouse scroll events.
3. **Calculate New Dimensions**: In the event listener, read `e.deltaY` to determine the scroll direction (up for enlarge, down for shrink) and calculate the new width and height by multiplying the current dimensions by a scale factor (e.g. 1.05 / 0.95) or a constant increment. Ensure they do not drop below the minimum size (140px).
4. **Apply New Dimensions**: Update `note.width` and `note.height`, apply them to `element.style`, call `saveState(true)`, and call `syncDockFormIfSelected(note.id)` to synchronize the OBS Dock form.
5. **Complete pre-commit steps**: Run required pre-commit verifications.
6. **Submit**: Once verified, commit the changes with an appropriate message and branch name.
