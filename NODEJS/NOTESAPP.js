const fs = require('fs');
const path = require('path');


// Path of our notes storage file
const notesFile = path.join(__dirname, 'notes.json');

// Utility: Load notes from JSON file
function loadNotes() {
    try {
        if (!fs.existsSync(notesFile)) {
            fs.writeFileSync(notesFile, JSON.stringify([]));
        }
        const data = fs.readFileSync(notesFile, 'utf8');
        return JSON.parse(data);
    }   catch(err) {
        console.err("Error loading notes", err);
        return [];
    }
}

// Utility: Save notes to JSON file
function saveNotes(notes) {
    try {
        fs.writeFileSync(notesFile, JSON.stringify(notes, null, 2));
    } catch (err) {
        console.error("Error Saving notes", err);
    }
}

// Command functions -------------------------------

// Add note
function addNote(text) {
    const notes = loadNotes();

    if(notes.some(n => n.text === text)) {
        console.log("NOte already exists");
        return;
    }

    notes.push({text});
    saveNotes(notes);

    console.log(`Note added: "${text}"`);
}

// List notes
function listNotes() {
    const notes = loadNotes();

    if (notes.length === 0) {
        console.log("No notes found");
        return;
    }

    console.log("Your Notes:");
    notes.forEach((n,i) => console.log(`${i+1}. ${n.text}`));
}

// Read a specific note
function readNote(text) {
    const notes = loadNotes();
    const note = notes.find(n => n.text === text);

    if(!note) {
        console.log(`Node not found: "${text}"`);
        return;
    }

    console.log(`"${node.text}"`);
}

//Remove a note
function removeNote(text){
    let notes = loadNotes();
    const newNotes = notes.filter(n => n.text !== text);

    if(notes.length === newNotes.length) {
        console.log(`Note not found: "${text}"`);
        return;
    }

    saveNotes(newNotes);
    console.log(`Note removed: "${text}"`);
}

// Parse command from command line
const [, , command, ...rest] = process.argv;
const input = rest.join(" ");

switch (command) {
    case "add":
        addNote(input);
        break;

    case "list":
        listNotes();
        break;
    
    case "read":
        readNote(input);
        break;

    case "remove":
        removeNote(input);
        break;
    
    default:
        console.log(`
    Usage:
        node notes.js add "Your note"
        node notes.js list
        node notes.js read "Your note"
        node notes.js remove "Your note"
        `);
}
