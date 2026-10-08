    function saveFormAsTxt() {
    // 1. Get values from form elements    
    const baseDir = document.getElementById('d1').value;
    const secondDir = document.getElementById('d2').value;
    const contentDir = document.getElementById('d3').value;
    const title = document.getElementById('t').value;
    const pages = document.getElementById('p').value;
    const height = document.getElementById('h').value;
    const width = document.getElementById('w').value;
    const baseFilename = document.getElementById('b').value;
    
    // 2. Format as string
    const data = `[DIRECTORIES]\nBaseDirectory = ${baseDir}\nSecondDirectory = ${secondDir}\nContentDirectory = ${contentDir}\n\n[INFORMATION]\nTitle = ${title}\nPages = ${pages}\nHeight = ${height}\nWidth = ${width}\nBase = ${baseFilename}`;
    
    // 3. Create Blob
    const blob = new Blob([data], { type: 'text/plain' });
    
    // 4. Create download link
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'config.ini';
    document.body.appendChild(a);
    a.click();
    
    // 5. Cleanup
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}   