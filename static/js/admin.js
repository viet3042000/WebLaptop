var updateBtns = document.getElementsByClassName('update_user');
for(var i = 0 ; i < updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
           Id = this.dataset.user;
           action = this.dataset.action;
           console.log("customerID:",Id,"action:",action)
           Update(Id,action);

 });

}
function Update(id,action){
    var url ='/boss/update_user/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'id':id,'action':action})

    })
    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        location.reload();
    });

}