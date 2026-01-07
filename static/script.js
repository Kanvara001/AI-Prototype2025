document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('irisForm');
    const btn = document.getElementById('predictBtn');

    if(form) {
        form.addEventListener('submit', function() {
            // เปลี่ยนข้อความปุ่มเมื่อกด submit
            btn.innerHTML = 'Analyzing...';
            btn.style.opacity = '0.7';
            btn.style.cursor = 'wait';
        });
    }
});