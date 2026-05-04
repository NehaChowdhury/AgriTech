document.addEventListener('DOMContentLoaded', () => {
    /**
     * Scroll Reveal Animation Engine
     * Efficiently toggles visibility based on scroll position
     */
    const initReveal = () => {
        const reveals = document.querySelectorAll('.reveal');
        const revealOnScroll = () => {
            const triggerBottom = (window.innerHeight / 5) * 4;
            reveals.forEach(box => {
                const boxTop = box.getBoundingClientRect().top;
                if (boxTop < triggerBottom) {
                    box.classList.add('active');
                }
            });
        };
        window.addEventListener('scroll', revealOnScroll);
        revealOnScroll(); // Trigger once on load
    };

    initReveal();

    /**
     * Generic API Request Handler
     * Reduces code duplication and handles errors globally
     */
    const handlePrediction = async (formId, endpoint, resultDivId, resultHandler) => {
        const form = document.getElementById(formId);
        if (!form) return;

        const resultDiv = document.getElementById(resultDivId);
        const submitBtn = form.querySelector('button[type="submit"]');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // UI State: Loading
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Processing...';
            resultDiv.classList.add('hidden');

            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch(endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });

                const result = await response.json();

                if (response.ok) {
                    resultHandler(result);
                    resultDiv.classList.remove('hidden');
                    // Smooth scroll to result
                    setTimeout(() => {
                        resultDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }, 100);
                } else {
                    alert(result.error || 'Server error. Please check your inputs.');
                }
            } catch (err) {
                console.error('API Error:', err);
                alert('Connection error. Please ensure the backend is running.');
            } finally {
                // UI State: Reset
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            }
        });
    };

    // Initialize Crop Prediction
    handlePrediction(
        'crop-form', 
        '/predict-crop', 
        'crop-result', 
        (res) => {
            document.getElementById('crop-name').textContent = res.prediction;
        }
    );

    // Initialize Fertilizer Recommendation
    handlePrediction(
        'fertilizer-form', 
        '/predict-fertilizer', 
        'fertilizer-result', 
        (res) => {
            const list = document.getElementById('fert-advice-list');
            list.innerHTML = '';
            res.recommendation.forEach(msg => {
                const li = document.createElement('li');
                li.innerHTML = `<span class="icon">🌱</span> ${msg}`;
                list.appendChild(li);
            });
        }
    );
});
