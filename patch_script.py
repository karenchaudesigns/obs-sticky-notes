import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove dock-btn-add-note
old_header = '''      <div class="flex items-center gap-2">
        <button id="dock-btn-add-note" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 active:bg-indigo-700 text-white text-xs font-semibold rounded-lg flex items-center gap-1.5 shadow-sm transition-colors">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
          New Note
        </button>
        <button id="dock-btn-switch-overlay" class="px-3 py-1.5 bg-zinc-800 hover:bg-zinc-700 text-zinc-200 text-xs font-semibold rounded-lg flex items-center gap-1.5 border border-zinc-700 transition-colors" title="Preview Overlay Canvas">'''

new_header = '''      <div class="flex items-center gap-2">
        <button id="dock-btn-switch-overlay" class="px-3 py-1.5 bg-zinc-800 hover:bg-zinc-700 text-zinc-200 text-xs font-semibold rounded-lg flex items-center gap-1.5 border border-zinc-700 transition-colors" title="Preview Overlay Canvas">'''

content = content.replace(old_header, new_header)

# Replace the interactive preview
old_preview = '''        <!-- Interactive Preview -->
        <div id="dock-preview-container" class="relative w-full aspect-video bg-zinc-900 border border-zinc-800 rounded-xl overflow-hidden shadow-sm flex-shrink-0">
          <div id="dock-preview-canvas" class="absolute top-0 left-0 origin-top-left w-[1920px] h-[1080px] pointer-events-auto"></div>
        </div>'''

new_preview = '''        <!-- Interactive Preview & Memo Pads -->
        <div class="flex gap-4 items-start w-full">
          <div id="dock-preview-container" class="relative flex-1 aspect-video bg-zinc-900 border border-zinc-800 rounded-xl overflow-hidden shadow-sm flex-shrink-0">
            <div id="dock-preview-canvas" class="absolute top-0 left-0 origin-top-left w-[1920px] h-[1080px] pointer-events-auto"></div>
          </div>

          <!-- Memo Pads Panel -->
          <div id="memo-pads-panel" class="w-16 flex-shrink-0 bg-zinc-900 border border-zinc-800 rounded-xl p-2 flex flex-col items-center gap-3 shadow-sm h-full">
            <div class="text-[10px] font-bold text-zinc-500 uppercase tracking-wider text-center w-full border-b border-zinc-800 pb-2 mb-1">Pads</div>
            <div class="memo-pad-option w-10 h-10 rounded shadow-md cursor-grab active:cursor-grabbing hover:scale-105 transition-transform" draggable="true" data-preset="classic-yellow" style="background-color: #FFF740;" title="Yellow"></div>
            <div class="memo-pad-option w-10 h-10 rounded shadow-md cursor-grab active:cursor-grabbing hover:scale-105 transition-transform" draggable="true" data-preset="soft-pink" style="background-color: #FF7EB9;" title="Pink"></div>
            <div class="memo-pad-option w-10 h-10 rounded shadow-md cursor-grab active:cursor-grabbing hover:scale-105 transition-transform" draggable="true" data-preset="pastel-cyan" style="background-color: #7AFCFF;" title="Cyan"></div>
            <div class="memo-pad-option w-10 h-10 rounded shadow-md cursor-grab active:cursor-grabbing hover:scale-105 transition-transform" draggable="true" data-preset="mint-green" style="background-color: #6bf178;" title="Green"></div>
          </div>
        </div>'''

content = content.replace(old_preview, new_preview)

# Update addNewNote function signature and behavior
old_add = '''    function addNewNote() {
      const id = 'note-' + Date.now();
      const randomPreset = BACKGROUND_PRESETS[Math.floor(Math.random() * BACKGROUND_PRESETS.length)];
      const maxZIndex = appState.notes.reduce((max, note) => Math.max(max, note.zIndex || 0), 0);
      const newNote = {
        id: id,
        mode: 'text',
        text: 'New Stream Task\\nClick Dock to edit details!',
        tasks: [{ id: 't_' + Date.now(), text: 'New Stream Task', done: false }],
        completed: false,
        visible: true,
          visible: true,
        x: 80 + (appState.notes.length * 30) % 400,
        y: 80 + (appState.notes.length * 25) % 300,'''

