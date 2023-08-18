window.addEventListener('load', () => {
    document.querySelectorAll('.toggle-button')
    .forEach(button => {
        button.addEventListener('click', async (e) => {
            const itemId = button.dataset.item_id
            result = await ( 
                await fetch(
                    `${itemId}/`, 
                    {
                        method: 'POST', 
                        headers: {
                            "X-CSRFToken": document.cookie.split('csrftoken=')[1],
                            // "Accept": "application/json",
                            // 'Content-Type': 'application/json'
                            } 
                    }
                )).json()
            if (result.success) {
                button.innerHTML = button.innerHTML == 'True' ? 'False' : 'True'
            }
        });
    });
})