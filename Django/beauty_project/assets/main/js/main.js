const mouseIcon = document.getElementById('mouse_icon')
const mouseText = document.getElementById('mouse_text')

mouseIcon.addEventListener('mouseover', (event) => {
    mouseIcon.classList.add('hidden')
    mouseText.classList.remove('hidden')
})
//
mouseText.addEventListener('mouseleave', (event)=> {
    event.target.classList.add('hidden')
    mouseIcon.classList.remove('hidden')
})

// for (let i=1; i<=6; i++)
//     if (document.getElementById(`section_${i}`) !== null)
//         document.getElementById(`lnk_${i}`).classList.add('active')
//
