const fetchData = async (url) => {
    data =  await (await fetch(url)).json()

    return data
}

const nextAndPreviousLinksInit = (nextURL, previousURL) => {
    stepLinksContainer = document.querySelector('.step-links')
    stepLinksContainer.innerHTML = ''
    
    if (data.previous) {
        btn = document.createElement('a')
        
        btn.innerHTML = '&laquo; previous'
        btn.href = '#'
        btn.onclick = () => proccessItems(previousURL)
        stepLinksContainer.appendChild(btn)
    }

    if (data.next) {
        btn = document.createElement('a')
        
        btn.innerHTML = 'next &raquo;'
        btn.href = '#'
        btn.onclick = () => proccessItems(nextURL)
        stepLinksContainer.appendChild(btn)
    }
}

const proccessItems = async (url) => {
    data = await fetchData(url)

    row = document.getElementsByClassName('row')[0]
    row.innerHTML = ''
    
    if (data.detail) {
        row.innerHTML = 'no data found'
        return
    }

    nextAndPreviousLinksInit(data.next, data.previous)

    for(item of data.results) {
        row.innerHTML += `
            <div class="col">
                <a href="item/${item['id']}" class="card-link">
                    <div class="card" style="width: 18rem">
                        <img src="${item['model']['images'][0]['image']}" class="card-img-top" alt="Faild to load picture" />
                        <div class="card-body">
                            <h5 class="card-title" title="${item['model']['manufacturer']['name']} ${item['model']['name']}">${item['model']['manufacturer']['name']} ${item['model']['name']}</h5>
                            <p class="card-text">
                                <small title="CPU: ${item['cpu_type']['name']['name'] + ' ' + item['cpu_type']['cpu_type']}">CPU: ${item['cpu_type']['name']['name'] + ' ' + item['cpu_type']['cpu_type']}</small>
                                <small title="Ram: ${item['ram_cache'] + 'gb-' + item['ram_type']['name']}">Ram: ${item['ram_cache'] + 'gb-' + item['ram_type']['name']}</small>
                                <small title="HDD: ${item['hdd_size']}${item['hdd_size'] > 20 ? 'gb-' : 'tb-'}${item['hdd_type']['name']}">HDD: ${item['hdd_size']}${item['hdd_size'] > 20 ? 'gb-' : 'tb-'}${item['hdd_type']['name']}</small>
                                <small title="GPU: ${item['gpu']['name']}">GPU: ${item['gpu']['name']}</small>
                            </p>
                            <a href="item/${item['id']}" class="btn btn-primary">More Info</a>
                        </div>
                    </div>
                </a>
            </div>
        `
    }
}

submitForm = (event) => {
    event.preventDefault();

    btn = document.querySelector('button[type="submit"]')
    spinner = btn.firstChild.nextElementSibling
    spinner.classList.remove('spinner-border-hidden')
    spinner.classList.add('spinner-border')
    btn.disabled = true

    const types = document.querySelectorAll('input[name="type"][type="checkbox"]:checked');
    const cpus = document.querySelectorAll('input[name="cpu"][type="checkbox"]:checked');
    const cpu_types = document.querySelectorAll('input[name="cpu_type"][type="checkbox"]:checked');
    const ram_types = document.querySelectorAll('input[name="ram_type"][type="checkbox"]:checked');
    const hdd_types = document.querySelectorAll('input[name="hdd_type"][type="checkbox"]:checked');
    const gpus = document.querySelectorAll('input[name="gpu"][type="checkbox"]:checked');

    let url = 'api/items';
    url += proccessQueryStrParams(
        types, 
        cpus, 
        cpu_types, 
        ram_types, 
        hdd_types, 
        gpus)

    proccessItems(url)

    // btn.disabled = false
    btn.disabled = false
    spinner.classList.remove('spinner-border')
    spinner.classList.add('spinner-border-hidden')
}

const proccessQueryStrParams = (...elements) => {
    list = []

    for (element of elements) {
        elem_values_list = []

        element.forEach( (elem) => {
            elem_values_list.push(elem.value);
        });
        
        list.push(
            encodeURIComponent(
                elem_values_list.join(',')
                )
            )
    }

    return '/' + list.join('/') + '/'
}

const proccessCPUTypesList = async (url) => {
    data = await fetchData(url)

    cpu_type_div = document.getElementById('cpu_type')

    if (data.length == 0) {
        cpu_type_div.innerHTML = 'select cpu'
        return
    } else {
        cpu_type_div.innerHTML = ''
    }

    data.forEach((item) => {
        cpu_type_div.innerHTML += `
        <div class="mb-3" style="display: flex; ">
            <input type="checkbox" class="form-check-input" name="cpu_type" value="${item['id']}" id="${item['cpu_type']}">
            <label for="${item['cpu_type']}" class="form-check-label container-fluid">${item['cpu_type']}</label>
        </div>`
    })
    
}

window.addEventListener('load', (e) => {
    const form = document.getElementById('form');
    form.addEventListener('submit', submitForm)
    
    const cpus = document.querySelectorAll('input[name="cpu"][type="checkbox"]');

    cpus.forEach((cpu) => {
        cpu.addEventListener('click', (e) => {
            const cpus = document.querySelectorAll('input[name="cpu"][type="checkbox"]:checked');
            cpu_list = []

            cpus.forEach((cpu) => {
                cpu_list.push(cpu.value)
            })

            let url = 'api/cputypes/';
            url += encodeURIComponent(cpu_list.join(','))
            url += '/'

            proccessCPUTypesList(url)
        })  
    })

    // sidebar toggle 
    toggle = document.querySelector('.toggleee')
            
    toggle.addEventListener('click', () => {
        document.querySelector('.topics').classList.toggle('active')
    })
})