new_add = '''    function addNewNote(options = {}) {
      const id = 'note-' + Date.now();
      const presetId = options.presetId || BACKGROUND_PRESETS[Math.floor(Math.random() * BACKGROUND_PRESETS.length)].id;
      const preset = BACKGROUND_PRESETS.find(p => p.id === presetId) || BACKGROUND_PRESETS[0];
      const maxZIndex = appState.notes.reduce((max, note) => Math.max(max, note.zIndex || 0), 0);
      const newNote = {
        id: id,
        mode: 'text',
        text: 'New Stream Task\\nClick Dock to edit details!',
        tasks: [{ id: 't_' + Date.now(), text: 'New Stream Task', done: false }],
        completed: false,
        visible: true,
        x: options.x !== undefined ? options.x : 80 + (appState.notes.length * 30) % 400,
        y: options.y !== undefined ? options.y : 80 + (appState.notes.length * 25) % 300,'''

content = content.replace(old_add, new_add)

old_add2 = '''        zIndex: maxZIndex + 1,
        bgPresetId: randomPreset.id,
        customBgUrl: '',
        customBgFilter: 'none',
        customBgFilterStrength: 100,
        fontFamily: 'font-handwriting',
        fontSize: 22,
        fontColor: randomPreset.textColor,

        fitText: false,
          fitText: false,'''

new_add2 = '''        zIndex: maxZIndex + 1,
        bgPresetId: preset.id,
        customBgUrl: '',
        customBgFilter: 'none',
        customBgFilterStrength: 100,
        fontFamily: 'font-handwriting',
        fontSize: 22,
        fontColor: preset.textColor,
        fitText: false,'''

content = content.replace(old_add2, new_add2)

# Remove btnDockAdd event listener and add new ones
old_listeners = '''      const btnDockAdd = document.getElementById('dock-btn-add-note');'''

new_listeners = '''      // Add note functionality for drag/drop logic on memo pads
      const memoPads = document.querySelectorAll('.memo-pad-option');
      memoPads.forEach(pad => {
        pad.addEventListener('click', (e) => {
          addNewNote({ presetId: e.target.getAttribute('data-preset') });
        });
        pad.addEventListener('dragstart', (e) => {
          e.dataTransfer.setData('text/plain', e.target.getAttribute('data-preset'));
          e.dataTransfer.effectAllowed = 'copy';
        });
      });

      const dockCanvas = document.getElementById('dock-preview-canvas');
      if (dockCanvas) {
        dockCanvas.addEventListener('dragover', (e) => {
          e.preventDefault();
          e.dataTransfer.dropEffect = 'copy';
        });
        dockCanvas.addEventListener('drop', (e) => {
          e.preventDefault();
          const presetId = e.dataTransfer.getData('text/plain');
          if (presetId) {
            const rect = dockCanvas.getBoundingClientRect();
            let x = (e.clientX - rect.left) / dockPreviewScale;
            let y = (e.clientY - rect.top) / dockPreviewScale;

            // Adjust to center the note on drop (default note size is 260x260)
            x = x - (260 / 2);
            y = y - (260 / 2);

            addNewNote({ presetId, x, y });
          }
        });
      }'''

content = content.replace(old_listeners, new_listeners)

# Also remove btnDockAdd.addEventListener('click', addNewNote);
old_click_listener = '''      if (btnDockAdd) {
        btnDockAdd.addEventListener('click', addNewNote);
      }'''

content = content.replace(old_click_listener, '')

with open('index.html', 'w') as f:
    f.write(content)

print("Patch applied successfully.")
