1. **Remove Typography & Layout Section from Bottom Panel:**
   - In `index.html`, remove the `Typography & Layout` section from the bottom panel editor. This includes removing the elements for `editor-font-family`, `editor-font-size`, `editor-font-color`, `editor-btn-reset-type`, format buttons (`.format-btn`), alignment buttons (`.align-btn`), and fit text checkbox (`editor-fit-text`).
   - Remove JS code that populates and listens to events on these bottom panel typography elements. (e.g. `document.getElementById('editor-font-family').value = ...`, `document.getElementById('editor-font-size').addEventListener...`)

2. **Add Font and Text Color to Popup Text Editor:**
   - Add `<select>` for font family and `<input type="color">` for text color inside the `#popup-text-editor`.
   - Update `setupEventListeners` and `element.addEventListener('click')` logic in `index.html` to populate and handle changes for the new font family and text color inputs in the popup.
   - We might also need to move the fit-text checkbox to the popup? No, the prompt only asks for "font and text color".

3. **Change L C R Buttons to Have Typical Icons:**
   - The user asked to change the L C R (Left, Center, Right) buttons to have typical icons.
   - Locate `.popup-align-btn` inside `#popup-text-editor`.
   - Replace the text `L`, `C`, `R` with SVG icons representing text alignment (Left, Center, Right).

4. **Verify UI:**
   - Run tests and visually inspect `index.html` via local server to ensure popup behaves as expected and the bottom panel correctly lacks the typography section.

5. **Pre Commit Checks:**
   - Ensure proper testing, verification, review, and reflection are done.

6. **Submit:**
   - Commit and push changes.
