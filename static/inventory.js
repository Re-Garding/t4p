
fetch('/inventory')
.then(response =>response.json())
.then(inventory => {

    for(const item in inventory){
        
        div = `<div class='item_icon' id=${inventory[item]['id']}>
            <img class='icon_img' src=${inventory[item]['pic_path']} />
            <div id='title'>${inventory[item]['title']}</div>
            <div>In Stock: ${inventory[item]['total_inv']}</div>
        </div>`
        console.log(div)
        document.querySelector('.container').insertAdjacentHTML("beforeend", div)

        document.querySelector(`#${inventory[item]['id']}`).addEventListener('click', (evt) => {
            evt.preventDefault();
            editRoute(inventory[item]['id'])

        })
    }
})

function editRoute(id){
    window.location = `/admin/edit/${id}`
}
