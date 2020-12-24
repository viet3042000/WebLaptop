var updateBtn = document.getElementsByClassName('delete');
for(var i = 0 ; i < updateBtn.length;i++){
    
    updateBtn[i].addEventListener('click',function(){

        Id = this.dataset.id;
        console.log(Id);
    if(user == 'AnonymousUser'){
        console.log('User is not authenticated')

    }else{
        var url ='/account/update_checkout/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'delete':"delete",'Id':Id})

    })
    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        location.reload();
    });
    }
 });

}