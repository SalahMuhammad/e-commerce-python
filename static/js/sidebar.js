window.addEventListener('load', (e) => {    
    getCPUTypes()

    checkboxesAction()

    // sidebar toggle 
    toggle = document.querySelector('.toggleee')
            
    toggle.addEventListener('click', () => {
        document.querySelector('.topics').classList.toggle('active')
    })
})

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

    nextAndPreviousLinksInit(data.next, data.previous)
    
    if (data.detail || data.results.length == 0) {
        row.innerHTML = 'no data found'
        return
    }

    for(item of data.results) {
        row.innerHTML += `
            <div class="col">
                <a href="item/${item['id']}" class="card-link">
                    <div class="card" style="width: 18rem">
                        <img src="${item['model']['images'].length == 0 ? '' : item['model']['images'][0]['image']}" class="card-img-top" alt="Faild to load picture" />
                        <div class="card-body">
                            <h5 class="card-title" title="${item['model']['manufacturer']['name']} ${item['model']['name']}">${item['model']['manufacturer']['name']} ${item['model']['name']}</h5>
                            <p class="card-text">
                                <small title="CPU: ${item['cpu_type']['name']['name'] + '-' + item['cpu_type']['cpu_type']}">CPU: ${item['cpu_type']['name']['name'] + '-' + item['cpu_type']['cpu_type']}</small>
                                <small title="Ram: ${item['ram_cache'] + 'gb ' + item['ram_type']['name']}">Ram: ${item['ram_cache'] + 'gb ' + item['ram_type']['name']}</small>
                                <small title="HDD: ${item['hdd_size']}${item['hdd_size'] > 20 ? 'gb ' : 'tb '}${item['hdd_type']['name']}">HDD: ${item['hdd_size']}${item['hdd_size'] > 20 ? 'gb ' : 'tb '}${item['hdd_type']['name']}</small>
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

getItems = () => {
    loadingSpinner = document.querySelector('.spinner-border-hidden')
    loadingSpinner.classList.remove('spinner-border-hidden')
    loadingSpinner.classList.add('spinner-border')

    const types = document.querySelectorAll('input[name="type"][type="checkbox"]:checked');
    const cpus = document.querySelectorAll('input[name="cpu"][type="checkbox"]:checked');
    const cpu_types = document.querySelectorAll('input[name="cpu_type"][type="checkbox"]:checked');
    const ram_types = document.querySelectorAll('input[name="ram_type"][type="checkbox"]:checked');
    const hdd_types = document.querySelectorAll('input[name="hdd_type"][type="checkbox"]:checked');

    setSelectedCount(
        types.length, cpus.length, cpu_types.length, 
        ram_types.length, hdd_types.length
    )

    let url = 'api/items';
    url += proccessQueryStrParams(
        types, 
        cpus, 
        cpu_types, 
        ram_types, 
        hdd_types
    )

    proccessItems(url)

    loadingSpinner.classList.remove('spinner-border')
    loadingSpinner.classList.add('spinner-border-hidden')
}

/**
 * it's process multiple params with same name in single parameter, 
 * with multi values
 * 
 * @param  {...any} elements 
 * @returns 
 */
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
    
    document.querySelectorAll('input[type="checkbox"][name="cpu_type"]').forEach(item => {
        item.onclick = getItems
    });
}

const checkboxesAction = () => {
    checkboxes = document.querySelectorAll('input[type="checkbox"]')
    checkboxes.forEach((checkbox) => {
        checkbox.onclick =  getItems
    })
}

const getCPUTypes = () => {
    const cpus = document.querySelectorAll('input[name="cpu"][type="checkbox"]');

    cpus.forEach((cpu) => {
        cpu.addEventListener('click', (e) => {
            const cpuss = document.querySelectorAll('input[name="cpu"][type="checkbox"]:checked');
            cpu_list = []

            cpuss.forEach((cpu) => {
                cpu_list.push(cpu.value)
            })

            let url = 'api/cputypes/';
            url += encodeURIComponent(cpu_list.join(','))
            url += '/'

            proccessCPUTypesList(url)
        })  
    })
}

const setSelectedCount = (...valuesList) => {
    selectedCount = document.querySelectorAll('.selected-count')

    for (elem in selectedCount)
        selectedCount[elem].innerHTML = '(' + valuesList[elem] +')'
}