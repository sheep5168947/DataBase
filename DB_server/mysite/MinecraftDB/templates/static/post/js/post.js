
function addpost(){
    document.getElementById("addpost").style.display = "block";
    document.getElementById("deletpost").style.display = "none";
}
function deletpost(){
    document.getElementById("addpost").style.display = "none";
    document.getElementById("deletpost").style.display = "block";
}

function sendForm()
{
    var token = $('input[name=csrfmiddlewaretoken]').val();
    var Username=document.getElementById("Username").innerHTML
    var Title=document.getElementById("Title").value
    var Contents=document.getElementById("Contents").value
    console.log(Username)
    console.log(Title)
    console.log(Contents)

    var obj = {
        csrfmiddlewaretoken: token,
        Username :Username,
        Title : Title,
        Contents :Contents 
    };
     var json = JSON.stringify(obj);
    // var request = new XMLHttpRequest(); // xhr() 會建立非同步物件
    // request.open('POST', "http://127.0.0.1:8000/MinecraftDB/getPost/")
    // request.setRequestHeader('Content-Type', 'application/json')
    // request.send(json);

    $.ajax({
        type: 'POST',
        url: "http://127.0.0.1:8000/MinecraftDB/getPost/" ,
        data: obj ,
        dataType: json 
      });
      window.location.href="/MinecraftDB/post/"+Username+"/";
}
var test=document.getElementById("Submit")
test.addEventListener("click",sendForm)
=======
}
function sendDeleteForm()
{
    var token = $('input[name=csrfmiddlewaretoken]').val();
    var Username=document.getElementById("Poster").innerHTML
    var Title=document.getElementById("PostTitle").value
    console.log(Username)
    console.log(Title)
    console.log(Contents)

    var obj = {
        csrfmiddlewaretoken: token,
        Username :Username,
        Title : Title,
    };
     var json = JSON.stringify(obj);
    // var request = new XMLHttpRequest(); // xhr() 會建立非同步物件
    // request.open('POST', "http://127.0.0.1:8000/MinecraftDB/getPost/")
    // request.setRequestHeader('Content-Type', 'application/json')
    // request.send(json);

    $.ajax({
        type: 'POST',
        url: "http://127.0.0.1:8000/MinecraftDB/deletePost/" ,
        data: obj ,
        dataType: json 
      });
}
var SubmitPost=document.getElementById("Submit")
var DeletePost=document.getElementById("deletepost")
console.log(DeletePost)
SubmitPost.addEventListener("click",sendForm)
DeletePost.addEventListener("click",sendDeleteForm)
>>>>>>> 917c887f21b4ebdea6a272a904014595ca195573

