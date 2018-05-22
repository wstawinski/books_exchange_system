$(document).ready(function() {

$("#id_tag").keydown(function(event){
    if(event.keyCode == 13) {
      event.preventDefault();
      blurAll();
      return false;
    }
  });

function blurAll(){
 var tmp = document.createElement("input");
 document.body.appendChild(tmp);
 tmp.focus();
 document.body.removeChild(tmp);
}

});
