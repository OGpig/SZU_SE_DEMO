let _btn=document.querySelector('#btn')
let _content=document.querySelector('.content')
let _send=document.querySelector('#send')
let _list=document.querySelector('.list')
let _input=document.querySelector('input')
let _text=document.querySelector('textarea')
let _list1=document.querySelector('.list1')
let _select=document.querySelector('select')
let img=["./img/1.jpg","./img/2.jpg","./img/3.jpg","./img/4.jpg"]
_btn.onclick=function(){
    _content.style.display='block'
    _list.style.display='none'
}
_send.onclick=function(){
    let randon=Math.floor(Math.random()*4)
    let _li = document.createElement('li')
    let date=new Date()
    let year=date.getFullYear()
    let month=date.getMonth()+1
        month=zero(month)
    let data=date.getDate()
        data=zero(data)
    let hours=date.getHours()
        hours=zero(hours)
    let minutes=date.getMinutes()
        minutes=zero(minutes)
        _li.innerHTML = `
        <img src=${img[randon]}>
        <span class="right">
            <p class="title">${_input.value}</p>
            <p>${_text.value}</p>
            <p><span class="bankuai">板块:&ensp;${_select.value}</span>&emsp;&emsp;<span class="time">发表时间:
                ${year}-${month}-${data}&emsp;${hours}:${minutes}
                </span></p>
        </span>
        `
        _list1.insertBefore(_li, _list1.firstChild)
        _input.value=''
        _text.value=''
        _select.value='请选择板块'
    _content.style.display='none'
    _list.style.display='block'
}
function zero(num){
    if(num<10){
        return "0"+num
    }
    return num
}