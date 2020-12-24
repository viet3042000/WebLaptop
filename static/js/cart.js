var productId;
var action;
var quantity = 0;
$(window).scroll(function() {
    if($(window).scrollTop() == $(document).height() - $(window).height()) {
           // ajax call get data from server and append to the div
    }
});
$(document).on("click", '.update-cart', function(event) {
            productId = this.dataset.product;
            action = this.dataset.action;
            console.log("productID:",productId,"action:",action)


    console.log('User:'+user);
    if(user == 'AnonymousUser'){
        console.log('User is not authenticated')

    }else{
        UpdateCart(productId,action,1);
    }
});

// search
//document.getElementsByClassName("search-btn")[0].addEventListener("click",function(){
//    var url ='/store/'
//    fetch(url,{
//        method:'POST',
//        headers:{
//            'Content-Type':'application/json',
//            'X-CSRFToken':csrftoken,
//        },
//        name  = document.getElementById("myInput").value;
//        body:JSON.stringify({'name':name})
//
//    })
//    .then((response) =>{
//        return response.json();
//    })
//    .then((data) =>{
//        location.reload();
//    });
//})

var updateBtns = document.getElementsByClassName('update-cart2');
for(var i = 0 ; i < updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
            productId = this.dataset.product;
            action = this.dataset.action;
            console.log("productID:",productId,"action:")


    console.log('User:'+user);
    if(user == 'AnonymousUser'){
        console.log('User is not authenticated')

    }else{
        UpdateCart(productId,action,1);
    }
 });

}
var updateBtns = document.getElementsByClassName('update-cart1');
for(var i = 0 ; i < updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
            productId = this.dataset.product;
            action = this.dataset.action;
            quantity = document.getElementsByClassName('qty-numb')[0].value;
            console.log("productID:",productId,"action:",action,"quantity:",quantity)


    console.log('User:'+user);
    if(user == 'AnonymousUser'){
        console.log('User is not authenticated')

    }else{
        UpdateCart(productId,action,quantity);
    }
 });

}

//$(document).on("click", '.update-cart1', function(event) {
//     productId = this.dataset.product;
//            action = this.dataset.action;
//            console.log("productID:",productId,"action:",action)
//
//
//    console.log('User:'+user);
//    if(user == 'AnonymousUser'){
//        console.log('User is not authenticated')
//
//    }else{
//        UpdateCart(productId,action,0);
//    }
//});


//var updateBtns = document.getElementsByClassName('update-cart1');
//for(var i = 0 ; i < updateBtns.length;i++){
//    updateBtns[i].addEventListener('input',function(){
//           productId = this.dataset.product;
//           action = this.dataset.action;
//           quantity=this.value;
//           console.log("productID1:",productId,"action:",action,'quantity:',quantity)
//
//
//    console.log('User:'+user);
//    if(user == 'AnonymousUser'){
//        console.log('User is not authenticated')
//
//    }else{
//        if(action == 'update'){
//            UpdateCart(productId,action,quantity);
//        }
//        else UpdateCart(productId,action,0);
//    }
// });
//
//}
function UpdateCart(productId,action,quantity){
    var url ='/update_item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action,'quantity':quantity})

    })
    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        location.reload();
    });

}

$('select').on('change', function() {
if($('#id_price').val()==0){
    start = '';
    end = '';
}else if($('#id_price').val()==1){
    start = '0';
    end = '10000';
}
else if($('#id_price').val()==2){
    start = '10000';
    end = '20000';
}
else if($('#id_price').val()==3){
    start = '20000';
    end = '30000';
}else {
    start = '30000';
    end = '100000';
}
  $.ajax({

        type: "GET",
        url: "/store/"+ "?demand=" + $('#id_demand').val() + "&category=" + $('#id_category').val()+"&brand=" + $('#id_brand').val()+"&name=" + $('.input').val()+"&start_price=" + start+"&end_price=" + end,
        contentType: "application/json",
        dataType: 'json',
        success: function(response){
        let dataset = JSON.parse("["+response.products+"]")[0]
        data = '';
        console.log(dataset);
        $("#id_row").html('');
        for(var i = 0 ; i < dataset.length;i++){
           // $("#id_row").append('<div class="col-md-3 col-xs-6" style="margin-bottom:35px"><div class="product"><div class="product-img"><img src="/images/'+dataset[i].image+'" alt=""></div><div class="product-body"><p class="product-category">'+dataset[i].demand+'</p><h3 class="product-name"><a href="{% url "product" product.id %}">'+dataset[i].name+'</a></h3><h4 class="product-price">'+formatCash(String(dataset[i].price))+',000 Vnd</h4></div><div class="add-to-cart"><button data-product='+dataset[i].id+'  data-action = "add" class="add-to-cart-btn update-cart"><i class="fa fa-shopping-cart"></i> add to cart</button></div></div></div>')
            data = $("#id_row").append('<div class="col-md-3 col-xs-4"><div class="product"><a href=  "/product/'+dataset[i].id+'/"><div class="product-img"><img src="/images/'+dataset[i].image+'" alt="" style="width: 100%"></div></a><div class="product-body"><p class="product-category">'+dataset[i].demand+'</p><h3 class="product-name"><a href="/product/'+dataset[i].id+'/">'+dataset[i].name+'</a></h3><h4 class="product-price">'+formatCash(String(dataset[i].price))+',000 Vnd</h4></div><div class="add-to-cart"><button data-product='+dataset[i].id+'  data-action = "add" class="add-to-cart-btn update-cart"><i class="fa fa-shopping-cart"></i> Thêm vào giỏ hàng </button></div></div></div>');
             console.log('<div class="col-md-3 col-xs-4"><div class="product"><a href= "/product/'+dataset[i].id+'/>')
        }

        $(".store-pagination").html('');
      }
   })
});
function formatCash(str) {
 	return str.split('').reverse().reduce((prev, next, index) => {
 		return ((index % 3) ? next : (next + ',')) + prev
 	})
}
