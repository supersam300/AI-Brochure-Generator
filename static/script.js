document.addEventListener('DOMContentLoaded', () => {
    const urlInput = document.getElementById('urlInput');
    const generateBtn = document.getElementById('generateBtn');
    const statusMessage = document.getElementById('statusMessage');
    const resultSection = document.getElementById('resultSection');
    const brochureContent = document.getElementById('brochureContent');
    const copyBtn = document.getElementById('copyBtn');

    generateBtn.addEventListener('click', async () => {
        const url = urlInput.value.trim();
        if (!url) {
            statusMessage.textContent = 'Please enter a valid URL.';
            statusMessage.style.color = '#ef4444';
            return;
        }

        // Reset UI
        statusMessage.textContent = 'Analyzing website and generating brochure... (this may take a moment)';
        statusMessage.style.color = '#94a3b8';
        resultSection.classList.add('hidden');
        generateBtn.disabled = true;
        generateBtn.textContent = 'Processing...';

        try {
            const response = await fetch('/api/brochure', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: url }),
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }

            const data = await response.json();

            // Render Markdown
            brochureContent.innerHTML = marked.parse(data.markdown);

            // Show Result
            resultSection.classList.remove('hidden');
            statusMessage.textContent = 'Brochure generated successfully!';
            statusMessage.style.color = '#10b981';

            // Scroll to result
            resultSection.scrollIntoView({ behavior: 'smooth' });

        } catch (error) {
            console.error('Error:', error);
            statusMessage.textContent = 'Failed to generate brochure. Please check the URL and try again.';
            statusMessage.style.color = '#ef4444';
        } finally {
            generateBtn.disabled = false;
            generateBtn.textContent = 'Generate Brochure';
        }
    });

    copyBtn.addEventListener('click', () => {
        const text = brochureContent.innerText; // or keep raw markdown if stored
        navigator.clipboard.writeText(text).then(() => {
            const originalText = copyBtn.textContent;
            copyBtn.textContent = 'Copied!';
            setTimeout(() => {
                copyBtn.textContent = originalText;
            }, 2000);
        });
    });
});
