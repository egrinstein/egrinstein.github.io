
$(document).ready( function(){

     $.ajax({
         url:'http://plot-generator.herokuapp.com',
         type:'GET',
         success: function(data){
               $('code#plotgen').html(data["text"]);
         }
     });
     
     $('button#plotgen').on('click', function () {
        var Status = $(this).val();
        $('code#plotgen').html("Loading...")
          $.ajax({
              url:'http://plot-generator.herokuapp.com',
              type:'GET',
              success: function(data){
                    $('code#plotgen').html(data["text"]);
              }
          });
    });
     
})

