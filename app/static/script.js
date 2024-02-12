$(document).ready(init)

async function init(){
    let cupcakes = await axios.get("/api/cupcakes")
    let $divCupcakes = $("#divCupcakes")
    for(let i=0; i<cupcakes.data.cupcakes.length;i++){
        let $cupcake = $(cupcakes.data.cupcakes[i])
        let $newList = $('<ul>')
        $newList.append(`<h2>Cupcake ${i+1}</h2>`)

        // Get data
        let $flavor = $cupcake[0].flavor
        let $size = $cupcake[0].size
        let $rating = $cupcake[0].rating
        let $image = $cupcake[0].image

        $newList.append(`<li><b>Flavor:</b> ${$flavor}</li>`)
        $newList.append(`<li><b>Size:</b> ${$size}</li>`)
        $newList.append(`<li><b>Size:</b> ${$rating}</li>`)
        $newList.append(`<img src="${$image}"/>`)
        $divCupcakes.append($newList)

    }
}

